#     if arr[1] in '/+*-':
#         ch_l[p] = int(arr[2])
#         ch_r[p] = int(arr[3])
#
# stack = []
#
# result = int(stack[0])

# for j in range(len(stack)):
#
#     if stack[j] == '*':
#         result *= int(stack[j + 1])
#     elif stack[j] == '/':
#         result //= int(stack[j + 1])
#     elif stack[j] == '-':
#         result -= int(stack[j + 1])
#     elif stack[j] == '+':
#         result += int(stack[j + 1])