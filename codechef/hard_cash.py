for n in range(int(input())):
    o=list(map(int,input().split()))
    n=o[0]
    k=o[1]
    a=list(map(int,input().split()))
    s=0
    for n in a:
        d=n%k
        s+=d
    print(s%k)
