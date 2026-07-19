def solution(n):
    answer = 0
    str1 = str(n)
    for num1 in str1:
        answer += int(num1)
    return answer