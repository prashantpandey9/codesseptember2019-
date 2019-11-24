a=int(input())
a=str(a)
s1=0
s2=0
for i in a:
    i=int(i)    
    if i%2==0:
        s1+=i
    else:
        s2+=i
print(s1,s2)
        

