import sys
sys.stdin = open('input.txt')

t = 10

for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))

    cnt = 0 #조망권이 확보된 세대의 수

    for i in range(2, n-2): #맨 좌측, 우측 2개는 땅이므로 범위에서 제외
        max_B = 0  # 좌우 4건물 중에 가장 높은 건물

        for j in range(i-2, i+3): #나를 포함 5개 건물중
            if j == i: #자기자신 제외
                continue
            elif max_B < num[j]: #제일 큰 건물을
                max_B = num[j] #max_B변수에 담는다

        if max_B < num[i]:
            cnt += num[i] - max_B #조망권을 확보한 세대수를 cnt에 담는다

    print(f'#{tc} {cnt}')