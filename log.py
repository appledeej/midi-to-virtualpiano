import datetime
import os.path
import config

def make_timestamp():
    return datetime.datetime.utcfromtimestamp(datetime.datetime.now().timestamp()).strftime('%Y-%m-%d_%H-%M-%S')

log_file = os.path.join(os.path.dirname(__file__), "logs\\" + make_timestamp() + ".log")

def write_to_log(message):
    with open(log_file, "a") as f:
        f.write(make_timestamp() + "/" + message + "\n")

def success(message):
    print("[*] " + message)
    write_to_log("[SCS]/" + message)

def info(message):
    print("[-] " + message)
    write_to_log("[INF]/" + message)

def warning(message):
    print("[!] " + message)
    write_to_log("[WRN]/" + message)

def error(message):
    print("[!!] " + message)
    write_to_log("[ERR]/" + message)

def debug(message):
    if config.show_debug_msgs:
        print("[D] " + message)
    write_to_log("[DBG]/" + message)