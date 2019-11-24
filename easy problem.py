'''
n,m=input().split()
n,m=int(n),int(m)
k=[]
for s in range(m):
    f=list(map(int,input().split()))
    k+=f
t=set(k)
print(len(t))
print(list(t))
'''
t = int(input())
for _ in range(t):
    v,e = map(int,input().split())
    d = {}
    for i in range(v):
        d[i] = []
    for i in range(e):
        x,y = map(int,input().split())
        d[x].append(y)
        d[y].append(x)
    print(d)
    """
    s = ''
    for key in d:
        s=''
        s+=str(key)
        for i in range(len(d[key])):
            s+='-> '
            s+=str((d[key])[i])
        print(s)
    """
