def w(a,b):
    if a==0 and b==0:
        return a^b
    if a==0 and b==1:
        return a^b
    if a==1 and b==0:
        return a^b
    if a==1 and b==1:
        return a^b
    
for j in range(int(input())):
    f=list(map(int,input().split()))
    c=0
    for j in range(2):
        for f in range(2):
            for d in range(2):
                if w(j,w(f,d))==w(w(j,f),d):
                    c+=1
    if c==8:
        print("Yes")
    else:print("No")
                    
    
