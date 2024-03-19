mod = 1_000_000_007
max_n = 10_000_001


def solve(n, m:list[int], sum_m):
    m = list(filter(lambda x: x != 0, m))
    m.sort(reverse=sum_m > 0)
    for i in range(n):
        if sum_m == 0 or sum_m * m[i] > 0:
            return i
        sum_m -= m[i]
    return n


t = 1
result = []
with open('input.txt', 'r') as f:
    #t = int(f.readline().strip())
    for i in range(t):
        n = int(f.readline().strip())
        m = [0] * n
        sum_m = 0
        for i in range(n):
            a, b = map(int, f.readline().split())
            m[i] = a - b
            sum_m += m[i]
        result.append(str(solve(n, m, sum_m)))


with open('output.txt', 'w') as f:
    f.writelines(result)