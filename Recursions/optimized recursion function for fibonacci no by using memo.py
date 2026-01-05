def fibonacci_memo(n, memo={}):
    # Check if we've already calculated this value
    if n in memo:
        return memo[n]
    # Base cases
    if n <= 1:
        return n
    # Recursive case with memoization
    else:
        result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = result # Store the result
        print("memo values",memo)
        return result
n = 5
for i in range(n + 1):
    print(fibonacci_memo(i), end=" ")
