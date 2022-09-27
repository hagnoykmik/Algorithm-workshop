'''
그리디
지금 나한테 좋은건 최소값을 구하는 것
제일 큰 값부터 찾아나가기
'''

n, k = map(int, input().split())
coins = [int(input() for _ in range(n))]
result = 0  # 개수

for i in range(n-1, -1, -1):
    # 나눠지지 않는 건 어차피 몫이 0임
    result += (k // coins[i])
    # k를 갱신
    k %= coins[i]

    print(result)