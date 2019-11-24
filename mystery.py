"""
def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
while True:
    try:
        j=int(input())
        DecimalToBinary(j)
    except ValueError:
        break
"""
def decimalToBinary(n):  
    return bin(n).replace("0b", "")
g=[]
while True:
    try:
        j=int(input())
        g.append(list(decimalToBinary(j)))
    except EOFError:
        break
for n in g:
    print(n.count("1"))
