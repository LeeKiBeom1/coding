def solution(s1, s2):
    i = set(s1) & set(s2)
    answer = len(i)
    return answer