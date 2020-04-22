def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string
for h in range(int(input())):
    n,k=input().split()
    n,k=int(n),int(k)
    d=[]
    for i in range(n+1): 
        o=len(str(base10toN(i,k)))
        d.append(o)
    #print(d)
    print(sum(d))

"""for n in range(int(input())):
    a=int(input())
    b=int(input())
    k=int(input())
    while True:
        print("k",k)
        k-=a
        k+=b
        print("%",k%a)
        if k%a!=b:
            print(k)
            break
        else:
            print("-1")
            break
"""
