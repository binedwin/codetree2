n = int(input())

for i in range(n):
    s = input().strip()
    year, month, day = s[:4], s[4:6], s[6:]

    m = int(month)
    d = int(day)

    valid = True  # 유효 여부 표시 변수

    if m < 1 or m > 12:
        valid = False
    else:
        # 각 달의 마지막 날
        if m in [1, 3, 5, 7, 8, 10, 12]:
            max_day = 31
        elif m == 2:
            max_day = 28
        else:
            max_day = 30

        if d < 1 or d > max_day:
            valid = False

    if valid:
        print(f"#{i+1} {year}/{month}/{day}")
    else:
        print(f"#{i+1} -1")