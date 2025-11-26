def solution(n):
    # n을 2진수로 변환하면서 1의 개수 세기
    a = n
    n_cnt = 0
    
    while a > 0:
        if a % 2 == 1:       # 문자열 말고 숫자로 비교
            n_cnt += 1
        a //= 2

    # n보다 큰 수부터 검사
    num = n + 1

    while True:
        k = num
        cnt = 0

        # k의 1 개수 세기
        while k > 0:
            if k % 2 == 1:
                cnt += 1
            k //= 2

        # 1의 개수가 같으면 그 숫자가 정답
        if cnt == n_cnt:
            return num

        num += 1