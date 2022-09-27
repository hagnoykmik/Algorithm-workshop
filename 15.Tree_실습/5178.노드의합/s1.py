import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, 11):
    # 노드 개수, 리프 노드 개수, 출력할 노드 번호
    n, m, l = map(int, input().split())
    nods = [0] * (n + 2)

    # 리프 노드에 값 채우기
    for _ in range(m):
        nod, num = map(int, input().split())
        nods[nod] = num

    # 자식 노드 값으로 부모 노드의 값 구하기
    for i in range(n, 0, -1):
        if nods[i] == 0:
            nods[i] = nods[2 * i] + nods[2 * i + 1]

    print(f'#{tc} {nods[l]}')
