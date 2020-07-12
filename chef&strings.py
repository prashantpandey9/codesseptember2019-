for j in range(int(input())):
    N=int(input())
    p=list(map(int,input().split()))
    s=0
    for n in range(len(p)-1):
        if p[n+1]>p[n]:
            s+=(p[n+1]-p[n])-1
        else:
            s+=(p[n]-p[n+1])-1
    print(s)
