from functions.set_time import set_time
from functions.update_time import update_time
import time


current_time = set_time()
while True:
    current_time = update_time(current_time)
    time.sleep(1)
