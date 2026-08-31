import time

def matrix_chain_order(dimensions):
    n = len(dimensions) - 1

    # dp[i][j] stores minimum multiplication cost
    dp = [[0] * n for _ in range(n)]

    # chain_length is the length of matrix chain
    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


# User Input
print("Matrix Chain Multiplication using Dynamic Programming")

n = int(input("Enter number of matrices: "))

dimensions = []

print("Enter dimensions:")
print(f"Enter {n + 1} values (Example: 10 20 30 40)")

dimensions = list(map(int, input().split()))

if len(dimensions) != n + 1:
    print(f"Error: Please enter exactly {n + 1} dimensions.")
else:
    start_time = time.perf_counter()

    minimum_cost = matrix_chain_order(dimensions)

    end_time = time.perf_counter()

    print("\nMinimum number of multiplications:", minimum_cost)
    print("Execution time:", end_time - start_time, "seconds")