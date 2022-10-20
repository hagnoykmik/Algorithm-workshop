'''
0번째 행 - W
앞부분 - W > B : W
         W < B : B
뒷부분 - B < R : R
         B > R : B
마지막 행 - R
'''

# import sys

# sys.stdin = open('sample_input.txt')


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    color_count = {}
    blue = 0
    change = 0

    # 첫째 줄은 White
    # for color in flag[0]:
    #     if color != 'W':
    #         change += 1
    #
    # print(change)

    # 중간에 B가 하나 들어가야돼
    for i in range(1, n - 1):
        color_count['W'] += flag[i].count('W')
        color_count['B'] += flag[i].count('B')
        color_count['R'] += flag[i].count('R')
        print(color_count)
        print(max(color_count))

        if color_count['B'] < flag[i].count:
            blue = i

    #
    #
    # # 마지막 줄은 RED
    # for color in flag[-1]:
    #     if color != 'R':
    #         change += 1
    #
    # print(change)
