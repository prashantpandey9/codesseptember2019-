f=[]
for i in range(int(input())):
    k=input()
    f.append(k)
    if k[::-1] in f:
        print(len(k),k[len(k)//2])
    else:
        f.append(k)
