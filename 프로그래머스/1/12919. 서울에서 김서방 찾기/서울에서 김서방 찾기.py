def solution(seoul):
    cnt=0
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            cnt=i
    return f"김서방은 {cnt}에 있다"