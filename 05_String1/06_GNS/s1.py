import sys
sys.stdin = open('GNS_test_input.txt', encoding="utf-8")

t = int(input())

for tc in range(1, t+1):
    n, c = input().split()
    numbers = list(input().split())

    planet = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new = [] #각 숫자의 개수(cnt)를 담을 리스트

#1. 일단 각 숫자의 개수를 받는다
    for idx, value in enumerate(planet):
        new.append(numbers.count(value)) #리스트에 각 숫자의 개수를 넣는다
    print(new)

#2. 개수에 맞개 차례대로 빈리스트에 담는다
    result = []

    for i in range(10):
        for j in range(new[i]):
            result.append(planet[i])

    print(f'#{tc}', *result)




