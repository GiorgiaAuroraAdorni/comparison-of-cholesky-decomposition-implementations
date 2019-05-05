#!/usr/bin/env python3

from collections import defaultdict
import matplotlib.pyplot as plt
from util import plot_results
import csv

# Each value in each column is appended to a list
columns = defaultdict(list)

with open('matlab/output/matlabOutput.csv') as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            if k != 'name':
                columns[k].append(float(v))  # append the value into the appropriate list based on column name k
            else:
                columns[k].append(v)

# Plot based on the rows number of each matrix
fig, axes = plt.subplots(nrows=3, ncols=1,figsize=(6, 8))

plt.subplot(3, 1, 1)
plot_results(columns['rows'], columns['solveTime'], 'Matrix Size', 'Time (seconds)', 'Time required to solve the systems')

plt.subplot(3, 1, 2)
plot_results(columns['rows'], columns['relativeError'], 'Matrix Size', 'Relative Error', 'Relative errors')

plt.subplot(3, 1, 3)
plot_results(columns['rows'], columns['maxMemory'], 'Matrix Size', 'Max Memory (byte)', 'Max memory used to solve the systems')

plt.tight_layout()
plt.savefig('resultOnSize.pdf')
plt.show()

# Plot based on the number of non zeros of each matrix
fig, axes = plt.subplots(nrows=3, ncols=1,figsize=(6, 8))

plt.subplot(3, 1, 1)
plot_results(columns['nonZeros'], columns['solveTime'], 'Non Zeros', 'Time (seconds)', 'Time required to solve the systems')

plt.subplot(3, 1, 2)
plot_results(columns['nonZeros'], columns['relativeError'], 'Non Zeros', 'Relative Error', 'Relative errors')

plt.subplot(3, 1, 3)
plot_results(columns['nonZeros'], columns['maxMemory'], 'Non Zeros', 'Max Memory (byte)', 'Max memory used to solve the systems')

plt.tight_layout()
plt.savefig('resultOnNonZeros.pdf')
plt.show()
