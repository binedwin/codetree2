def solution(s):
    a_list=list(s)
    answer_list=[]
    if a_list[0]==')' or a_list[-1]=='(':
        return False
        
    for i in a_list:
        if i == '(':
            answer_list.append('(')
        else:
            if not answer_list:
                return False
            answer_list.pop()
    
    if not answer_list:
        answer=True
    else:
        answer=False
    
    return answer