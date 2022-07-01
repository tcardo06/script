from datetime import datetime, timedelta
from sys import argv

#import temperature
from influxdb_client.client.write_api import SYNCHRONOUS

import time
import argparse
import psutil
import influxdb_client


bucket = "coding"
org = "coding"
token = "pfgjQDVdiB0Iu6u7y2FaIbMSf6jpwRO7cP4de8wgbj0ED8Q3ejGFtmTNvLd7s2KY9E5oGVb9hJju9muSXF-EHg=="
# Store the URL of your InfluxDB instance
url = "http://localhost:8086/"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague")
write_api.write(bucket=bucket, org=org, record=p)

query_api = client.query_api()
query = ' from(bucket:"coding")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "my_measurement")\
|> filter(fn: (r) => r.location == "Prague")'
result = query_api.query(org=org, query=query)
results = []
for table in result:
  for record in table.records:
    results.append((record.get_field(), record.get_value()))

print(results)

NAME = argv[0]


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

        # Others
        #"Uptime": timedelta(seconds=time() - psutil.boot_time()),
    }
    print("\n\n SYSTEM INFO ALL\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


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


system_info_all()
system_info_cpu()
system_info_memory()
system_info_networks()
system_info_disk()


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interval", help="echo the interval", type=int)
args = parser.parse_args()

while True:
    time.sleep(args.interval)
    system_info_all()
    system_info_cpu()
    system_info_memory()
    system_info_networks()
    system_info_disk()
    print(args.interval)

