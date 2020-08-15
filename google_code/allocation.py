for w in range(int(input())):
    l=list(map(int,input().split()))
    n=l[0]
    b=l[1]
    a=list(map(int,input().split()))
    a.sort()
    g=[]
    su=0
    count=0
    for h in a:
        su+=h
        g.append(su)
        if su<=b:
            count+=1
    print("Case #"+str(w+1)+":",count)
