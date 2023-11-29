import os
import psutil

p = psutil.Process(os.getpid())

counter = 0
while True:
    if counter % 1000 == 0:
        print(p.cpu_percent())
    counter += 1