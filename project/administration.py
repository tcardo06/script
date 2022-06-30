from datetime import datetime, timedelta
from sys import argv
from time import time
import argparse
import logging

import psutil


logging.basicConfig(level=logging.INFO)
logging.info('This will be logged')

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
        "Uptime": timedelta(seconds=time() - psutil.boot_time()),
    }
    #print("\n\n SYSTEM INFO ALL\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))

def system_info_cpu():
    info = {
        # CPU
        "Number of cores in system": f"{psutil.cpu_count(logical=False)}",
        "CPU Statistics": f"{psutil.cpu_stats()}",
        "CPU frequency": f"{psutil.cpu_freq()}",
        "Average system load ": f"{psutil.getloadavg()}",
        "CPU in use": f"{psutil.cpu_percent(interval=.1)}%",
        "Time on CPU": timedelta(seconds=psutil.cpu_times().system + psutil.cpu_times().user),

    }
    print("\n\n SYSTEM INFO CPU\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))

def system_info_memory():
    info = {
        # Memory
        "Memory in use": f"{psutil.virtual_memory().percent}%",
        "Memory available": f"{psutil.virtual_memory().available / (1024 ** 3):,.3f} GiB",
        "Memory swap": f"{psutil.swap_memory()}",

    }
    #print("\n\n SYSTEM INFO MEMORY\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))

def system_info_networks():
    info = {
        # Networks
        "Net counters": f"{psutil.net_io_counters()}",
        "Net addresses": f"{psutil.net_if_addrs()}",
        "Net stats": f"{psutil.net_if_stats()}",

    }
    #print("\n\n SYSTEM INFO NETWORKS\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))

def system_info_disk():
    info = {
        # Disk
        "Disk partition": f"{psutil.disk_partitions()}",
        "Disk in use": f"{psutil.disk_usage('/').percent}%",
        "Disk free": f"{psutil.disk_usage('/').free / (1024 ** 3):,.3f} GiB%",
        "Disk counters": f"{psutil.net_io_counters()}",

    }
    #print("\n\n SYSTEM INFO DISK\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))

def system_info_others():
    info = {
        # Others
        "Uptime": timedelta(seconds=time() - psutil.boot_time()),

    }
    #print("\n\n SYSTEM INFO OTHERS\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


FUNCTION_MAP = {
    'all': system_info_all(),
    'cpu': system_info_cpu(),
    'memory': system_info_memory(),
    'networks': system_info_networks(),
    'disk': system_info_disk(),
    'others': system_info_others()
    }

system_info_all = argparse.ArgumentParser()
system_info_all.add_argument("all", help="string to test", type=str, choices=FUNCTION_MAP.keys())
system_info_all = system_info_all.parse_args()
func = FUNCTION_MAP[system_info_all().all]
func()

print("The string is : " + system_info_all().all)

system_info_cpu = argparse.ArgumentParser()
system_info_cpu.add_argument("cpu", help="string to test", type=str, choices=FUNCTION_MAP.keys())
system_info_cpu = system_info_cpu.parse_args()
func = FUNCTION_MAP[system_info_cpu().cpu]
func()

print("The string is : " + system_info_cpu().cpu)


NAME = argv[0]


system_info_all()
system_info_cpu()
system_info_memory()
system_info_networks()
system_info_disk()
system_info_others()
