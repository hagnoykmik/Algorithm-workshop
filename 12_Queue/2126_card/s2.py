n = int(input())
queue = list(range(1, n+1))

while len(queue) > 1:   # 카드가 한 장 남았을 때까지 반복
    print(queue.pop(0), end=' ')
    queue.append(queue.pop(0))

print(queue[0])