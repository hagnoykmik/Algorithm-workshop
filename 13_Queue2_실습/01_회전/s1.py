import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))

    for i in range(m):
        queue.append(queue.pop(0))

    print(f'#{tc} {queue[0]}')