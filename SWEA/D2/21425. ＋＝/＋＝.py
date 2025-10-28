T =int(input())
cnt=0

for i in range(T):
    a,b,n =map(int, input().split())
    cnt=0
    while a<=n and b<=n:
        if a<b:
            a+=b
        else:
            b+=a
        cnt+=1
    print(cnt)
        