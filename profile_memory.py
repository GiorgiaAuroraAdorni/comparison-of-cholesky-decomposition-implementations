#!/usr/bin/env python3

import psutil
import sys

pid = int(sys.argv[1])
p = psutil.Process(pid)

initial_memory = p.memory_info().rss
max_memory = 0

print("Monitoring " + p.name() + "...")

try:
    while True:
        current_memory = p.memory_info().rss

        if max_memory < current_memory:
            max_memory = current_memory

except KeyboardInterrupt:
    pass

memory_usage = max_memory - initial_memory

print(memory_usage)
