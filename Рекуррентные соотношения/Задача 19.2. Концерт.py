mod = 1_000_000_007
max_n = 10_000_001


def solve(n, m, d, l):
    next_closest_smaller = [n] * n
    for i in range(n - 1, 0, -1):
        k = i + 1
        while k < n and l[i] <= l[k]:
            k = next_closest_smaller[k]
        next_closest_smaller[i] = k
    # Не точная постановка задачи.
    # Можно ли на одну касету записать несколько песен?
    # Входные: 3 1 4 \n 1 2 1
    # Ответ 3 или 1 ?
    

t = 1
result = []
with open('concert.in', 'r') as f:
    #t = int(f.readline().strip())
    for i in range(t):
        n, m, d = map(int, f.readline().split())
        l = list(map(int, f.readline().split()))
        result.append(str(solve(n, m, d, l)))


with open('concert.out', 'w') as f:
    f.writelines(result)