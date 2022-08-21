import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_s = 0  # 합의 최대값

    # n x n 배열 탐색
    for i in range(n - m + 1):
        for j in range(n - m + 1):

            sum_f = 0  # 파리의 합

            # m x m 배열 탐색
            for k in range(i, i + m):
                for l in range(j, j + m):
                    sum_f += board[k][l]

            # 최대값을 구한다
            if max_s < sum_f:
                max_s = sum_f

    print(f'#{tc} {max_s}')