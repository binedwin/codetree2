def solution(num):
    answer=0
    for i in range(1,num+1,2):
        if num%i==0:
            answer+=1
    return answer