import sys
sys.stdin = open('sample_input.txt')


def binary(n, arr, key):
    global result
    l = 0
    r = n - 1
    memo = 0  # 왼, 중, 오 -1, 0, 1

    while l <= r:
        mid = (l + r) // 2

        # mid에 찾는 값이 있다면
        if key == B[mid]:
            result += 1
            return

        # left 탐색
        elif key < B[mid] and memo != -1:
            r = mid - 1
            memo = -1

        # right 탐색
        elif key > B[mid] and memo != 1:
            l = mid + 1
            memo = 1

        else:
            return


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A = set(A)  # 중복 값 제거
    B = list(map(int, input().split()))

    result = 0

    for key in A:
        binary(m, B, key)

    print(f'#{tc} {result}')