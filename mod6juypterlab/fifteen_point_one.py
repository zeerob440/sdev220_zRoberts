import random
import multiprocessing
import time
import os
#15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
# could not get this program to run in Juypter Lab, but was able to run it in Pycharm and VS Code as .py files
def random_interval_0_1_sec_current_time_printing_device_function():
        anchoring_time = time.ctime()
        range_random: float = random.uniform(0, 1)
        time.sleep(range_random)
        print(anchoring_time)
        print(f'PID: {os.getpid()}, Time: {anchoring_time}')

if __name__ == "__main__":
    for i in range(3):
        processed = multiprocessing.Process(target= random_interval_0_1_sec_current_time_printing_device_function)
        processed.start()
        processed.join()
