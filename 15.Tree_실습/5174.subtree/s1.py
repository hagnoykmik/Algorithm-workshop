import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t+1):

    def subtree(num):
        global cnt
        cnt += 1
        # 자식노드가 둘다 0이면 리프 노드이므로 멈춘다
        if ch1[num] != 0:
            subtree(ch1[num])
        if ch2[num] != 0:
            subtree(ch2[num])

    # 간선의 개수
    e, n = map(int, input().split())
    v = e + 1  # 정점의 개수
    nods = list(map(int, input().split()))

    ch1 = [0] * (v + 1)
    ch2 = [0] * (v + 1)

    # 부모 노드와 자식 노드로 담기
    for i in range(e):
        p, c = nods[2 * i], nods[2 * i + 1]

        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    # N을 루트로 하는 서브 트리
    cnt = 0
    subtree(n)

    print(ch1)
    print(ch2)
    print(f'#{tc} {cnt}')