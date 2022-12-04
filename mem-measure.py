import time
import argparse
import sys
import psutil
import os

def get_used_mem() -> int:
    mem_file = "/proc/meminfo"
    with open(mem_file, "r") as f:
        data = f.readlines()
    total_mem = data[0]
    avail_mem = data[2]
    used_mem = int(total_mem.split()[1]) - int(avail_mem.split()[1])
    return used_mem

def get_cpu_usage_1m() -> float:
    load1m = (psutil.getloadavg()[0]/os.cpu_count()) * 100
    return load1m

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'mem-measure.py')
    parser.add_argument("-m", "--mem_filename")
    parser.add_argument("-c", "--cpu_filename")
    args = parser.parse_args()
    counter = 0
    while True:
        with open(args.mem_filename, "a") as f:
            f.write(str(get_used_mem())+"\n")
        time.sleep(5)
        counter = counter + 1
        if counter % 12 == 0:
            with open(args.cpu_filename, "a") as f:
                f.write(str(get_cpu_usage_1m())+"\n")
            counter = 0
