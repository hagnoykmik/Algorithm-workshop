n, k = map(int, input().split())

cnt = 0
coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

# coin을 단위가 큰 것부터 나눠본다
for coin in coins[::-1]:
    # k보다 큰 단위여도 몫이 0이니까 상관없음
    cnt += k // coin
    k %= coin

print(cnt)




