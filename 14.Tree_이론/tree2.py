# 자식을 인덱스로 부모 번호 저장

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
par = [0] * (V + 1)

for i in range(E):    # 2개씩 자르기
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:   # 아직 자식이 없으면
        ch1[p] = c    # 자식 1로 저장
    else:
        ch2[p] = c

    # 루트를 찾기 위해 쓴다
    par[c] = p

root = find_root(v)  # 루트 찾기
