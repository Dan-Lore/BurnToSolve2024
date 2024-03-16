# НЕ ПОЛНОЕ РЕШЕНИЕ
def solve(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1]
            else:
                dp[start][end] = 1 + min(dp[start][end - 1], dp[start + 1][end])

    return dp[0][n - 1]

with open('input.txt', 'r') as file:
    s = file.readline().strip()

result = solve(s)

with open('output.txt', 'w') as file:
    file.write(str(result))