import sys
sys.stdin = open('sample_input.txt')


def bfs(x, cnt):
    global distance
    visited[x] = True
    queue = [(x, distance)]

    # 큐가 빌 때까지
    while queue:
        q = queue.pop(0)     # 현재 정점

        for nx in graph[q]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx, distance)
    print(cnt)


# 입력값 받기
t = int(input())

for tc in range(1, t + 1):
    v, e = map(int, input().split())     # 노드와 간선의 개수

    graph = [[] for _ in range(v + 1)]   # 인접 리스트
    for i in range(e):
        e1, e2 = map(int, input().split())
        graph[e1].append(e2)
        graph[e2].append(e1)

    s, g = map(int, input().split())     # 출발 노드, 도착 노드
    visited = [False] * (v + 1)          # 방문리스트

    bfs(s)



