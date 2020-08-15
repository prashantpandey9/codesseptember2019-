for x in range(int(input())):
    s =  input()
    c=0
    for i in range(len(s)-1):
        if(((abs(ord(s[i])-ord(s[i+1]))) == 1) or (((abs(ord(s[i])-ord(s[i+1]))) == 25))):
            c+=1
    if(c==(len(s)-1)):   
        print("YES")
    else:
        print("NO
