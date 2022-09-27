import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+ 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = 0  # 글자를 넣을 수 있는 칸 개수

    # 가로 탐색
    for r in range(n):
        cnt_w = 0       # 가로로 비워져있는 칸의 개수 카운트
        for c in range(n):
            # 비워져있는 칸이면 카운트를 한다
            if board[r][c] == 1:
                cnt_w += 1
            # 중간에 0을 만났는데 글자수와 같으면 result에 카운트를 한 후 cnt_w를 초기화한다
            else:
                if cnt_w == k:
                    result += 1
                cnt_w = 0
        # 가로 검색을 끝낸 후 글자수와 비워져있는 칸의 개수가 같으면 result에 하나를 추가한다
        if cnt_w == k:
            result += 1

    # 세로 탐색
    for r in range(n):
        cnt_h = 0       # 세로로 비워져있는 칸의 개수 카운트
        for c in range(n):
            if board[c][r] == 1:
                cnt_h += 1
            else:
                if cnt_h == k:
                    result += 1
                cnt_h = 0
        if cnt_h == k:
            result += 1

    print(f'#{tc} {result}')

