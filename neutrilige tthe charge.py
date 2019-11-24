def count(test_str):#function to find occurence 
    res = {i : test_str.count(i) for i in set(test_str)}   
    o=list(res.values())
    print(res,o)
    g=[]
    for n in o:
        print("n",n)
        if n%2==0:
            pass
        else:
            g.append(n)
    print(g)
        
    for m in g:
        print(res[m])
    print()
a=int(input())
k=input()
count(k)
