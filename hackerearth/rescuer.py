import math 
def distance(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)*1.0)
a=list(map(int,input().split()))
print("%.5f"%distance(a[0],a[1],a[2],a[3])) 
