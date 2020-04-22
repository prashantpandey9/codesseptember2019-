for j in range(int(input())):
    i=['a','e','i','o','u']
    g=input()
    s=0
    for j in g:
        if j in i:
            s+=1
    print(s)
