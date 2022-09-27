
def bfs(v):
    visited[v] = True       # 방문 표시
    queue = [v]             # 시작 정점을 큐에 담고 초기화
    print(v, end=' ')
    # 인접한 정점 큐에 담기
    while queue:
        v = queue.pop(0)    # 현재 정점
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
                print(next_v, end=' ')


n, m = map(int, input().split())       # 정점, 간선
path = list(map(int, input().split()))

# 방문 리스트
visited = [False] * (n + 1)

# 인접 리스트
graph = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = path[i * 2], path[i * 2 + 1]
    graph[v1].append(v2)
    graph[v2].append(v1)

# 1번부터 시작
bfs(1)


