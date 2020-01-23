N = int(input())
data = [int(x) for x in input().split()]
o=''
for j in data:
    i=j%10
    l=str(i)
    o+=l
m=int(o)
if m%10==0:
    print("Yes")
else:
    print("No")
