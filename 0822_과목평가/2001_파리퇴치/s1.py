import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    # m x m 범위를 돌면서 fly의 값을 더한다
    cnt = 0  # 행이 바뀔 때 초기화
    max_c = 0

    for r in range(n):
        for c in range(n):
            for i in range(n-m+1):
                for j in range(n-m+1):
                    cnt += board[i][j]

    # 최대값을 구한다
    if max_c < cnt:
        max_c = cnt

    print(f'#{tc} {max_c}')