# 완전 탐색 2
def f(i, k):
    global answer

    # 자리가 다 정해졌으면
    if i == k:
        run = 0
        tri = 0
        # 카드의 앞부분
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
            run += 1
        # 카드의 뒷부분
        if card[3] == card[4] and card[4] == card[5]:
            tri += 1
        if card[3] + 1 == card[4] and card[4] + 1 == card[5]:
            run += 1
        # Baby gin 인지 검사
        if run + tri == 2:
            answer = 'True'

    # 자리결정 경우의 수
    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            f(i + 1, k)   # 다음자리 결정
            card[i], card[j] = card[j], card[i]  # 원상복귀


# t = int(input())
# for tc in range(1, t + 1):
card = [1, 2, 3, 1, 2, 3]
# card = list(map(int, input()))
n = len(card)
answer = 'False'
f(0, n)

print(answer)