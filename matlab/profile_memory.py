#!/usr/bin/env python3

import pandas as pd
import subprocess
import psutil
import time
import sys
import csv
import os


def monitor_memory(subproc):
    pid = subproc.pid
    proc = psutil.Process(pid)

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

    memory_usage = max_memory - initial_memory

    print("Max memory usage:", max_memory)
    print("Delta memory usage:", memory_usage)

    return max_memory, memory_usage


def get_file_list(directory):
    matrix_list = list()
    file_list = list()

    # Iterate over all the entries
    for file in os.listdir(directory):
        if file.endswith(".mat"):
            matrix_list.append(file)
            # Store full path
            file_list.append(os.path.join(directory, file))

    return file_list, matrix_list


# FIXME
matrices_dir = "matrices"

file_list, matrix_list = get_file_list(matrices_dir)

matlab_path = "/usr/local/bin/matlab"

with open('output/matlabOutput.csv', 'w') as output_csv:
    writer = csv.writer(output_csv, delimiter=',')
    writer.writerow(['name', 'rows', 'nonZeros', 'loadTime', 'solveTime', 'relativeError', 'maxMemory', 'memoryUsage'])

    for i in range(len(file_list)):
        file_name = file_list[i]
        matrix_name = matrix_list[i]

        command = [matlab_path, "-nodesktop", "-nosplash", "-r", "processFile('" + file_name + "', '" + matrix_name + "'); quit"]

        subproc = subprocess.Popen(command)

        if sys.platform.startswith("linux"):
            with open('/proc/' + str(subproc.pid) + '/oom_score_adj', 'w') as score:
                score.write('1000')

        max_memory, memory_usage = monitor_memory(subproc)

        with open('output/' + matrix_name + '.csv', 'r') as input_csv:
            reader = csv.reader(input_csv)
            row = next(reader)
            row.append(max_memory)
            row.append(memory_usage)

        writer.writerow(row)

        input_csv.close()

output_csv.close()
