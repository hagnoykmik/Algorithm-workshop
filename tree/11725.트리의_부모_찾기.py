n = int(input())
root = 1

nod1 = [0] * (n + 1)
nod2 = [0] * (n + 1)

arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n - 1):
    n1, n2 = map(int, input().split())

    nod1[n1] = n2
    nod2[n2] = n1

print(nod1)
print(nod2)
