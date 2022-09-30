# prim
def prim(start):
    visited = [False] * (n + 1)    # 사이클을 안 만들기 위해서 방문리스트 작성
    distance = [INF] * (n + 1)     # 정점에서의 최소 비용을 구하기 위해서
    distance[start] = 0
    cost = 0

    for _ in range(n):
        min_distance = INF         # 정점이 바뀌면 최소 거리를 초기화
        # 현재 정점에서 최소 거리를 구한다
        for idx, dist in enumerate(distance):
            if not visited[idx] and dist < min_distance:  # 아직 방문하지 않았고, 최소 거리라면 갱신
                min_distance = dist
                min_i = idx

        # 해당 정점 방문 처리하고 비용을 더한다
        visited[min_i] = True
        cost += min_distance

        # 현재 정점에서 인접한 정점들 중 거리가 더 가깝다면 갱신
        for next_i, dist in graph[min_i]:
            if not visited[next_i] and dist < distance[next_i]:
                distance[next_i] = dist

    return cost


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
INF = 9999999

print(prim(1))