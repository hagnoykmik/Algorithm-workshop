# 설마 버퍼............?
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    pw = list(map(int, input().split()))

    while pw:
        for i in range(1, 6):
            p = pw.pop(0)
            pw.append(p - i)
            if p - i <= 0:
                pw.append(0)
                break

    print(f'#{tc}', *pw)