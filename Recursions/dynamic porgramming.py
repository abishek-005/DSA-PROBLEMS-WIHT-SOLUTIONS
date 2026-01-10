def fibonacci_dp(n):
    # Base cases
    if n <= 1:
        return n

    # DP array
    dp = [0] * (n + 1)
    dp[1] = 1

    # Fill DP array
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# -------- Main Program --------
n = int(input("Enter a number: "))

result = fibonacci_dp(n)
print(f"Fibonacci number at position {n} is: {result}")
