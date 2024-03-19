# У задачи ужасное условие и кривой пример. Не решена.
mod = 1_000_000_007
max_n = 10_000_001


def solve(n, a, b):
    dp = [0] * n
    for i in range(1, n):
        dp[i] = dp[i - 1] + a[0] * b[i]
    return dp[n - 1]


n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())


print(solve(n, a, b))