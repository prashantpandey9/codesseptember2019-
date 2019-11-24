a=int(input())
b=0
for q in range(a):
    b=0
    e,s=input().split()
    e,s=int(e),int(s)
    u=e
    while True:
        y=u//s
        f=e%s
        b+=y
        u=y+f
        if u<s:
            break
    print(b)
    
    
    
    
    
