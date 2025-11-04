def solution(array):
    array_most = [0] * 1001  # 숫자의 등장 횟수를 저장
    for i in array:
        array_most[i] += 1

    max_count = max(array_most)           # 가장 많이 등장한 횟수
    if array_most.count(max_count) >= 2:  # 최빈값이 여러 개면
        return -1

    mode = array_most.index(max_count)    # 최빈값의 인덱스(=숫자)
    return mode