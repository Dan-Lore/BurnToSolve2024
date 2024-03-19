mod = 1_000_000_007


def solve(n, h):
    # Сколько макс длина подмассива слева с усл a_i-1 < a_i
    dp_l = [[i] for i in range(n)]
    # Сколько макс длина подмассива справа с усл a_i > a_i+1
    dp_r = [[i] for i in range(n)]

    for i in range(1, n):
        j = n - 1 - i
        for l in range(i):
            r = n - 1 - l
            if h[dp_l[l][-1]] < h[i]:
                if len(dp_l[i]) < len(dp_l[l]) + 1:
                    dp_l[i] = dp_l[l] + [i]
            if h[j] > h[dp_r[r][-1]]:
                if len(dp_r[j]) < len(dp_r[r]) + 1:
                    dp_r[j] = dp_r[r] + [j]
                
    ans = 0
    max_k = 0
    for i in range(n):
        cur = min(len(dp_l[i]), len(dp_r[i]))
        if cur > max_k:
            ans = i
            max_k = cur
    

    tmp = ' '.join(map(lambda val: str(val + 1), dp_l[ans][-max_k:-1] + dp_r[ans][-max_k:][::-1]))
    return str(max_k - 1) + '\n' + tmp


t = 1
result = []
with open('report.in', 'r') as f:
    #t = int(f.readline().strip())
    for i in range(t):
        n = int(f.readline().strip())
        h = list(map(int, f.readline().split()))
        result.append(str(solve(n, h)))


with open('report.out', 'w') as f:
    f.write('\n'.join(result))