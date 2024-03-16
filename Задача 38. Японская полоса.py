# НЕ ПОЛНОЕ РЕШЕНИЕ
from math import factorial

i = open("in.txt", "r")
o = open("out.txt", "w")

all_cells = int(i.readline())
k = int(i.readline())
_ = i.readline()

if k == 0:
    o.write('1')
else:
    kod_len = 0
    for _ in range(k):
        a = int(i.readline())
        kod_len += a

    free_cells = all_cells - kod_len + 1

    ans = factorial(free_cells) // factorial(free_cells - k) // factorial(k)
    o.write(str(ans))

i.close()
o.close()