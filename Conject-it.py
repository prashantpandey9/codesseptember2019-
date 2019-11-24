a=int(input())
for h in range(a):
    s=int(input())
    while s!=1:
        if s%2==0:
            s=s/2
        else:
            s=(3*s)+1
    if s==1:
        print("YES")
    else:
        print("NO")
