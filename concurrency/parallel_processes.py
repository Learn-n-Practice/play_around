import multiprocessing
import time

def sleep_around(sec):
    """
    Sleep for given seconds
    """
    print(f"Sleeping for {sec} second(s)")
    time.sleep(sec)
    print("Done sleeping...")


if __name__ == "__main__":
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=sleep_around, args=[10])
    p2 = multiprocessing.Process(target=sleep_around, args=[10])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f"Done executing in {round(finish-start, 2)} seconds")