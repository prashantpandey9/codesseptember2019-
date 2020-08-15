for j in range(int(input())):
    f=0
    m=0
    h=int(input())
    h=list(map(int,input().split()))
    for n in h:
        if n==2:
            f+=1
        if n==0:
            m+=1
    m=(m*(m-1))/2
    f=(f*(f-1))/2
    print(int(m+f))
