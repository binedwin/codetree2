def solution(numbers):
    answer=0
    for i in range(10):
        cnt=0   
        for j in range(len(numbers)):
            if numbers[j]==i:
                cnt+=1
                break
        if cnt==0:
            answer+=i
    return answer