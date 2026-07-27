import time

def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Main Program
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

start = time.perf_counter()

insertion_sort(arr, n)

stop = time.perf_counter()

print("\nSorted Array:")
print(*arr)

execution_time = (stop - start) * 1_000_000  # Convert to microseconds

print("\nTime Complexity:")
print("Best Case : O(n)")
print("Average Case : O(n²)")
print("Worst Case : O(n²)")
print(f"Execution Time: {execution_time:.2f} microseconds")