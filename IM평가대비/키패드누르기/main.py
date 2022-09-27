numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
answer = ''
# result = "LRLLLRLLRRL"
phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

# 델타 검색
def search(x, y, cnt):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 4 and phone[nx][ny] == num:
            cnt += 1
            x, y = nx, ny
            return cnt



# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작할 때의 손 위치
left = 4, 0
right = 4, 2

cnt_l = 0
cnt_r = 0

for num in numbers:
    # 숫자가 1, 4, 7일 때
    if num % 3 == 1:
        answer += 'L'
        for left_r in range(4):
            if phone[left_r][0] == num:
                left = left_r, 0
                break
    # 숫자가 3, 6, 9일 때
    elif num % 3 == 0:
        answer += 'R'
        for right_r in range(4):
            if phone[right_r][2] == num:
                right = right_r, 2
                break
    # 숫자가 2, 5, 8, 0일 때
    else:
        search(left_r, 0, cnt_l)
        cnt_l = cnt
        search(right_r, 2, cnt_r)
        cnt_r = cnt
        pass



