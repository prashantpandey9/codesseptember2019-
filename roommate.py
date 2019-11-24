"""for j in range(int(input())):
    f=int(input())
    d=2
    s=1
    e=1
    aa=[0,1]
    for n in range(f):
        xx=d*s
        if f<=xx:
            aa.append(xx)
            break
        else:
            aa.append(xx)
            s=xx
    for n in range(len(aa)):
        if f==aa[n]:
            print(e)
        elif f<aa[n] and f>aa[n-1]:
            print(e+(f-aa[n-1]))
        else:
            pass
            
"""
for i in range(int(input())):
    f=int(input())
    print(bin(f).count("1"))
    
