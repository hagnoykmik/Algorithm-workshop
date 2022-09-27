import sys
sys.stdin = open('sample_input.txt')


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i <= j:
        while i <= j and pivot >= arr[i]:
            i += 1
        while i <= j and pivot <= arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]

    return j


def quicksort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quicksort(arr, left, middle - 1)
        quicksort(arr, middle + 1, right)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    quicksort(arr, 0, n - 1)

    print(f'#{tc} {arr[n//2]}')