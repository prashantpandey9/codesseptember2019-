nums=list(map(int,input().split()))
d={}
for i in range(0,len(nums)):
    d[nums[i]] = i
for j in range(len(nums)):
    if j!=d[nums[j]]:
        print(True)
        break
else:
    print(False)
