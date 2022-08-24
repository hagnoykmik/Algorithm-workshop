# 선형 큐
class Queue:
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        self.front = -1   # 큐의 머리
        self.rear = -1    # 큐의 꼬리

    # 1. 큐의 뒤쪽에 원소를 삽입하는 연산
    def enqueue(self, item):
        if self.is_full():
            print('큐가 가득차서 원소를 삽입할 수 없습니다.')
        else:
            self.rear += 1
            self.items[self.rear] = item

    # 2. 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산
    def dequeue(self):
        if self.is_empty():
            print('큐가 비어서 원소를 삭제 및 반환할 수 없습니다.')
        else:
            self.front += 1
            return self.items[self.front]

    # 3. 큐가 공백상태인지 확인
    def is_empty(self):
        return self.rear == self.front     # 머리와 꼬리가 같은 곳을 가리키면 공백

    # 4. 큐가 포화상태인지 확인
    def is_full(self):
        return self.rear == self.size - 1   # 꼬리가 큐의 마지막을 가리키면 포화상태

    # 5. 큐의 앞쪽에서 원소를 삭제없이 반환하는 연산
    def q_peek(self):
        if self.is_empty():
            print('큐가 비어서 원소를 반환할 수 없습니다.')
        else:
            return self.items[self.front]

# 크기가 3인 큐 생성
queue = Queue(3)

# 세개의 데이터 1, 2, 3을 차례로 큐에 삽입
print(queue.items)    # [None, None, None]
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.items)    # [1, 2, 3]

# 큐에서 세개의 데이터 차례로 꺼내서 출력
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())