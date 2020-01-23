
n,q=map(int,input().split())
d=list(map(int,input().split()))
for h in range(q):
    f=list(map(int,input().split()))
    if f[0]==1:
        
        x=f[1]
        if d[x-1]==0:
            d[x-1]=1
        else:
            d[x-1]=0
    elif f[0]==0:
        s=''
        for j in range(f[1],f[2]+1):
            s+=str(d[j-1])
        ee=int(s,2)
        if ee%2==0:
            print("EVEN")
        else:
            print("ODD")


"""
e=1
for n in range(5):
    for  j in range(n):
        print(e,end='')
        e+=1
    print()
"""
