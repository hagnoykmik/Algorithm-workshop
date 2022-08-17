# 교수님 코드
# 파이써닉

# 스택 생성
my_stack = [] #파이썬은 리스트의 크기를 자동으로 늘려주고 줄여주므로 size가 필요없음.

# push
my_stack.append(1)
my_stack.append(2)

# pop
my_stack.pop()

# peek
print(my_stack[-1])

# is_empty
if not my_stack:  #?
    print('스택이 비었습니다.')

