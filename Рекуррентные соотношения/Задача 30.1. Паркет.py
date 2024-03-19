# НЕ ПОЛНОЕ РЕШЕНИЕ, 
# проблемы с модулем в исходнике задачи
def solve(n):
    mod = 1_000_000_007
    return (int(1 + 4 * pow(6, n, mod)) // 5) % mod


with open('in.txt', 'r') as f:
    n = int(f.read().strip())

result = solve(n // 2) if n % 2 == 0 else 0

with open('out.txt', 'w') as f:
    f.write(str(result))