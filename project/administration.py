from datetime import datetime, timedelta
from sys import argv
from time import time

import psutil

NAME = argv[0]


def system_info():
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
        "Memory available": f"{psutil.virtual_memory().available / (1024**3):,.3f} GiB",
        "Memory swap": f"{psutil.swap_memory()}",

        # Networks
        "Net counters": f"{psutil.net_io_counters()}",
        "Net addresses": f"{psutil.net_if_addrs()}",
        "Net stats": f"{psutil.net_if_stats()}",

        # Disk
        "Disk partition": f"{psutil.disk_partitions()}",
        "Disk in use": f"{psutil.disk_usage('/').percent}%",
        "Disk free": f"{psutil.disk_usage('/').free / (1024**3):,.3f} GiB%",
        "Disk counters": f"{psutil.net_io_counters()}",

        # Others
        "Uptime": timedelta(seconds=time() - psutil.boot_time()),
    }
    print("\n\n SYSTEM INFO\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


system_info()
