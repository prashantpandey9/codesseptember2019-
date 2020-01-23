a=int(input())
f=list(map(int,input().split()))
mi=-2147483648
ma=f[0]
for j in f:
    if j>ma:
        mi=ma
        ma=j
print(mi)
