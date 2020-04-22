for n in range(int(input())):
    a=list(map(int,input().split()))#x and k as list input
    x=a[0]#10
    k=a[1]#23
    d=0#counter
    while True:
        e=str(x)
        w=str(x)[::-1]
        if e==w:
            d+=1
            if d==k:
                break
        x+=1
    print(x)
