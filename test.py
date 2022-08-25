n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1


for i in range(m-1, -1, -1):              # 1,0

    if m % 2 == 0:                        # m이 짝수일 때
        if i % 2 == 0:                    # 짝수 열의 행이 내림
            for j in range(n-1, -1, -1):
                arr[j][i] = a
                a += 1
        else:
            for j in range(n):            # 홀수 열의 행이 오름
                arr[j][i] = a
                a += 1
    else:                                 # m이 홀수일 때
        if i % 2:                         # 홀수 열의 행이 내림
            for j in range(n - 1, -1, -1):
                arr[j][i] = a
                a += 1
        else:                             # 짝수 열의 행이 오름
            for j in range(n):
                arr[j][i] = a
                a += 1

for k in arr:
    print(*k)