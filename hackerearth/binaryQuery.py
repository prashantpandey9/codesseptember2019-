"""
n,q=map(int,input().split())
d=list(map(str,input().split()))
for h in range(q):
    f=list(map(str,input().split()))
    if f[0]=='1':
        x=int(f[1])
        if d[x-1]=='0':
            d[x-1]='1'
        else:
            d[x-1]='0'
    elif f[0]=='0':
        s=''
        a=d[int(f[1])-1:int(f[2])]
        s=s.join(a)
        s=int(s)
        if s&==0:
            print("EVEN")
        else:
            print("ODD")
"""
N , Q = list(map(int , input().split()))
n = list(map(int , input().split()))
cal = 0
sum1 = 0
for i in range(Q):
    inp = list(map(int , input().split()))
    if(inp[0]==1):
        if(n[inp[1]-1]==0):
            n[inp[1]-1] = n[inp[1]-1]+1
        else:
            n[inp[1]-1] = n[inp[1]-1]-1
    else:
        if(n[inp[2]-1]==1):
            print("ODD")
        else:
            print("EVEN")
