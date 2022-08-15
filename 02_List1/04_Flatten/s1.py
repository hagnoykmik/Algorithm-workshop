import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
# 0. 입력값 받기
    n = int(input()) #덤프 횟수
    arr = list(map(int, input().split()))

# 1. 내림차순으로 정렬하기(버블 정렬)
    for i in range(99, -1, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 2. 덤프하기(max-1 -> min+1)

    while n > 0:
        for k in range(100):  # 맨 왼쪽값(max)과 오른쪽값(min)의 인덱스 합은 99
            while arr[k] - arr[99-k] > 1: #1보다 크게 차이나면 덤프 횟수만큼 진행
                arr[k] -= 1
                arr[99-k] += 1
                n -= 1

    print(arr)
# 3. 덤프 진행 후 새로운 최고점과 최저점의 차이 반환
    arr.sort(reverse=True) #내림차순 정렬
    dump = arr[0] - arr[-1] #최고점과 최저점 차이 구하기
    print(f'#{tc} {dump}')

