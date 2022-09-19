import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input()))
    binary = []

    # 7byte씩 담기
    for i in range(len(arr) // 7):
        binary.append(arr[i * 7:(i + 1) * 7])
        result = 0

        # 2의 j승 곱하기
        for j in range(7):
            result += (binary[i][6 - j]) << j

        print(result, end=' ')
    print()
