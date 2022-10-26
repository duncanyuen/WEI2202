import requests
import time

def get_cpu_temp():
    temp_file = "/sys/class/thermal/thermal_zone0/temp"
    with open(temp_file, "r") as f:
        temp = f.readlines()[0]
    temp = float(temp)/1000
    return temp

def update(host = "192.168.10.111", port = "5000", path = "update"):
    url = "http://" + host + ":" + port + "/" + path
    temp = get_cpu_temp()
    temp_data = {"temperature": str(temp)}
    r = requests.post(url, json = temp_data)
    return r.status_code

if __name__ == "__main__":
    while(True):
        status = update()
        time.sleep(5)

