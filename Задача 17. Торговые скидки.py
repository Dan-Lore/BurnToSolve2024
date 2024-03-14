# НЕ РАБОЧИЙ КОД
with open('discount.in', 'r') as f:
    buck_len = int(f.readline().strip())

    buck_best_price = 0
    buck_best = dict()
    buck_need_to_buy = dict()
    shop_price = dict()

    for i in range(buck_len):
        code, need, price_per_one = list(map(int, f.readline().split()))
        buck_need_to_buy[code] = need
        shop_price[code] = price_per_one
        buck_best[code] = 0
        buck_best_price += need * price_per_one

    s = int(f.readline().strip())
    sale = [0] * s
    for i in range(s):
        n, *items, cost = map(int, f.readline().split())
        sale[i] = [n, items, cost] 


Q = list()
Q.append([buck_best.copy(), 0, 0, buck_best_price])

used = dict()

while len(Q) > 0:
    buck, dissId, diss, add = Q.pop(0)

    flag = False

    if diss + add < buck_best_price:
        buck_best = buck.copy()
        buck_best_price = diss + add
    elif diss + add > buck_best_price:
        flag = all([buck[key] <=  buck_best[key] for key in buck.keys()])

    if flag:
        continue

    for i in range(dissId, s):
        buck_temp = buck.copy()
        diss_temp = diss
        add_temp = add

        n, items, cost = sale[i]
        for j in range(0, n):
            code, itemCount = items[2 * j], items[2 * j + 1]
            buck_temp[code] += itemCount
            add_temp -= shop_price[code] * itemCount
        diss_temp += cost

        if any([buck_temp[key] > buck_need_to_buy[key] for key in buck.keys()]):
            continue

        Q.append([buck_temp, i, diss_temp, add_temp])


with open('discount.out', 'w') as f:
    f.write(str(buck_best_price))