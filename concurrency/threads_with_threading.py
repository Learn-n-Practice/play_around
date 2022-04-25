import threading
from time import sleep, perf_counter

start = perf_counter()

def sleep_around(sec):
    """
    Sleep for given seconds
    """
    print(f"Sleeping for {sec} second(s)")
    sleep(sec)
    print("Done sleeping...")

sec = int(input("Seconds to make function sleep: "))
threads = []

# Create and start 10 threads
for _ in range(10):
    t = threading.Thread(target=sleep_around, args=[sec])
    t.start()
    threads.append(t)

# Join threads to finish executing before before executing remaining code
for  t in threads:
    t.join()

finish = perf_counter()
print(f"Done execunting in {round(finish-start, 2)} seconds")