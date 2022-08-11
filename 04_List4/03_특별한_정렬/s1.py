import sys
sys.stdin = open('sample_input.txt')

'''
아이디어
1. 먼저 숫자를 정렬한다
2. 큰수와 작은수를 나누어 담는다
3. 큰수와 작은수를 번갈아가며 하나의 리스트에 담는다
'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))

# 1. 일단 리스트를 정렬한다(버블 정렬)
    for i in range(n-1, 1, -1): #9 (마지막 값부터)
        for j in range(i): #j= 0 ~ 8
            if numbers[j] > numbers[j+1]: #0과 1칸 비교
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] #앞에 있는 값이 더 크면 두값의 자리를 바꾼다
    # numbers = [3, 9, 17, 18, 21, 26, 30, 36, 43, 46, 59, 60, 62, 64, 69, 71, 75, 88, 97, 98] 오름차순으로 정렬

# 2. 정렬한 리스트의 반을 나눠 큰수를 담을 리스트와 작은수를 담을 리스트에 넣는다.
    max_list = []
    min_list = []

    for k in range(n//2):
        min_list += [numbers[k]] #원소를 넣기 위해 배열형태로 넣는다
        #[3, 9, 17, 18, 21, 26, 30, 36, 43, 46]

    for l in range(n//2, n):
        max_list += [numbers[l]]
    max_list = max_list[::-1] #들여쓰기가 제일어렵다
    #[98, 97, 88, 75, 71, 69, 64, 62, 60, 59]
    print(max_list)

    # 3. 큰 수와 작은 수를 번갈아가며 하나의 리스트에 담는다
    special_list = [0] * n

    for x in range(n//2):
        special_list[2*x] = max_list[x] #짝수번째에 큰값들을 내림차순으로 넣고
        special_list[2*x+1] = min_list[x] #홀수번째에는 작은 값들을 오름차순으러 넣는다

    special_list = special_list[0:10] #10개까지만 출력
# 4. 리스트로 담은 원소들을 언패킹한다
    print(f'#{tc}', *special_list)

