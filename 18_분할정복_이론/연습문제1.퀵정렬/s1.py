import sys
sys.stdin = open('input.txt')

# pivot 찾기
def partition(arr, left, right):
    pivot = arr[left]
    i = left
    j = right

    while i <= j:
        # 1. i 찾기
        while i <= j and pivot >= arr[i]:
            i += 1
        # 2. j 찾기
        while i <= j and pivot <= arr[j]:
            j -= 1
        # i가 j보다 작으면 자리를 바꾼다
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # while문을 나가게 되면 (i < j) pivot과 자리바꾼다
    arr[left], arr[j] = arr[j], arr[left]

    # pivot의 인덱스 return
    return j


# 퀵 정렬
def quicksort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quicksort(arr, left, middle - 1)   # 왼쪽 정렬
        quicksort(arr, middle + 1, right)  # 오른쪽 정렬


t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split()))

            # 리스트, left, right
    quicksort(arr, 0, len(arr) - 1)

    print(arr)