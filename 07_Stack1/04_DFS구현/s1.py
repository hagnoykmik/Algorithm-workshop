
# 3. 함수 만들기
def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for next_v in graph[v]:
        if not visited[next_v]: # 아직 방문하지 않았다면
            dfs(next_v)


# 0. 입력값 받기
n, m = map(int, input().split()) # 정점, 간선
edges = list(map(int, input().split())) # 간선 정보


# 1. 인접 리스트 만들기
graph = [[] for _ in range(n + 1) ] # n+1인 이유는 정점 번호가 1이기 때문

for i in range(0, len(edges), 2): # 2개씩 담는다
    v1, v2 = edges[i], edges[i + 1]
    graph[v1].append(v2)
    graph[v2].append(v1)


# 2. 방문 처리 리스트 만들기
visited = [False] * (n + 1)

# 4. 시작 정점을 1로 탐색
dfs(1)

print(graph)