# 반복문
def selectionSort(arr, s):
    n = len(arr)

    for i in range(0, n - 1):  # 마지막 2개 남았을 때는 0부터 n-2까지
        minI = i               # 맨 앞자리를 제일 작은 숫자라고 가정

        # 남은 자리와 비교
        for j in range(i + 1, n):  # i의 오른쪽 숫자들 중에 가장 작은 값을 가지는 인덱스를 i와 바꾼다
            if arr[j] < arr[minI]:
                minI = j           # 최솟값을 작은 값의 인덱스로 바꾼다

        # 가장 작은 값을 현재 비교하는 인덱스 값과 바꾼다
        arr[minI], arr[i] = arr[i], arr[minI]


arr = [2, 4, 6, 1, 9, 8, 7, 0]
selectionSort(arr, 0)
print(arr)