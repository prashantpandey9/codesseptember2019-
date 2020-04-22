for j in range(int(input())):
    f=input()
    matrix = [[int(input()) for j in range(2)] for i in range(10)]
    left=0
    right=0

    for j in matrix:
        
        if j[0]==1: #right
            right+=j[1]
        elif j[0]==0: #left
            left+=j[1]
        else:
            pass
    shift=left-right
    if shift>0:
        shift=shift%len(f)
        lshift=f[0:shift]
        rshift=f[shift:]
        print(rshift+lshift)
    elif shift<0:
        shift=-shift
        shift=shift%len(f)
        lshift=f[0:len(f)-shift]
        rshift=f[len(f)-shift:]
        print(rshift+lshift)

    else:
        print(f)
