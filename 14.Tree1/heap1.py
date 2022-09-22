# 최대힙

def enq(n):
    # 완전 이진 트리에서 마지막 정점을 하나 추가한다
    global last
    last += 1         # 마지막 정점 추가
    heap[last] = key  # 마지막 정점에 추가할 값(key)을 넣는다

    c = last
    p = c // 2        # 완전 이진 트리에서 부모 정점 번호

    # 부모가 있고, 부모 < 자식 인 경우 자리 교환
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 부모를 새로운 자식으로
        c = p
        p = c // 2

heap = [0] * 100
last = 0
