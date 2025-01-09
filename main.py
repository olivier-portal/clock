from functions.set_time import set_time
from functions.update_time import update_time
from functions.set_alarm import set_alarm
import time


current_time = set_time()
set_alarm()
while True:
    current_time = update_time(current_time)
    time.sleep(1)
