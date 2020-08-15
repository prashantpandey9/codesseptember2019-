
nums=list(map(int,input().split()))
target=int(input())
d={}
for i in range(0,len(nums)):
    d[nums[i]] = i

for i in range(0,len(nums)):
    if target - nums[i] in d and i!=d[target-nums[i]]:
        print([i,d[target-nums[i]]])
        break  
