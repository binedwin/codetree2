def solution(sizes):
    max_sizes=0

    for i in range(len(sizes)):
        sizes[i].sort()
        if max(sizes[i])>max_sizes:
            max_sizes=max(sizes[i])
        
    sizes.sort()
    
    return sizes[-1][0]*max_sizes