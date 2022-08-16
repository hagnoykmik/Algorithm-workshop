import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    str1 = input()
    str2 = input()

# 1. 글자마다 개수를 센다
    n = len(str1)
    counter = [0] * n  # 문자별 개수를 담을 카운팅 정렬

    for i, char in enumerate(str1): #인덱스와 값을 동시에 빼준다
        for check in str2: #str2의 문자열과 하나씩 비교해서
            if char == check: #같을 때마다
                counter[i] += 1 #인덱스에 카운트 값을 넣어준다
# 2. 최고 개수 반환
    max_n = 0
    for j in range(n): #카운팅 정렬을 돌면서 max값을 담는다
        if max_n < counter[j]:
            max_n = counter[j]

    print(f'#{tc} {max_n}')



