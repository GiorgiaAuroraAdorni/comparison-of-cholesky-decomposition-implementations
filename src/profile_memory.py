import psutil
import sys

memory_usage = 0

PID = int(sys.argv[1])

initial_memory = psutil.Process(PID).memory_info().rss / 2. ** 30

print("Monitoring " + psutil.Process(PID).name())

try:
    while True:
        current_mem = psutil.Process(PID).memory_info().rss / 2. ** 30
        if current_mem > memory_usage:
            memory_usage = current_mem
except:
    e = sys.exc_info()[0]
    print("Error: " )
    print(e)
    pass

print(memory_usage - initial_memory)
