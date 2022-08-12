
import sys
sys.stdin = open('test_input.txt', encoding="utf-8")

for tc in range(1, 11):
    n = int(input())
    word = input()
    str_search = input()

    cnt = str_search.count(word)
    print(f'#{tc} {cnt}')

