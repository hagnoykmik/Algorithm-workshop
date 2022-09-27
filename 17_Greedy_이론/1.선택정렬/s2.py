# 재귀함수
def selectionSort(arr, s):
    n = len(arr)

    if s == (n - 1):
        return arr
    else:
        minI = s
        for i in range(s + 1, n):
            if arr[minI] > arr[i]:
                minI = i
                # 현재 인덱스(s)를 제일 작은 값으로 만든다
        arr[minI], arr[s] = arr[s], arr[minI]

        selectionSort(arr, s + 1)  # 재귀함수 호출


arr = [2, 4, 6, 1, 9, 8, 7, 0]
selectionSort(arr, 0)
print(arr)