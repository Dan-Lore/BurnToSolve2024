# НЕ ПОЛНОЕ РЕШЕНИЕ
with open('input.in', 'r') as f:
    n = int(f.readline().strip())
    prod = [0] * n
    dih = []
    for i in range(n):
        prod[i] = list(map(int, f.readline().split()))
        dih.extend(prod[i])
    dih.sort()


def dfs(i, visited, machines, need_prod):
        if visited[i]:
            return False
        visited[i] = True
        for j in reversed(range(n)):
            if prod[i][j] < need_prod:
                continue
            if machines[j] is None or dfs(machines[j], visited, machines, need_prod):
                machines[j] = i
                return True
        return False


best_dist = [1] * n
l, r = 0, len(dih)

while l + 1 < r:
    m = (l + r) // 2
    need_prod = dih[m]

    # Двудольный граф
    visited = [False] * n # посещена ли левая доля
    machines = [None] * n # занята ли правая доля
    workers = [None] * n

    # Жадно
    for i in range(n):
        for j in range(n):
            if machines[j] is None and prod[i][j] >= need_prod:
                workers[i] = j
                machines[j] = i
                break

    # Алгоритм пополняющего пути - Алгоритм Куна
    for i in range(n):
        if workers[i] is not None:
            continue
        if (dfs(i, visited, machines, need_prod)):
            visited = [False] * n
    
    if all(item is not None for item in machines):
        l = m
        for i in range(n):
            best_dist[machines[i]] = i + 1
    else:
        r = m


with open('output.out', 'w') as f:
    line1 = str(dih[l]) + '\n'
    line2 = ' '.join(map(str, best_dist))
    f.write(line1 + line2)