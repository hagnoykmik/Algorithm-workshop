n = int(input())
arr = [[0] * n for _ in range(n)]
a = n**2 + 1

for i in range(n):
    for j in range(n):
        a += 1
        arr[n-i-1][j] += a

for i in range(n):
    for j in range(n):
        print(arr[j][i], end=' ')
    print()