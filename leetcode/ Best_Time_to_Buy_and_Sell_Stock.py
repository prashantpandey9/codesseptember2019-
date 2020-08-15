prices=list(map(int,input().split()))
##q=[]
##ma=0
##for n in range(len(prices)):
##    r=prices[n+1:]
##    if len(r)!=0 and ma<max(r)-prices[n]:
##        ma=max(prices[n+1:])-prices[n]
##print(ma)

if not prices:
    print(0)
        
minPos = 0
maxPos = 0
diff = 0
newMinPos = 0
for i in range(1, len(prices)):
    if prices[i] > prices[maxPos]:
        maxPos = i
        diff = prices[maxPos] - prices[minPos]
            
    if prices[i] < prices[newMinPos]:
        newMinPos = i
        
    if prices[i] - prices[newMinPos] > diff:
        minPos = newMinPos
        maxPos = i
        diff = prices[i] - prices[newMinPos]

print(diff)
