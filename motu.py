"""
n=int(input())
patlu=1
motu=2
r=[]
for i in range(1,n//2):
    y=i*patlu
    j=i*motu
    o=y+j
    n-=o
    r.append(y)
    r.append(j)
    if n<0:
        ii=r.pop()
        n+=ii
        if n<0:
            ww=r.pop()
            n+=ww
        break
print(r,)     
if len(r)%2==0:
    print("Motu")
else:
    print("Patlu")
"""
n=int(input())
for i in range(n):
    p=i
    if(n-p>=0):
        n=n-p
    else:
        print("Patlu")
        break
    m=i*2
    if(n-m>0):
        n=n-m
    else:
        print("Motu")
        break
