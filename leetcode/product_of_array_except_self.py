nums=list(map(int,input().split()))
a=len(nums)
c=[]
for i in range(len(nums)):
    q=nums[:i]+nums[i+1:]
    z=1
    for j in q:
        z*=j
    c.append(z)
print(c)


