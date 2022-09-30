def solution(n):      
    answer = ''
    n = sorted(str(n), reverse=1)
    for num in n:
        answer += num
    return int(answer)