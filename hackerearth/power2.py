import math
c=0
for h in range(int(input())):
    j=int(input())
    hh=math.log2(j)
    hh=math.floor(hh)
    m=2**hh
    if m==j:
        c+=1
print(c)
