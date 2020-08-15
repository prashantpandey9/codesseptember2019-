def ispoly(s):
    q=s.pop(s.index(max(s)))
    u=sum(s)
    if q<u:
        print("Yes")
    else:
        print("No")
    
for n in range(int(input())):
    f=int(input())
    s=list(map(int,input().split()))
    ispoly(s)    
