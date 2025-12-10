def solution(sizes):
    w=0
    h=0
    for i in sizes:
        i.sort()
    for j in range(len(sizes)):
        if w<=sizes[j][0]:
            w=sizes[j][0]
        if h<=sizes[j][1]:
            h=sizes[j][1]
    return w*h