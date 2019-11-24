for j in range(int(input())):
    s=input()
    sd=input()
    ks=''
    sk=''
    if len(s)>=len(sd):
        k=len(s)
        ks=s
        sk=sd
    else:
        k=len(sd)
        ks=sd
        sk=s
    for n in range(k):
        if ks[n] in sk:
            print("Yes")
            break
    else:
        print("No")
