import math
n=int(input())
s=0
m=(n*(n+1))//2
for c in range(1,n+1):
    l=((c*j)//(math.gcd(c,j)**2))%(10**9+7)
print(s)
