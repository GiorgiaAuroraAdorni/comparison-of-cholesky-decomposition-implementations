#!/usr/bin/env python3

import psutil
import sys
import time

pid = int(sys.argv[1])
p = psutil.Process(pid)

initial_memory = p.memory_info().rss
max_memory = 0

print("Monitoring " + p.name() + "...")
print("Initial memory usage:", initial_memory)

try:
    while True:
        current_memory = p.memory_info().rss

        if max_memory < current_memory:
            max_memory = current_memory

        time.sleep(0.050) # 20Hz sampling rate
except:
    print("Exception:", sys.exc_info()[0])

memory_usage = max_memory - initial_memory

print("Max memory usage:", max_memory)
print("Delta memory usage:", memory_usage)
