"""
x,k=input().split()
k=int(k)
o=x[k+1:]
print(o)
v="9"*(k+1)
o=v+o
print(o)
"""
x,k=input().split()
k=int(k)
u=''
h=k
if k==0:
    print(x)
else: 
    for w in x:
        if w=='9':
            u+=w
        else:
            u+='9'
            h-=1
        if h<1:
            break
    f=len(u)
    ww=x[f:]
    u+=ww
    print(u)
