n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1


for i in range(n-1, -1, -1):  # 1,0
    # 마지막 행부터 내림차순
    if i % 2:
        for j in range(m-1, -1, -1):
            arr[i][j] = a
            a += 1
    # 오름차순 반복
    else:
        for j in range(m):
            arr[i][j] = a
            a += 1

for k in arr:
    print(*k)