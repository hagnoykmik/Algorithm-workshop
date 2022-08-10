import sys

sys.stdin = open("C:\Users\82107\Desktop\보충\0810\sum\input.txt")

t = 10

for tc in range(1, t + 1):
    n = input()
    arr = [list(map(int, input().split()))]

    maxS = 0  # 합의 최대값을 담을 변수
    rs = 0  # 행의 합

    for i in range(100):
        for j in range(100):
            rs += arr[i, 100]

            if maxS < rs:
                maxS = rs

    cs = 0  # 열의 합

    for i in range(100):
        for j in range(100):
            cs += arr[j][i]

            if maxS < cs:
                maxS = cs

    s1 = 0  # 우측으로 내려가는 대각선
    for i in range(100):
        s1 += arr[i][i]

        if maxS < s1:
            maxS = s1

    s2 = 0
    for i in range(100):
        s2 += arr[i][99 - i]

        if maxS < s2:
            maxS = s2

print(f"#{tc} {maxS}")
