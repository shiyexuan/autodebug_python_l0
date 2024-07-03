# L0 底线用例：变量使用错误

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity][0]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value = knapsack(weights, values, capacity)
print("背包能装的最大价值为:", max_value)