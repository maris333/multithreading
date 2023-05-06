import random
import time
import threading
from multiprocessing import Process


# Bubble sort implementation
def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


# Multithreading implementation
def sort_with_threads(arr, num_threads):
    threads = []
    chunks = [arr[i::num_threads] for i in range(num_threads)]

    # Create threads and assign a chunk of the array to each thread
    for i in range(num_threads):
        thread = threading.Thread(target=bubble_sort, args=(chunks[i],))
        threads.append(thread)

    start_time = time.time()

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


# Multiprocessing implementation
def sort_with_processes(arr, num_processes):
    chunks = [arr[i::num_processes] for i in range(num_processes)]
    processes = []

    # Create processes and assign a chunk of the array to each process
    for i in range(num_processes):
        process = Process(target=bubble_sort, args=(chunks[i],))
        processes.append(process)

    start_time = time.time()

    # Start the processes
    for process in processes:
        process.start()

    # Wait for processes to finish and combine sorted chunks
    for process in processes:
        process.join()

    end_time = time.time()
    return end_time - start_time


def main():
    # Generate 10 100-element arrays to sort
    arrs = []
    for i in range(10):
        arr = [random.randint(0, 1000) for _ in range(100)]
        arrs.append(arr)

    # Sort with multithreading and measure time
    num_threads = 4
    thread_times = []
    for arr in arrs:
        thread_time = sort_with_threads(arr, num_threads)
        thread_times.append(thread_time)

    # Sort with multiprocessing and measure time
    num_processes = 2
    process_times = []
    for arr in arrs:
        process_time = sort_with_processes(arr, num_processes)
        process_times.append(process_time)

    # Print execution times for each approach
    print("Multithreading times:", thread_times)
    print("Multiprocessing times:", process_times)


if __name__ == "__main__":
    main()
