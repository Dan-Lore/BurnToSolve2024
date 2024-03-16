inf = 1_000_000

with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    matrix = [0] * n
    for i in range(n):
        matrix[i] = [inf * inf] + list(map(int, f.readline().split())) + [inf * inf]

for i in range(1, n):
    for j in range(1, m + 1):
        matrix[i][j] += min(matrix[i-1][j-1:j+2])

with open('output.txt', 'w') as f:
    f.write(str(min(matrix[n-1])))