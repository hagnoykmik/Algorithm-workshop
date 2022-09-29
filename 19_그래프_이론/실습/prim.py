# 1) 일반적인 프림 알고리즘

def prim(start):
    visited = [False] * (n + 1)  # MST에 포함 여부 리스트
    distance = [INF] * (n + 1)   # distance[v] => 정점 v가 MST에 속한 정점과 연결된 간선의 비용
    distance[start] = 0          # 출발점은 비용이 안드니까 0
    cost = 0                     # MST의 비용 총합(== 최소 비용)

    # 정점의 개수(n)만큼 반복하면서 모든 정점을 이은 MST 생성
    for _ in range(n):
        # 1. MST의 정점에서 이동할 수 있는 모든 정점 중 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
        min_dist = INF
        for i, dist in enumerate(distance):
            # 아직 MST에 없으면
            if not visited[i] and dist < min_dist:
                # 최소값 갱신
                min_node = i     # 2. 3번과 인접한 것 중에 최소비용 갱신
                min_dist = dist  # 31

        # 2. 해당 정점을 MST에 포함하고 비용을 더함
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
                              # graph[1] - 1에서 갈 수 있는 2번에 대해서 가장 최소 비용
            if not visited[next_node] and dist < distance[next_node]:
                                        # 지금 비교할 비용 (32, 31, 60, 51) < 원래 비용(INF)(F들 중에 가장 작은것)
                distance[next_node] = dist

    return cost


n, m = map(int, input().split())    # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]  # 인접 리스트
INF = 99999999                      # 나올 수 없는 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    graph[s].append((e, w))  # 무방향
    graph[e].append((s, w))

print(prim(1))  # 1번 정점에서 시작