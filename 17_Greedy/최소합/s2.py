# DP - 메모이제이션

import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 최솟값을 저장
    memo = [[0] * n for _ in range(n)]

    # 행, 열
    for x in range(n):
        for y in range(n):

            # memo의 첫 번째 값(0, 0)에 board의 첫 번째 값(0, 0) 저장
            if x == 0 and y == 0:
                memo[x][y] = board[x][y]

            # 0번째 행(왼쪽만 더한다)
            elif x == 0:
                memo[x][y] = memo[x][y - 1] + board[x][y]
            # 0번째 열(위쪽만 더한다)
            elif y == 0:
                memo[x][y] = memo[x - 1][y] + board[x][y]
            # 왼, 위 중 작은 값 더한다
            else:
                memo[x][y] = min(memo[x][y - 1] + board[x][y], memo[x - 1][y] + board[x][y])

    print(f'#{tc} {memo[n - 1][n - 1]}')
