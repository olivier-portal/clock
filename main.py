from set_time import set_time
from update_time import update_time
import time

def main():
    current_time = set_time()
    while True:
        current_time = update_time(current_time)
        time.sleep(1)

if __name__ == "__main__":
    main()