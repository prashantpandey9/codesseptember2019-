r=list(map(int,input().split()))
r.pop(0)
p=0
u=len(r)//2
for j in range(u):
    print(r[j],end=' ')
    print(r[j+u],end=' ')
