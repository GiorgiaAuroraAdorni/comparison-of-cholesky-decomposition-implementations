#!/usr/bin/env python3

from util import get_file_list, monitor_memory

import subprocess
import csv
import os

os.chdir("cpp")

matrices_dir = "matrices"

file_list, matrix_list = get_file_list(matrices_dir, ".mtx.gz")

cpp_path = "cmake-build-release/cholesky-cpp"

with open('output/cppOutput.csv', 'w') as output_csv:
    writer = csv.writer(output_csv, delimiter=',')
    writer.writerow(['name', 'rows', 'nonZeros', 'loadTime', 'solveTime', 'relativeError', 'maxMemory', 'memoryUsage'])

    for i in range(len(file_list)):
        file_name = file_list[i]
        matrix_name = matrix_list[i]

        command = [cpp_path, file_name]

        subproc = subprocess.Popen(command, stdout=subprocess.PIPE, encoding="utf-8")

        max_memory, memory_usage = monitor_memory(subproc)

        reader = csv.reader(subproc.stdout)
        row = next(reader)
        row.append(max_memory)
        row.append(memory_usage)

        writer.writerow(row)
        output_csv.flush()

output_csv.close()
