def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i+1] 
    arr[n-1] = temp
    return arr
def maxSubArraySum(a,size): 
    max_so_far =a[0] 
    curr_max = a[0] 
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max)    
    return max_so_far
for h in range(int(input())):
    g=int(input())
    arr=list(map(int,input().split()))
    e=arr
    r=arr[0]
    while arr==e:
        print(maxSubArraySum(arr,g),end=' ')
        arr=leftRotatebyOne(arr,g)
        if arr[0]==r:
            break
        
        
