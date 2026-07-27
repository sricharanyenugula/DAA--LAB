import time

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


# Main Program
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

start = time.perf_counter()

merge_sort(arr, 0, n - 1)

stop = time.perf_counter()

print("\nSorted Array:")
print(*arr)

execution_time = (stop - start) * 1_000_000  # Convert to microseconds

print("\nTime Complexity:")
print("Best Case : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case : O(n log n)")
print(f"Execution Time: {execution_time:.2f} microseconds")