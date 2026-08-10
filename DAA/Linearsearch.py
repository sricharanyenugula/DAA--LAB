import time

def linear_search(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


# Main Program
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

key = int(input("Enter element to search: "))

start = time.perf_counter()

result = linear_search(arr, n, key)

stop = time.perf_counter()

print("\nSearch Result:")

if result != -1:
    print("Element found at position:", result + 1)
else:
    print("Element not found")

execution_time = (stop - start) * 1_000_000

print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")

print(f"Execution Time: {execution_time:.2f} microseconds")
