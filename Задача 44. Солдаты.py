mod = 1_000_000_007


max_n = 10_000_000
dp = [1] * (max_n + 1)
for i in range(4, max_n+1):
    dp[i] = dp[i // 2] + dp[(i + 1) // 2]


t = 1
result = []
with open('input.txt', 'r') as f:
    #t = int(f.readline().strip())
    for i in range(t):
        n = int(f.readline().strip())
        result.append(str(dp[n]))


with open('output.txt', 'w') as f:
    f.write('\n'.join(result))