"""
def dd(f):
    while True:
        if f%2==0:
            f=f/2
            if f/2==1:
                print("Yes")
                break
        else:
            print("No")
            break
    
for n in range(int(input())):
    f=int(input())
    fs=list(map(int,input().split()))
    ss=0
    for n in fs:
        if n>0:
            ss+=n
    if ss%2==0:
        dd(ss)
"""
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for i in a:
        if i>0:
            x+=i
    binary=bin(x)[2:]
    if binary.count('1')==1:
        print('Yes')
    else:
        print('No')

