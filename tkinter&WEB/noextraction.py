for n in range(int(input())):
    sss=list(map(int,input().split()))
    r=sss[1]
    l=list(map(int,input().split()))
    i=sss[0]    
    r=r%i
    s=l[r:i]+l[0:r]
    for n in s:
        print(n,end=" ")
    print()
"""
s=input()
r=0
n=0
for i in s:
    if ord(i)>=48 and ord(i)<=57:
        if r==0:
            n+=1k
            r=1
        continue
    print('n',n)
    r=0
print(n)
"""
