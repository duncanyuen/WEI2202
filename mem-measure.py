import time
import subprocess
import argparse
import sys

def get_used_mem() -> int:
    mem_file = "/proc/meminfo"
    with open(mem_file, "r") as f:
        data = f.readlines()
    total_mem = data[0]
    avail_mem = data[2]
    used_mem = int(total_mem.split()[1]) - int(avail_mem.split()[1])
    return used_mem

def get_cpu_usage() -> float:
    output = subprocess.check_output("mpstat -u")
    print(output)

if __name__ == "__main__":
    get_cpu_usage()
    sys.exit(0)
    parser = argparse.ArgumentParser(
                    prog = 'mem-measure.py')
    parser.add_argument("-m", "--mem_filename")
    args = parser.parse_args()
    while True:
        with open(args.mem_filename, "a") as f:
            f.write(str(get_used_mem())+"\n")
        time.sleep(5)