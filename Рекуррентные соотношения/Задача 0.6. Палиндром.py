def solve(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1]
            else:
                dp[start][end] = 1 + min(dp[start][end - 1], dp[start + 1][end])

    palindromic_string = []
    i, j = 0, n - 1
    while i < j:
        if s[i] == s[j]:
            palindromic_string.append(s[i])
            i += 1
            j -= 1
        elif dp[i][j] == dp[i + 1][j] + 1:
            i += 1
        elif dp[i][j] == dp[i][j - 1] + 1:
            j -= 1

    result = ''.join(palindromic_string)
    if i == j:
        result += s[i] + ''.join(reversed(result))
    else:
        result += ''.join(reversed(result))

    return result


with open('input.txt', 'r') as file:
    s = file.readline().strip()

result = solve(s)

with open('output.txt', 'w') as file:
    file.write(str(len(result)) + '\n' + result)