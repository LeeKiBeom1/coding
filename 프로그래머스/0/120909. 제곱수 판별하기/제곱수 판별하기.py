def solution(n):
    i = n ** 0.5
    if int(i) ** 2 == n:
        answer = 1
    else:
        answer = 2
    return answer