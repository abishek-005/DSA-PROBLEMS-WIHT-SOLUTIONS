def knapsack(values, weights, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        return knapsack(values, weights, capacity, n-1)
    else:
        return max(values[n-1] + knapsack(values, weights, capacity-weights[n-1], n-1),
                   knapsack(values, weights, capacity, n-1))
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)
print(knapsack(values, weights, capacity, n))
