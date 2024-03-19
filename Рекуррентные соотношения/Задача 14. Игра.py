# НЕ ПОЛНОЕ РЕШЕНИЕ
mod = 1_000_000_007
max_n = 10_000_000 - 2


t = 1
result = []
with open('input.txt', 'r') as f:
    n =  int(f.readline().strip())

dp = [False] * (max_n + 1)
def game(s, pow10):
    if pow10 == 0:
        dp[max_n - s] = True
        return
    for mul in [0, 4, 8]:
        game(s + mul * pow10, pow10 // 10)
game(0, (max_n + 2) // 10)

def find_indexes(n, pow10=1):
    if pow10 > max_n:
        return ''
    ans = []
    for mul in range(4):
        i = pow10 * mul + n
        if not dp[i]:
            ans.append(i)
    return ' '.join(map(str, ans)) + find_indexes(n, pow10*10)    


with open('output.txt', 'w') as f:
    if dp[n]:
        ans = 'The second wins\n'
    else:
        ans = 'The first wins\n'
        ans += find_indexes(n)
    f.write(ans)
        