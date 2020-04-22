for _ in range(int(input())):
    n,t=map(int,input().split())
    p=t
    s=list(input())
    for i in range(0,n):
        if s[i].isalpha():
            t=t%26
            if s[i].isupper():
                s[i]=chr(((ord(s[i])+t-65)%26)+65)
            elif s[i].islower():
                s[i]=chr(((ord(s[i])+t-97)%26)+97)
        elif s[i].isdigit():
            
            s[i]=chr(((ord(s[i])+p-48)%10)+48)
            
    print("".join(s))
