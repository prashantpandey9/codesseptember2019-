i=int(input())
s=""
sp=i-1
for j in range(i):
        s+=' '*sp
        sp-=1
        for k in range(j,j*2+1,1):
            s+=str(k+1)
        for l in range(j+1,j+2,1):
            s+=str(l)
        print(s)
        s=""
        
