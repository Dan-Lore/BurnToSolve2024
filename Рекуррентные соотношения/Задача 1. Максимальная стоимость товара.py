mod = 1_000_000_007


with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    a = list(map(int, f.readline().split()))
    b = list(map(int, f.readline().split()))


a_set = set()
for i in range(n):
    t_set = set()
    for val in a_set:
        t_set.add(val + a[i])
    a_set.update(t_set)
    a_set.add(a[i])

b_set = set()
for i in range(m):
    t_set = set()
    for val in b_set:
        t_set.add(val + b[i])
    b_set.update(t_set)
    b_set.add(b[i])
b_set.add(0)

price = [False] * (max(a_set) + 1)
for plata in a_set:
    for sdacha in b_set:
        if plata - sdacha >= 0:
            price[plata-sdacha] = True

result = 'YES'
for s in range(max(a_set), 0, -1):
    if price[s] == False:
        result = 'NO'
        break
    
if result == 'NO':
    result += '\n' + str(s)


with open('output.txt', 'w') as f:
    f.write(str(result))