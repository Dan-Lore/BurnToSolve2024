mod = 1_000_000_007


def solve(n, k):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = k
    for i in range(2, n + 1):
        dp[i] = k * (dp[i-1] + dp[i-2])
    return sum(dp)


t = 1
with open('input.txt', 'r') as f:
    #t = int(f.readline().strip())
    k, n = map(int, f.readline().split())


with open('output.txt', 'w') as f:
    for i in range(t):
        result = solve(n, k)
        f.write(str(result))