k=list(map(int,input().split()))
s,mi,ma=k[0],k[1],k[2]
y=s
r=((s//ma)+1)
l=[mi]*r
s=s-(mi*r)
for n in range(r):
    k=ma-l[n]
    if s>k:
        s=s-k
        l[n]+=k
    else:
        ee=l[n]+s
        if (ee)<mi:
            break
        else:
            l[n]+=s
            break
mm=l[::-1]
if sum(l)==y:
    print("YES")
    for ss in range(r):
        print(mm[ss],end=" ")
else:
    print("NO")
