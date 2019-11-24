a=int(input())
s=0
q=[]
t=list(map(int,input().split()))
for r in t:
    s+=r
    q.append(s)
y=q.pop()
h=str(y)
s1=0
for j in h:
    k=int(j)
    s1+=k
rr=0
if s1>10:
    s1=str(s1)
    for l in s1:
        t=int(l)
        rr+=t
    print(rr)
else:
    print(s1)
        
    
