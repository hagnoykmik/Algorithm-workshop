# 완전 탐색(순열)
def f(i, k):
    global answer
    # 자리를 다 채웠으면 Baby- gin 검사
    if i == k:
        run = 0
        tri = 0

        # 앞부분 검사
        if p[0] == p[1] and p[1] == p[2]:
            tri += 1
        if p[0] + 1 == p[1] and p[1] + 1 == p[2]:
            run += 1

        # 뒷부분 검사
        if p[3] == p[4] and p[4] == p[5]:
            tri += 1
        if p[3] + 1 == p[4] and p[4] + 1 == p[5]:
            run += 1

        # Baby gin 검사
        if run + tri == 2:
            answer = 'True'

    # 경우의 수 보기(자리 채우기)
    else:
        for j in range(k):  # 모든 원소에 대해
            if used[j] == 0:  # 사용하지 않았다면
                p[i] = arr[j]  # p값을 채운다
                used[j] = 1  # 사용함으로 바꿈
                f(i + 1, k)
                used[j] = 0  # 다른 자리에서 사용하기 위해 초기화


t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input()))
    n = len(arr)
    used = [0] * n  # 사용여부 확인
    p = [0] * n
    answer = 'False'

    f(0, n)

    print(f'#{tc} {answer}')


