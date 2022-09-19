def bit_print(i):  # 7번 비트부터 0번 비트까지 출력
    s = ''
    for j in range(7, -1, -1):
        # i의 j번 비트가 0이 아니면 1을 추가
        s += '1' if (i & (1 << j)) else '0'
    print(s)

bit_print(5)
bit_print(-5)
bit_print(-6)
bit_print(-6 >> 1)

