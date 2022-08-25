import sys
sys.stdin = open('sample_input.txt')


def binary(key, page):
    start = 1
    end = page
    cnt = 0

    while start < end:
        middle = (start + end) // 2
        cnt += 1

        if middle == key:
            return cnt

        elif middle > key:
            end = middle

        elif middle < key:
            start = middle


t = int(input())
for tc in range(1, t + 1):
    p, pa, pb = map(int, input().split())

    a = binary(pa, p)
    b = binary(pb, p)

    if a == b:
        print(f'#{tc} 0')
    elif a > b:
        print(f'#{tc} B')
    elif a < b:
        print(f'#{tc} A')

