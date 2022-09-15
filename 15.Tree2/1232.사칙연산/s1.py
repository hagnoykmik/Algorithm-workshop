import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):

    # 중위연산
    def inorder(t):
        if t > 0:
            inorder(ch_l[t])
            if ch_l[t] in '/*-+':

            else:
                stack.append(value[t])
            inorder(ch_r[t])


    n = int(input())
    ch_l = [0] * (n + 1)
    ch_r = [0] * (n + 1)
    value = [''] * (n + 1)

    for i in range(n):
        arr = list(input().split())
        p = int(arr[0])
        value[p] = arr[1]

        if arr[1] in '/+*-':
            ch_l[p] = int(arr[2])
            ch_r[p] = int(arr[3])

    stack = []

    inorder(1)
    print(stack)

    result = int(stack[0])

    for j in range(len(stack)):

        if stack[j] == '*':
            result *= int(stack[j + 1])
        elif stack[j] == '/':
            result //= int(stack[j + 1])
        elif stack[j] == '-':
            result -= int(stack[j + 1])
        elif stack[j] == '+':
            result += int(stack[j + 1])

    print(result)

