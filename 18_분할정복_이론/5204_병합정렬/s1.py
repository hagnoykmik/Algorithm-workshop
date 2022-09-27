import sys
sys.stdin = open('sample_input.txt')

# 병합
def merge(left, right):
    # 비교
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    result = []
    i = 0  # left
    j = 0  # right

    # 인덱스는 0, 1, ..., len(arr)-1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # while문 탈출 후 남은 거 다 넣어주기
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 분할
def partition(arr):
    # 더이상 나눌 수 없으면 종료
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = partition(arr[:mid])
    right_arr = partition(arr[mid:])

    return merge(left_arr, right_arr)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge_arr = partition(arr)

    print(f'#{tc} {merge_arr[n//2]} {cnt}')


