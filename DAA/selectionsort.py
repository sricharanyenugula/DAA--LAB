import time

def selection_sort(arr, n):
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


# Main Program
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

start = time.perf_counter()

selection_sort(arr, n)

stop = time.perf_counter()

print("\nSorted Array:")
print(*arr)

execution_time = (stop - start) * 1_000_000  # Convert to microseconds

print("\nTime Complexity:")
print("Best Case : O(n²)")
print("Average Case : O(n²)")
print("Worst Case : O(n²)")
print(f"Execution Time: {execution_time:.2f} microseconds")