for h in range(int(input())):
    SUM=0
    ll=int(input())
    d=list(map(int,input().split()))
    d.sort()
    a=list(map(int,input().split()))
    a.sort()
    for n in range(ll):
        if d[n]>a[n]:
            SUM+=a[n]
        elif d[n]<a[n]:
            SUM+=d[n]
        else:
            SUM+=d[n]
    print(SUM)
    
    
