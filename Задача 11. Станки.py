with open('input.in', 'r') as f:
    n = int(f.readline().strip())
    g = [0] * n
    prod = [0] * n
    dih = []
    for i in range(n):
        prod[i] = list(map(int, f.readline().split()))
        g[i] = set()
        for j in range(n):
            g[i].add(j)
        dih.extend(prod[i])
    dih.sort()


def dfs(i, visited, machines, need_prod):
        if visited[i]:
            return False
        visited[i] = True
        for j in g[i]:
            if prod[i][j] < need_prod:
                continue
            if machines[j] is None or dfs(machines[j], visited, machines, need_prod):
                machines[j] = i
                return True
        return False


l, r = 0, len(dih)

while l + 1 < r:
    m = (l + r) // 2
    need_prod = dih[m]

    # Двудольный граф
    visited = [False] * n # посещена ли левая доля
    machines = [None] * n # занята ли правая доля

    nig = [False] * n
    # Жадно
    for i in range(n):
        for j in g[i]:
            if machines[j] is None and prod[i][j] >= need_prod:
                nig[i] = True
                machines[j] = i
                break

    # Алгоритм увеличивающегося пути
    for i in range(n):
        if nig[i]:
            continue
        if (dfs(i, visited, machines, need_prod)):
            visited = [False] * n
    
    if all(item is not None for item in machines):
        l = m
        for i in range(n):
            g[i] = {j for j in g[i] if prod[i][j] >= need_prod}
    else:
        r = m


machines = [None] * n
need_prod = dih[l]
best_dist = [0] * n
for i in range(n):
    for j in g[i]:
        if machines[j] is None and prod[i][j] >= need_prod:
            best_dist[i] = j + 1
            machines[j] = i
            break


with open('output.out', 'w') as f:
    line1 = str(need_prod) + '\n'
    line2 = ' '.join(map(str, best_dist))
    f.write(line1 + line2)