mod = 1_000_000_007


def solve(n, k):
    pass


t = 1
result = []
with open('input.txt', 'r') as f:
    #t = int(f.readline().strip())
    for i in range(t):
        n, k = map(int, f.readline().split())
        result.append(str(solve(n, k)))


with open('output.txt', 'w') as f:
    f.write('\n'.join(result))