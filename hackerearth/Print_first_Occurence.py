for h in range(int(input())):
    f=input()
    s=''
    for j in f:
        if j not in s:
            s+=j
    print(s)
