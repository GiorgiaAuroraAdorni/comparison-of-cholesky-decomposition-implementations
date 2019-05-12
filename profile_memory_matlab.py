#!/usr/bin/env python3

from util import get_matrix_list, monitor_memory

import subprocess
import csv
import os

os.chdir("matlab")

matrices_dir = "matrices"

file_list, matrix_list = get_matrix_list(matrices_dir, ".mat")

matlab_path = "/usr/local/bin/matlab"

with open('output/matlabOutput.csv', 'w') as output_csv:
    writer = csv.writer(output_csv, delimiter=',')
    writer.writerow(['name', 'rows', 'nonZeros', 'loadTime', 'solveTime', 'relativeError', 'maxMemory', 'memoryUsage'])

    for i in range(len(file_list)):
        file_name = file_list[i]
        matrix_name = matrix_list[i]

        command = [matlab_path, "-nodesktop", "-nosplash", "-r", "processFile('" + file_name + "', '" + matrix_name + "'); quit"]

        subproc = subprocess.Popen(command)

        max_memory, memory_usage = monitor_memory(subproc)

        with open('output/' + matrix_name + '.csv', 'r') as input_csv:
            reader = csv.reader(input_csv)
            row = next(reader)
            row.append(max_memory)
            row.append(memory_usage)

        writer.writerow(row)
        output_csv.flush()

        input_csv.close()

output_csv.close()
