def solution(lines):
    line = [0] * 202
    plus_a = 100
    cnt = 0
    
    for i in range(3):
        s = lines[i][0] + plus_a
        e = lines[i][1] + plus_a
        for j in range(s, e):  # 끝점은 제외
            line[j] += 1

    for i in range(201):
        if line[i] >= 2:
            cnt += 1
    return cnt