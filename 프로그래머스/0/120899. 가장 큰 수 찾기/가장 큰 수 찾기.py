def solution(array):
    num1 = max(array)

    num2 = array.index(num1)
    
    # 3. [가장 큰 수, 인덱스] 형태로 answer 리스트에 담아줍니다.
    answer = [num1, num2]
    
    return answer