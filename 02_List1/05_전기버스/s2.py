#교수님 코드
import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))

    start = 0 # 출발점
    end = k # 도착점
    is_possible = True # 충전소가 없는 경우 판별
    result = 0 # 결과값

    # 아이디어 : 최대한 이동거리만큼 이동하고 충전소 없으면 뒤로(거꾸로) 이동
    while end < n: # 종점에 도착하지 않은 경우


        for i in range(end, start, -1):
            #1. 충전소 있으면
            if i in stations:
                start = i # start갱신
                end = start + k
                result += 1
                break # for문 탈출!
        else:
            #2. 충전소가 없으면
            is_possible = False
            result = 0
            break

    print(f'#{tc} {result}')