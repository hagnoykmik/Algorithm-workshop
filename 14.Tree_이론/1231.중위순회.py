for tc in range(1, 11):
    print('\n', f'#{tc}', end='')

    # 중위순회 함수
    def inorder(n):
        if n:
            inorder(ch1[n])
            print(char[n], end='')
            inorder(ch2[n])


    V = int(input())
    E = V - 1
    char = [''] * (V + 1)  # 문자열을 담을 리스트 생성
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    root = 1

    for _ in range(V):
        nods = list(input().split())  # 간선의 정보가 다르므로 일단 리스트로 받는다

        p = int(nods[0])              # 리스트의 첫번째는 무조건 p
        char[p] = nods[1]             # 문자를 p를 인덱스로 하여 리스트에 담는다

        if len(nods) > 2:             # p와 문자열이외에 정보가 있다면 부모 번호를 인덱스로 자식 번호 저장
            for i in range(2, len(nods)):
                if ch1[p] == 0:
                    ch1[p] = int(nods[i])
                else:
                    ch2[p] = int(nods[i])

    inorder(root)
