"""
comb=0
j,k=input().split()
j,k=int(j),int(k)
while(j!=0 and k!=0):
    if(j>=k):
        k-=1
        j-=2
        if(j>=0 and k>=0):
            comb+=1
    else:
        k-=2
        j-=1
        comb+=1
print(comb)
"""
comb=0
j,k=input().split()
j,k=int(j),int(k)
c=(j+k)//3
if(c>j or c>k):
    if (a>b):
        print(k)
    else:
        print(j)
else:
    print(c)
