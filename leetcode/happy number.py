def isHappy(n): 
    f=n
    jj=set()
    jj.add(n)
    while s!=1:
        s=sum([int(j)**2 for j in str(f)])
        if s==1:
            return True
        elif s in jj:
            return False
        else:
            jj.add(s)
    return True
