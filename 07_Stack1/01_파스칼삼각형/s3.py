import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(1, n + 1)]

    for i in range(1, n):
        for j in range(1, i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')
    for k in range(n):
        for l in range(n):
            if arr[k][l] != 0:
                print(arr[k][l], end=' ')
        print()