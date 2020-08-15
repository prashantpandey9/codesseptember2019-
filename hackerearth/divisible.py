def solve (A):
    # Write your code here
    p=''
    AA=list(A)
    u=len(AA)
    r1=[]
    r2=[]
    for h in range(1,u//2+1):
        r1.append(AA[h-1])
        r2.append(AA[-h])
    r2.reverse()
    for j in r1:
        i=str(j)
        t=i[:1]
        p+=t
    for j in r2:
        oo=j%10
        ll=str(oo)
        p+=ll
    p=int(p)
    if p%11==0:
        return("OUI")
    else:
        return("NON")
N = int(input())
A = map(int, input().split())

out_ = solve(A)
print (out_)
