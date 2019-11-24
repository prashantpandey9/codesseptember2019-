n=int(input())
a=list(map(int,input().split()))
q=int(input())
u=[0]*1001
for j in a:
    u[j]+=1
for r in range(q):
    h=int(input())
    if h not in a:
        print("NOT PRESENT")
    else:
        if u[h]==0:
            print("NOT PRESENT")
        else:
            print(u[h])
            
