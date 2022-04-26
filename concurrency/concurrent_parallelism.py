import concurrent.futures
import time

def sleep_around(sec):
    """
    Sleep for given seconds
    """
    print(f"Sleeping for {sec} second(s)")
    time.sleep(sec)
    return f"Done sleeping..."

def get_data():
    num_process = int(input("How many processes will you create? "))
    sleep_time = []
    print("Enter the sleeping time for each process\n")
    for i in range(num_process):
        sleep_time.append(int(input(f"Process {i+1}: ")))
    return sleep_time

def processes(time_list):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(sleep_around, sec) for sec in time_list]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

if __name__ == "__main__":
    sleep_time = get_data()
    start = time.perf_counter()
    processes(sleep_time)

    finish = time.perf_counter()
    print(f"Done executing in {round(finish-start, 2)} seconds")