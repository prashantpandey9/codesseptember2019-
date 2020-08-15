for i in range(int(input())):
    d=list(map(int,input().split()))
    f=[0]*(d[1]+1)
    n=list(map(int,input().split()))
    m=list(map(int,input().split()))
    for j in range(d[0]):
                f[n[j]]+=m[j]
    s=[]
    for i in f:
        if i != 0:
            s.append(i)    
    print(min(s))
