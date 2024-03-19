def check_1in2(box1, box2):
    for i in range(len(box1)):
        if box1[i] > box2[i]:
            return False
    return True

def solve(m, boxes):
    dp = [1] * m

    for i in range(1, m):
        for j in range(i):
            if check_1in2(boxes[j], boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    return max_length


with open('input.txt', 'r') as file:
    params = file.readline()
    lines = file.readlines()

n, m = map(int, params.split())
boxes = [0] * m
for i in range(m):
    boxes[i] = list(map(int, lines[i].split()))
    boxes[i].sort()
boxes.sort()

result = solve(m, boxes)
with open('output.txt', 'w') as file:
    file.write(str(result))