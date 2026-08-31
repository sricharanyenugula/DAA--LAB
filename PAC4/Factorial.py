# Factorial using Iterative and Recursive Methods
# With Best, Average and Worst Case Time Complexity

def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


# User Input
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Iterative Method
    result1 = factorial_iterative(n)

    print("\n--- Iterative Method ---")
    print("Factorial of", n, "=", result1)

    print("\nTime Complexity:")
    print("Best Case    : O(n)")
    print("Average Case : O(n)")
    print("Worst Case   : O(n)")

    print("\nSpace Complexity:")
    print("O(1)")

    # Recursive Method
    result2 = factorial_recursive(n)

    print("\n--- Recursive Method ---")
    print("Factorial of", n, "=", result2)

    print("\nTime Complexity:")
    print("Best Case    : O(n)")
    print("Average Case : O(n)")
    print("Worst Case   : O(n)")

    print("\nSpace Complexity:")
    print("O(n)")