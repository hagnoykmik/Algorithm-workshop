import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    # m x m 범위를 돌면서 fly의 값을 더한다

    cnt = 0

    for r in range(m-1, 2*m-1):  # m-1부터 m-1+m까지
        for c in range(m-1, 2*m-1):
            if 0 <= r < n and 0 <= c < n:
                cnt += board[r][c]

    print(f'#{tc} {cnt}')