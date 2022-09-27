'''
정점의 개수 V : 1~E+1
간선의 개수 E : 마지막 V-1개 (12)
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def preorder(n):
    if n:                  # 0이 아니라면
        print(n, end=' ')  # visit(n)
        preorder(ch1[n])   # left
        preorder(ch2[n])   # right


V = int(input())  # 정점 개수, 마지막 정점 번호 
E = V - 1
root = 1
nods = list(map(int, input().split()))

# 부모 노드를 인덱스로 이용해 자식 노드 번호 채우기
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

# 2개씩 잘라서 채우기
for i in range(E):
    p, c = nods[i * 2], nods[i * 2 + 1]

    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

preorder(root)