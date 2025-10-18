def solution(n):
    # 1. 정수 n을 문자열로 변환하여 각 자릿수를 분리합니다.
    # 예: 118372 -> '1', '1', '8', '3', '7', '2'
    s = str(n)
    
    # 2. 자릿수(문자)들을 내림차순(reverse=True)으로 정렬합니다.
    # sorted() 함수는 문자를 아스키 코드 값에 따라 정렬합니다.
    # 예: ['8', '7', '3', '2', '1', '1']
    sorted_digits = sorted(s, reverse=True)
    
    # 3. 정렬된 자릿수들을 다시 하나의 문자열로 합칩니다.
    # 예: "873211"
    result_string = "".join(sorted_digits)
    
    # 4. 최종 문자열을 정수형(Integer)으로 변환하여 반환합니다.
    result_integer = int(result_string)
    
    return result_integer

# 예시:
# print(solution(118372))  # 출력: 873211
# print(solution(4213))    # 출력: 4321