"""# Python code to find frequency of each word 
def freq(str,n):
    str = str.split()		 
    str2 = [] 
    s=[]
    for i in str:
        if i not in str2:
            str2.append(i) 
    for i in range(0, len(str2)):
        s.append(tuple(str2[i],str.count(str2[i])))
    for n in range(n):
        print(s[n])

freq("the the the quick quick brown brown brown brown fox jumps jumps over",1)	    

"""
def step_fib(k):
    def f(n,k):
        s=k
        f1=0
        f2=1
        if(n<1):
            return
        for x in range(0,n):
            if s==k:
                print(f1,end=",")
                s=0
            next=f1+f2
            f1=f2
            f2=next
            s+=1
    return f(n,k)
#step_fib(13)
"""
def get_digits_product(n):
    d=str(n)
    p=1
    for n in d:
        j=int(n)
        p*=j
    return p
m=int(input())
print(get_digits_product(m))
"""
