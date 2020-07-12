for i in range(int(input())):
    f=list(map(int,input().split()))
    s=list(map(int,input().split()))
    k=f[0]
    for n in s:
        k=k&n
    if k==0:
        print("Yes")
    else:
        print("No")
