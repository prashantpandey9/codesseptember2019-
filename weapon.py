for n in range(int(input())):
    a=0
    for d in range(int(input())):
        s=input()
        a=a^int(s,2)
    print(bin(a)[2:].count('1'))
