w=int(input())
a=0
b=7
for j in range(w):
    r=int(input())
    l=abs(a-r)
    k=abs(b-r)
    if(l<k):
        print("A")
        a=r
    elif(k>l):
        print("B")
        b=r
    else:
        print("A")
        a=r
