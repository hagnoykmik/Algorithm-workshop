# 실패한 내코드
import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 0. 입력값 받기
    n = int(input())  # 덤프 횟수
    arr = list(map(int, input().split()))

    # 1. 내림차순으로 정렬하기(버블 정렬)
    for i in range(99, -1, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 2. 덤프하기(max-1 -> min+1)
    for k in range(100):  # 맨 왼쪽값(max)과 오른쪽값(min)의 인덱스 합은 99
        while arr[k] - arr[99 - k] > 1:  # 1보다 크게 차이나면 덤프 횟수만큼 진행
            arr[k] -= 1
            arr[99 - k] += 1
            n -= 1
            if n == 0:  # n이 0이되면 종료....가안됨(if문을 밖에도 써주면 너무 일찍 멈춤)
                break  # 브레이크는 제일 가까운 반복 루프 1개만 탈출가능함

    # 3. 덤프 진행 후 새로운 최고점과 최저점의 차이 반환
    arr.sort(reverse=True)  # 내림차순 정렬
    dump = arr[0] - arr[-1]  # 최고점과 최저점 차이 구하기
    print(f'#{tc} {dump}')

    # 이중 반복문 탈출 방법!
    for k in range(100):  # 맨 왼쪽값(max)과 오른쪽값(min)의 인덱스 합은 99
        while arr[k] - arr[99 - k] > 1:  # 1보다 크게 차이나면 덤프 횟수만큼 진행
            arr[k] -= 1
            arr[99 - k] += 1
            n -= 1
            if n == 0:  # n이 0이되면 종료....가안됨(if문을 밖에도 써주면 너무 일찍 멈춤)
                break  # 브레이크는 들여쓰기 기준 제일 가까운 반복 루프 1개만 탈출가능함 이경우는 가장 가까운 while만 탈출하고
                # for문은 0부터 99까지 반복

    breaker = False  # 반복문 탈출을 위한 변수 지정
    for k in range(100):
        if breaker:
            break  # 이브레이크는 for문을 탈출한다.
        while arr[k] - arr[99 - k] > 1:
            arr[k] -= 1
            arr[99 - k] += 1
            n -= 1
            if n == 0:
                breaker = True  # for문 탈출을 위해서 True로 변수 저장
                break  # 브레이크는 제일 가까운 반복 루프 1개만 탈출가능함

    for k in range(100):
        while arr[k] - arr[99 - k] > 1:
            if n == 0:  # n이 0이되면 종료....가안됨(if문을 밖에도 써주면 너무 일찍 멈춤)
                break  # 브레이크는 제일 가까운 반복 루프 1개만 탈출가능함 while문을 탈출하고 for 문은 계속 0~99까지 반복하지만
                # 아래식을 수행하기전에 탈출을 하기때문에 결과값에는 영향없음.
            arr[k] -= 1
            arr[99 - k] += 1
            n -= 1
    # 예외처리라는 방법을 통해서 이중 반복문을 탈출할 수 있지만 이건 나도 사용 안해봐서 몰라요...
    # 이중 반복문 탈출방법 이라고 구글링하면 나올거에요.
