mod = 1_000_000_007


def solve(n, k):
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = (2 * dp[i-1] - dp[max(0, i-1-k)]) % mod
    return dp[n]


t = 1
result = []
with open('input.txt', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        n, k = map(int, f.readline().split())
        result.append(str(solve(n, k)))


with open('output.txt', 'w') as f:
    f.write('\n'.join(result))