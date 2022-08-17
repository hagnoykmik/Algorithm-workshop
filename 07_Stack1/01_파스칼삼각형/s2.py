import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    number = int(input())
    arr = [[] * number for _ in range(1, number + 1)]    # 리스트 크기 자동조절
                                                         # 범위 1부터로

# nCr에서 아이디어
    for n in range(1, number + 1):
        for r in range(n):
            if r == 0 or n == r:                         # r이 0이거나 n과 같으면 1
                arr[n][r].append(1)
            else:                                        # nCr = n-1Cr + n-1Cr-1
                arr[n][r].append(arr[n-1][r] + arr[n-1][r-1])
    print(f'#{tc}')

    for i in range(1, number + 1):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()