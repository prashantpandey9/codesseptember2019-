for n in range(int(input())):
    i=input()
    st=''
    for d in i:
        
        if d==' ':
            st+="$"
        else:
            st+=str((1+(ord(d)%97)))
    print(st)
