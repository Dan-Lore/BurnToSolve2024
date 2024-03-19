mod = 1_000_000_007


with open('input.txt', 'r') as f:
    n, m, s = map(int, f.readline().split())
    h = list(map(int, f.readline().split()))
    b = list(map(int, f.readline().split()))

h_set = set()
for i in range(n):
    t_set = set()
    for val in h_set:
        t_set.add(val + h[i])
    h_set.update(t_set)
    h_set.add(h[i])

b_set = set()
for i in range(m):
    t_set = set()
    for val in b_set:
        t_set.add(val + b[i])
    b_set.update(t_set)
    b_set.add(b[i])
b_set.add(0)

result = 'No'
for val in h_set:
    change = val - s
    if change in b_set:
        result = 'Yes'
        break

with open('output.txt', 'w') as f:
    f.write(str(result))