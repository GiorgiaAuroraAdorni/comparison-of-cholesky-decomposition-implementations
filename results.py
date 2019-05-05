#!/usr/bin/env python3

from collections import defaultdict
import matplotlib.pyplot as plt
import csv

# each value in each column is appended to a list
columns = defaultdict(list)

with open('matlab/output/matlabOutput.csv') as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            if k != 'name':
                columns[k].append(float(v))  # append the value into the appropriate list based on column name k
            else:
                columns[k].append(v)

# plot 1
plt.subplot(2, 3, 1)
new_rows, new_solveTime = zip(*sorted(zip(columns['rows'], columns['solveTime'])))

plt.plot(new_rows, new_solveTime, 'bo-', linewidth=2, markersize=6)
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Matrix size', fontsize=6)
plt.ylabel('Time (seconds)', fontsize=6)
plt.title("Time required to solve the systems", weight='bold', fontsize=8)

# plot 2
plt.subplot(2, 3, 2)
new_rows, new_relativeError = zip(*sorted(zip(columns['rows'], columns['relativeError'])))

plt.plot(new_rows, new_relativeError, 'bo-', linewidth=2, markersize=6)
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Matrix size', fontsize=6)
plt.ylabel('Relative Error', fontsize=6)
plt.title("Relative errors", weight='bold', fontsize=8)

# plot 3
plt.subplot(2, 3, 3)
new_rows, new_maxMemory = zip(*sorted(zip(columns['rows'], columns['maxMemory'])))

plt.plot(new_rows, new_maxMemory, 'bo-', linewidth=2, markersize=6)
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Matrix size', fontsize=6)
plt.ylabel('Max Memory (byte)', fontsize=6)
plt.title("Max memory used to solve the systems", weight='bold', fontsize=8)

# plot 4
plt.subplot(2, 3, 4)
new_nonZeros, new_solveTime = zip(*sorted(zip(columns['nonZeros'], columns['solveTime'])))

plt.plot(new_nonZeros, new_solveTime, 'bo-', linewidth=2, markersize=6)
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Non Zeros', fontsize=6)
plt.ylabel('Time (seconds)', fontsize=6)
plt.title("Time required to solve the systems", weight='bold', fontsize=8)

# plot 5
plt.subplot(2, 3, 5)
new_nonZeros, new_relativeError = zip(*sorted(zip(columns['nonZeros'], columns['relativeError'])))

plt.plot(new_nonZeros, new_relativeError, 'bo-', linewidth=2, markersize=6)
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Non Zeros', fontsize=6)
plt.ylabel('Relative Error', fontsize=6)
plt.title("Relative errors", weight='bold', fontsize=8)

# plot 6
plt.subplot(2, 3, 6)
new_nonZeros, new_maxMemory = zip(*sorted(zip(columns['nonZeros'], columns['maxMemory'])))

plt.plot(new_nonZeros, new_maxMemory, 'bo-', linewidth=2, markersize=6)
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Non Zeros', fontsize=6)
plt.ylabel('Max Memory (byte)', fontsize=6)
plt.title("Max memory used to solve the systems", weight='bold', fontsize=8)

plt.savefig('matlab.pdf')
plt.show()

