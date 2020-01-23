l=input()
k=''
for n in range(0,len(l),8):
    m=chr(int(l[n:9],2))
    k+=m
    print(n,m)
print(k)
    
