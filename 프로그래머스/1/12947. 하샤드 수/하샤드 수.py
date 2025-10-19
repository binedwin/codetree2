def solution(x):
    sum_of_digits = sum(map(int, str(x)))

    if x % sum_of_digits == 0:
        return True
    else:
        return False
