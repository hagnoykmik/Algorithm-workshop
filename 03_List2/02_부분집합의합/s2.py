import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    n = len(arr)

# 부분집합의 개수만큼 반복 & 모든 부분집합 검색
    for i in range(1, 1 << n):
        sum_s = 0 #부분집합의 원소들의 합(i가 바뀌면==다른 부분집합이 되면 초기화)

        for j in range(n): #j = 0부터 m-1까지 인덱스로 이용(arr의 값)
            if i & (1 << j): #i의 j번째 비트가 i이면(부분집합에 포함되면)
                sum_s += arr[j] #부분집합 리스트에 원소로 넣는다

        if sum_s == 0: #합이 k라면 1출력
            print(f'#{tc} 1')
            break

    else: #아니라면 0출력
        print(f'#{tc} 0')

