for n in range(int(input())):
    a,k=map(int,input().split())
    e,m=0,0
    for n in range(int(input())):
        q1,q2=map(int,input().split())
        e+=q1
        m+=q2
    ww=a*e+k*m
    ee=a*m+k*e
    if ee<ww:
        print(ee)
    else:
        print(ww)
