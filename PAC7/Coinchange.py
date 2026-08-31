import time

def coin_change(coins, amount):
    # dp[i] = minimum number of coins required to make amount i
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


# User Input
coins = list(map(int, input("Enter coin denominations separated by spaces: ").split()))
amount = int(input("Enter the target amount: "))

# Check for valid input
if amount < 0 or any(coin <= 0 for coin in coins):
    print("Please enter positive coin values and a non-negative amount.")
else:
    start_time = time.perf_counter()

    result = coin_change(coins, amount)

    end_time = time.perf_counter()

    if result == -1:
        print("The amount cannot be formed using the given coins.")
    else:
        print("Minimum number of coins required:", result)

    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")


# Time Complexity
print("\n--- Time Complexity ---")
print("Best Case    : O(A × C)")
print("Average Case : O(A × C)")
print("Worst Case   : O(A × C)")
print("Space Complexity: O(A)")