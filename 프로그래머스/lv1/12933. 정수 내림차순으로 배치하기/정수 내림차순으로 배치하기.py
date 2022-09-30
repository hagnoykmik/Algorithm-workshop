def solution(n):      
    answer = ''
    n = sorted(str(n), reverse=True)
    return int(''.join(n))
