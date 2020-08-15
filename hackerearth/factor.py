"""#1
a=int(input())
s=0
for h in range(1,a):
    if a%h==0:
        s+=h
print(s)
"""
"""#2
a=int(input())
fact=1
for j in range(1,a+1):
    fact*=j
print(fact)
"""
#3
a=int(input())
u=str(a)
yy=len(u)
s=0
for h in range(yy):
    g=u[(yy-1)-h]
    g=int(g)
    s+=(2**h)*g
print(s)

"""#4
a=input()
u=''
count=1
u+=a[0]
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count+=1
    else:
        if count>1:
            u+=str(count)
        u+=a[i+1]
        count=1
print(u)
"""
"""#5
a=input()
u=''
count=1
u+=a[0]
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count+=1
    else:
        if count>1:
            pass
        u+=a[i+1]
        count=1
print(u)
"""
"""#6
a=list(map(int,input().split()))
a.pop(0)
a=sorted(a)
i=a[0]
for n in a:
    if i==n:
        i+=1
        pass
    else:
        print("false")
        break
else:
    print("true")
"""
"""#7
o=int(input())
p=["A","E","I","O","U","a","e","i","o","u"]
for j in range(o):
    i=input()
    count=0
    for n in i:
        if n in p:
            count+=1
    print(count)
"""
#a=int(input())
