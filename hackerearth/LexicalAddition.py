a=list(map(int,input().split()))
n=a[2]
m=a[1]
s=a[0]
j=[]
for n in range(n,m+1,-1):
    if(s%n>=m and s//n ):
        p=str(n)*s//n
        j.append(p)
    else:
        p=str(n)*s//n
        j.append(p)
print(j) 
