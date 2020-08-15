def seven_segment(x):
    orig = x.split(' ')
    orig = [int(i) for i in orig]
    sev_seg = [6, 2, 5, 5,4, 5, 6, 3, 7, 6]
    k = []
    s = 0
    for i in orig:
        if i == 0:
            k.append(6)
        elif i == 1:
            k.append(2)
        elif i == 2:
            k.append(5)
        elif i == 3:
            k.append(5)
        elif i == 4:
            k.append(4)
        elif i == 5:
            k.append(5)
        elif i == 6:
            k.append(6)
        elif i == 7:
            k.append(3)
        elif i == 8:
            k.append(7)
        elif i == 9:
            k.append(6)
        elif i > 9:
            for n in str(i):
                s += sev_seg[int(n)]
 
            k.append(s)
            s = 0
 
    return orig[k.index(min(k))]
 
 
 
 
if __name__ == "__main__":
    i = int(input())
    for _ in range(0, i):
        m = int(input())
        L = input()
        print(seven_segment(L))
