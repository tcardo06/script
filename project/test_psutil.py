from datetime import datetime, timedelta
from sys import argv
from time import time

import psutil

NAME = argv[0]


def system_info():
    info = {
        "Uptime": timedelta(seconds=time() - psutil.boot_time()),
        "CPU in use": f"{psutil.cpu_percent(interval=.1)}%",
        "Time on CPU": timedelta(seconds=psutil.cpu_times().system + psutil.cpu_times().user),
        "Memory in use": f"{psutil.virtual_memory().percent}%",
        "Memory available": f"{psutil.virtual_memory().available / (1024 ** 3):,.3f} GiB",
        "Disk in use": f"{psutil.disk_usage('/').percent}%",
        "Disk free": f"{psutil.disk_usage('/').free / (1024 ** 3):,.3f} GiB%",

    }
    print("\n\n SYSTEM INFO\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


def process_info():
    pass


system_info()
process_info()