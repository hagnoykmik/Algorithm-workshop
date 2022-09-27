'''
9
111456
123123
233677
112233
333333
123456
667767
054060
101123
'''

t = int(input())
for tc in range(1, t + 1):
    nums = input()
    counting_sort = [0] * 12
    answer = 'False'

    # 만약에 맨앞자리가 0이라면 일단 카운팅 정렬에 담는다
    for i in range(6):
        if nums[i] == '0':
            counting_sort[i] += 1
        else:
            break

    nums = int(nums)
    # 카드의 숫자를 인덱스로 카운팅 정렬에 담는다
    while nums > 0:
        counting_sort[nums % 10] += 1
        nums //= 10

    # baby gin 검사
    i = 0
    tri = 0
    run = 0
    while i < 10:  # i가 반복될 수도 있음( #123123)
        # triplet
        if counting_sort[i] >= 3:
            tri += 1
            counting_sort[i] -= 3
            continue
        # run
        if counting_sort[i] >= 1 and counting_sort[i + 1] >= 1 and counting_sort[i + 2] >= 1:
            run += 1
            counting_sort[i] -= 1
            counting_sort[i + 1] -= 1
            counting_sort[i + 2] -= 1
            continue
        i += 1

    if run + tri == 2:
        answer = 'True'

    print(answer)
