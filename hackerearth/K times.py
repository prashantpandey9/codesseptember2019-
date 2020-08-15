a=int(input())
o=list(map(int,input().split()))
p=[0,1,2,3,4,5,6,7,8,9]
k=int(input())
y=[0]*10
for n in o:
    if n in p:
        y[n-1]+=1
for l in y:
    if k==l:
        print(y.index(l)+1)
        break
    
    
