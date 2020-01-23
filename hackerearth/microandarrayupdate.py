for i in range(int(input())):
    s=list(map(int,input().split()))
    a=list(map(int,input().split()))
    n=s[0]#for no of elements in array
    k=s[1]#no K
    q=0
    """while(min(a)!=k):
        for n in range(len(a)):
            a[n]=a[n]+1
        q+=1
    print(q)
    """
    j=min(a)
    r=k-j
    if(r>0):
        print(r)
    else:
        print(0)
