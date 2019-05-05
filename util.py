#!/usr/bin/env python3

import matplotlib.pyplot as plt
import psutil
import time
import sys
import os


def monitor_memory(subproc):
    pid = subproc.pid
    proc = psutil.Process(pid)

    if sys.platform.startswith("linux"):
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


def get_file_list(directory, extension):
    matrix_list = list()
    file_list = list()

    # Iterate over all the entries
    for file in os.listdir(directory):
        if file.endswith(extension):
            matrix_list.append(file)
            # Store full path
            file_list.append(os.path.join(directory, file))

    return file_list, matrix_list


def plot_results(x, y, xlabel, ylabel, title):
    sorted_x, sorted_y = zip(*sorted(zip(x, y)))
    plt.plot(sorted_x, sorted_y, 'go-', linewidth=2, markersize=6)

    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(xlabel, fontsize=6)
    plt.ylabel(ylabel, fontsize=6)
    plt.title(title, weight='bold', fontsize=8)
