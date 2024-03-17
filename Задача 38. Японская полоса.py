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

    free_cells = max(1, all_cells - kod_len + 1)
    locked_cells = max(1, free_cells - k)

    ans = factorial(free_cells) // factorial(locked_cells) // factorial(k)
    o.write(str(ans))

i.close()
o.close()