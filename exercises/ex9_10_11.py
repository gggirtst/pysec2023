import os
import threading
import signal
import sys


exit_flag = False

def signal_handler(sig, frame):
    global exit_flag
    exit_flag = True
    print("CTRL+C detected. Exiting gracefully...")

def long_running_task():
    while not exit_flag:
        pass

def print_directory_contents(path, depth=0):
    items = os.listdir(path)
    threads = []

    def process_item(item):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            print("  " * depth + f"Directory: {item}")
            t = threading.Thread(target=print_directory_contents, args=(item_path, depth + 1))
            threads.append(t)
            t.start()
        else:
            size = os.path.getsize(item_path)
            ctime = os.path.getctime(item_path)
            print("  " * depth + f"File: {item}, Size: {size} bytes, Created: {ctime}")

    for item in items:
        process_item(item)

    long_task_thread = threading.Thread(target=long_running_task)
    long_task_thread.start()

    for thread in threads:
        thread.join()


    global exit_flag
    exit_flag = True
    long_task_thread.join()

#root_directory = '/users/girtstutans/pysec2023'
root_directory = '/users/girtstutans/pysec2023/exercises'

signal.signal(signal.SIGINT, signal_handler)

try:
    print_directory_contents(root_directory)
except KeyboardInterrupt:
    pass
