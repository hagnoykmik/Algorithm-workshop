import sys
sys.stdin = open('sample_input.txt')


def f(i, k):
    global minV
    if i == k:  # 인덱스 i == 원소의 개수
        s = 0  # 모든 m행에서 p[m]열을 골랐을 때의 합
        for m in range(k):
            s += arr[m][p[m]]
        if minV > s:
            minV = s
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]  # 자리바꾸기
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]  # 다시 원상복귀


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]       # p[i] = i행에서 선택한 열 번호
    minV = n * 10

    f(0, n)

    print(f'#{tc} {minV}')