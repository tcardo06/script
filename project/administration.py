from datetime import datetime, timedelta
from sys import argv

from influxdb_client.client.write_api import SYNCHRONOUS

import time
import argparse
import psutil
import influxdb_client


bucket = "coding"
org = "coding"
# token to change depending on the user
token = "1PSoQMREDKmqmOmeCcTgRPnG2BFmnO003YtGyXLV4bZfAfkKHhLlqnBqqcBNnu_62uDi09bec8bp6i4ZLPNRyw=="
# Store the URL of your InfluxDB instance
url = "http://localhost:8086/"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

NAME = argv[0]


# function that get the metrics
def system_info_all():
    info = {
        # CPU
        "Number of cores in system": f"{psutil.cpu_count(logical=False)}",
        "CPU Statistics": f"{psutil.cpu_stats()}",
        "CPU frequency": f"{psutil.cpu_freq()}",
        "Average system load ": f"{psutil.getloadavg()}",
        "CPU in use": f"{psutil.cpu_percent(interval=.1)}%",
        "Time on CPU": timedelta(seconds=psutil.cpu_times().system + psutil.cpu_times().user),

        # Memory
        "Memory in use": f"{psutil.virtual_memory().percent}%",
        "Memory available": f"{psutil.virtual_memory().available / (1024 ** 3):,.3f} GiB",
        "Memory swap": f"{psutil.swap_memory()}",

        # Networks
        "Net counters": f"{psutil.net_io_counters()}",
        "Net addresses": f"{psutil.net_if_addrs()}",
        "Net stats": f"{psutil.net_if_stats()}",

        # Disk
        "Disk partition": f"{psutil.disk_partitions()}",
        "Disk in use": f"{psutil.disk_usage('/').percent}%",
        "Disk free": f"{psutil.disk_usage('/').free / (1024 ** 3):,.3f} GiB%",
        "Disk counters": f"{psutil.net_io_counters()}",

    }

    cpu_usage = influxdb_client.Point("cpu_usage").tag("emetteur", "localhost").field("utilisation", psutil.cpu_percent(interval=.1))
    disk_usage = influxdb_client.Point("disk_usage").tag("emetteur", "localhost").field("utilisation", psutil.disk_usage('/').percent)
    memory_usage = influxdb_client.Point("memory_usage").tag("emetteur", "localhost").field("utilisation", psutil.virtual_memory().percent)
    write_api.write(bucket=bucket, org=org, record=cpu_usage)
    write_api.write(bucket=bucket, org=org, record=disk_usage)
    write_api.write(bucket=bucket, org=org, record=memory_usage)


def system_info_cpu():
    info_cpu = {
        # CPU
        "Number of cores in system": f"{psutil.cpu_count(logical=False)}",
        "CPU Statistics": f"{psutil.cpu_stats()}",
        "CPU frequency": f"{psutil.cpu_freq()}",
        "Average system load ": f"{psutil.getloadavg()}",
        "CPU in use": f"{psutil.cpu_percent(interval=.1)}%",
        "Time on CPU": timedelta(seconds=psutil.cpu_times().system + psutil.cpu_times().user),

    }
    print("\n\n SYSTEM INFO CPU\n\n" + "\n".join([f"{key}: {value}" for key, value in info_cpu.items()]))


def system_info_memory():
    info_memory = {
        # Memory
        "Memory in use": f"{psutil.virtual_memory().percent}%",
        "Memory available": f"{psutil.virtual_memory().available / (1024 ** 3):,.3f} GiB",
        "Memory swap": f"{psutil.swap_memory()}",

    }
    print("\n\n SYSTEM INFO MEMORY\n\n" + "\n".join([f"{key}: {value}" for key, value in info_memory.items()]))


def system_info_networks():
    info = {
        # Networks
        "Net counters": f"{psutil.net_io_counters()}",
        "Net addresses": f"{psutil.net_if_addrs()}",
        "Net stats": f"{psutil.net_if_stats()}",

    }
    print("\n\n SYSTEM INFO NETWORKS\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


def system_info_disk():
    info = {
        # Disk
        "Disk partition": f"{psutil.disk_partitions()}",
        "Disk in use": f"{psutil.disk_usage('/').percent}%",
        "Disk free": f"{psutil.disk_usage('/').free / (1024 ** 3):,.3f} GiB%",
        "Disk counters": f"{psutil.net_io_counters()}",

    }
    print("\n\n SYSTEM INFO DISK\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interval", help="echo the interval", type=int)
args = parser.parse_args()

while True:
    time.sleep(args.interval)
    system_info_all()

