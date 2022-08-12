import sys
sys.stdin = open('sample_input.txt')

'''
아이디어
1. 집합 A의 부분 집합 중 N개의 원소를 갖고 있는 것들을 찾는다(모든 부분집합 탐색)
2. 그것들의 합을 구한다 
3. 원소의 합이 K인 부분집합의 개수를 출력
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
t = int(input())

for tc in range(1, t+1):
    n, k = input().split()
    n = int(n)
    k = int(k)

    m = len(numbers)
    cnt = 0 #조건에 만족하는 부분집합 개수

# 1. 부분집합의 개수만큼 반복
    for i in range(1 << m):
        sum_subset = 0

# 2. 모든 부분집합 탐색
        for j in range(m):
            if i & (1 << j): #모든 부분집합
                sum_subset += numbers[j] #부분집합을 다 담아라
                cnt += 1

# 4. 조건에 만족하면
            if cnt == n: #부분집합의 개수가 3개일때
                if sum_subset == k:
                    print(f'#{tc} 1')
                    break
    else:
        print(f'#{tc} 0')
