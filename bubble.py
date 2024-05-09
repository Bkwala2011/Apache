import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    random_numbers = [random.randint(1.0, 10000.0) for _ in range(10000)]

    start_time = time.time()

    bubble_sort(random_numbers)

    end_time = time.time()

    time_taken = end_time - start_time

    print(time_taken)
