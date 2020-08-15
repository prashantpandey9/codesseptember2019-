"""
u=int(input())
r=list(map(int,input().split()))
for j in r:
    if j%4==0 :
        print(j//4)
    elif j//4==0:
        print(-1)
    else:
        print(j//4)
"""
"""#2
u=int(input())
r=list(map(int,input().split()))
s=0
for j in r:
    if j%2==0:
        s+=j
    elif(j%3==0):
        s+=j
print(s)
"""
r=list(map(int,input().split()))
r.pop(0)
y=len(r)
o=[0]*y
m=0
t=1
for n in range(len(r)):
    if r[n]<0:
        o[t]=r[n]
        t+=2
    else:
        o[m]=r[n]
        m+=2
for j in o:
    print(j,end=' ')
