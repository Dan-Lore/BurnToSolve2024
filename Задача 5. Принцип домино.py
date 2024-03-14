with open('in.txt', 'r') as f:
    n = int(f.readline().strip())
    dominoes = []

    for i in range(n):
        data = f.readline().split()
        k = int(data[0])
        dominoes.append(list(map(lambda x: int(x) - 1, data[1:])))


max_time = 0
start_domino = -1

for i in range(n):
    i_time = 0
    Q = list()
    if len(dominoes[i]) > 0:
        Q.append(dominoes[i])
    visited = [False] * n
    visited[i] = True

    while len(Q) > 0:
        line = Q.pop(0)
        i_time += 1
        next_line = []

        for v in line:
            visited[v] = True

        for v in line:
            for u in dominoes[v]:
                if not visited[u]:
                    next_line.append(u)

        if len(next_line) > 0:
            Q.append(next_line)
    
    if all(visited) and i_time >= max_time:
        max_time = i_time
        start_domino = i


with open('out.txt', 'w') as f:
    if start_domino == -1:
        f.write("impossible")
    else:
        f.write(str(max_time) + '\n' + str(start_domino + 1))