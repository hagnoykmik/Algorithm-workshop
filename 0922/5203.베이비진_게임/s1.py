import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t + 1):
    cards = list(map(int, input().split()))
    n = len(cards)
    p1 = [0] * (n // 2)
    p2 = [0] * (n // 2)

    # 카드 나눠 담기
    for i in range(n):
        if i % 2 == 0:
            p1[i // 2] = cards[i]
        else:
            p2[i // 2] = cards[i]

    # run or triplet 검사


