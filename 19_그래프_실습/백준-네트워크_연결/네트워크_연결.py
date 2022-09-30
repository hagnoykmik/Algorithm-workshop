# find-set
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])  # 경로 압축
    return parent[node]                        # 경로 압축


n = int(input())  # 컴퓨터의 수
e = int(input())  # 연결 수
network = []
for _ in range(e):
    s, e, c = map(int, input().split())  # 시작, 도착, 비용
    network.append((c, s, e))

network.sort()               # 맨 앞 원소 기준 정렬(오름차순)

parent = list(range(n + 1))  # make-set
counts = 0  # 더이상 간선을 선택하지 않아도 되는 때를 판별
cost = 0    # 비용이 최소가 되는 것을 찾는다

for c, x, y in network:
    # find-set
    x_root = find_set(x)
    y_root = find_set(y)

    # Union (서로소라면)
    if x_root != y_root:
        parent[y_root] = x_root
        cost += c
        counts += 1

        # 모든 정점을 다 연결했으면 종료
        if counts >= n - 1:
            break

print(counts)
print(cost)





