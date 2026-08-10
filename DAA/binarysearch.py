import time


def binary_search(arr, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main Program
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

# Sort the array
arr.sort()

print("\nSorted Array:")
print(*arr)

key = int(input("Enter element to search: "))

start = time.perf_counter()

result = binary_search(arr, n, key)

stop = time.perf_counter()

print("\nSearch Result:")

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")

execution_time = (stop - start) * 1_000_000

print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(log n)")
print("Worst Case   : O(log n)")

print("Space Complexity: O(1)")

print(f"Execution Time: {execution_time:.2f} microseconds")
