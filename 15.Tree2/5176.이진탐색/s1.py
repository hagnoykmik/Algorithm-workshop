# 실패
import sys
sys.stdin = open('sample_input.txt')


# 규칙 (왼쪽 < 부모 < 오른쪽)
def tree(v):
    global last
    last += 1
    nods[last] = v

    c = last
    p = c // 2

    while p:
        if c % 2 == 0 and nods[p] < nods[c]:
            nods[p], nods[c] = nods[c], nods[p]
        elif c % 2 and nods[p] > nods[c]:
            nods[p], nods[c] = nods[c], nods[p]

        c = p
        p = c // 2

t = int(input())
for tc in range(1, t+1):

    n = int(input())
    nods = [0] * (n + 1)
    last = 0

    for num in range(1, n + 1):
        tree(num)

    print(nods)
