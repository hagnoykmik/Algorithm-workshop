# 리스트 이용

queue = []        # 큐역할을 할 빈 리스트

# 세개의 데이터 1, 2, 3을 차례로 큐에 삽입
print(queue)      # []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)      # [1, 2, 3]

# 큐에서 세개의 데이터를 차례로 꺼내서 출력
# 선입선출을 위해 pop메서드의 인자로 인덱스 0을 준다
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
'''
1
2
3
'''

