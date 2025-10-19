def solution(s):
    answer= s.lower()
    count_p = answer.count('p')
    count_y = answer.count('y')
    if count_p==count_y:
        return True 
    else:
        return False