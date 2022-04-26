import multiprocessing
import time

def sleep_around(sec):
    """
    Sleep for given seconds
    """
    print(f"Sleeping for {sec} second(s)")
    time.sleep(sec)
    print("Done sleeping...")

def processes():
    processes = []
    num_process = int(input("How many processes will you create? "))
    for _ in range(num_process):
        p = multiprocessing.Process(target=sleep_around, args=[2,])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.perf_counter()
    processes()

    finish = time.perf_counter()
    print(f"Done executing in {round(finish-start, 2)} seconds")