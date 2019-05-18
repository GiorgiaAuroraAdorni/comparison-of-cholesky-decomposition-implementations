#!/usr/bin/env python3

from collections import defaultdict
import psutil
import time
import sys
import csv
import os


def monitor_memory(subproc):
    pid = subproc.pid
    proc = psutil.Process(pid)

    ### Only for MATLAB
    if sys.platform.startswith("win"):
        while not proc.children():
            pass

        proc = proc.children()[0]
    ###
    elif sys.platform.startswith("linux"):
        with open('/proc/' + str(pid) + '/oom_score_adj', 'w') as score:
            score.write('1000')

    initial_memory = proc.memory_info().rss
    max_memory = 0

    print("Monitoring " + proc.name() + "...")
    print("Initial memory usage:", initial_memory)

    try:
        while subproc.poll() is None:
            current_memory = proc.memory_info().rss

            if max_memory < current_memory:
                max_memory = current_memory

            time.sleep(0.050)  # 20Hz sampling rate

    except:
        print("Exception:", sys.exc_info()[0])
        
    print("Process exited with code: ", subproc.returncode)

    memory_usage = max_memory - initial_memory

    print("Max memory usage:", max_memory)
    print("Delta memory usage:", memory_usage)

    return max_memory, memory_usage


def get_matrix_list(directory, extension):
    matrix_list = list()
    file_list = list()

    # Iterate over all the entries
    for file in os.listdir(directory):
        if file.endswith(extension):
            matrix_list.append(file)
            # Store full path
            file_list.append(os.path.join(directory, file))

    return file_list, matrix_list


def get_file(directory, filename):
    out = ""

    # Iterate over all the entries
    for file in os.listdir(directory):
        if file.endswith(filename):
            # Store full path
            out = (os.path.join(directory, file))

    return out


def extract_columns(directory):
    columns = defaultdict(list)

    with open(directory, 'r') as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                if k != 'name':
                    columns[k].append(float(v))  # append the value into the appropriate list based on column name k
                else:
                    columns[k].append(v)

    return columns
