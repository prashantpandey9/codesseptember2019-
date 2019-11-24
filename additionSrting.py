"""a=int(input())
k=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for j in range(a):
    h=input()
    i=h[::-1]
    o=[]
    for j in h:
        if j in k:
            o.append(k.index(j)+1)
    p=o[::-1]
    l=[]
    for n in range(0,len(h)):
        l.append(p[n]+o[n])
    qq=''
    for n in l:
        if n>26:
            n=n-26
            i=k[n-1]
            qq+=str(i)
        else:
            i=k[n-1]
            qq+=str(i)
    print(qq)
    
"""#Implement
"""
r=int(input())
for n in range(r):
    a=input()
    j=a[::-1]
    rw=''
    for n in range(len(a)):
        r=ord(a[n])-97
        y=ord(j[n])-96
        t=((r+y)%26)+97
        m=chr(t)
        rw+=m
    print(rw)
"""
d=int(input())
for j in range(d):
    s=input()
    for n in range(len(s)):
        print(chr(((ord(s[n])-97+ord(s[len(s)-1-n])-96)%26)+97),end='')
