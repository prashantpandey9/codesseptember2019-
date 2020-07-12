def indiSum(n):
    e=str(n)
    s=0
    for i in e:
        s+=int(i)
    return s

for j in range(int(input())):
    cs=0
    ms=0
    for j in range(int(input())):
        c,m=map(int,input().split())
        ic=indiSum(c)
        im=indiSum(m)
        if ic>im:
            cs+=1
        elif ic==im:
            cs+=1
            ms+=1
        else:
            ms+=1
    if cs>ms:
        print(0,cs)
    elif cs==ms:
        print(2,cs)
    else:
        print(1,ms)
