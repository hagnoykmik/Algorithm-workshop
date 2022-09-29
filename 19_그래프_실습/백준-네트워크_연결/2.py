from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    cost = 0

    # 힙이 다 소진될 때 까지
    while heap:
        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist

        # 인접 정점에 대해 가중치와 정점 정보를 힙에 삽입
        for next_node, c in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (c, next_node))

    return cost


n = int(input())  # 컴퓨터의 수
e = int(input())  # 연결 수

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    s, e, c = map(int, input().split())  # 시작, 도착, 비용
    graph.append((e, c))
    graph.append((s, c))


print(prim(1))





