"""#1
n=int(input())
t=65
for j in range(1,n+1):
    for c in range(j):
        print(chr(t),end='')
    t+=1
    print()
"""


"""#2
f=int(input())
o=0
for j in range(f,0,-1):
    o+=1
    for k in range(1,j+1):
        if o%2==0:
            print("0",end='')
        else:
            print("1",end='')
    print()
 """   
"""#3       
a=int(input())
h=[int(x) for x in input().split()]
i=max(h)
w=[0]*i*a
for j in h:
    w[j]+=1
n=max(w)
print(w.index(n))
"""
#4
"""a=int(input())
y=[int(x) for x in input().split()]
i=len(y)
s1=0
s2=0
for l in range(i):
    s1=0
    s2=0
    for n in range(l):
        s1+=y[n]
    for d in range(l+1,i):
        s2+=y[d]
    if s1==s2:
        print(l)
        break
else:
    print(-1)
"""
        
