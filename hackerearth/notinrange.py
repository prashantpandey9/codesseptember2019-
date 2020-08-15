k = (1000000*1000001)//2
t = int(input())
l = []
for _ in range(t):
    x,y = map(int,input().split())
    l.append([x,y])

##print("1",l)
    
l = sorted(l)

#for merging the left limits
for i in range(len(l)-1):
    if(l[i+1][0]<=l[i][1]):
        l[i+1][0] = l[i][1]+1

#for the broken range if l>r
for i in range(len(l)):
    if(l[i][0]>l[i][1]):
        l[i] = 0

#for finding the sum between r and l and then subtract it from the total sum
for i in range(len(l)):
    if(l[i]!=0):
        e = (l[i][1]*(l[i][1]+1))//2
        o = (l[i][0]*(l[i][0]+1))//2
        p = e-o+l[i][0]
        k-=p
print(k)

##import time
##start = time.time()
##from sys import stdin, stdout
##def not_in_range(ranges):
##  end_ = 0
##  t_sum = 0
##  for start in sorted(ranges):
##    print(end_,start,(end_ + start) * (start - 1 - end_) / 2)
##    if start > end_:
##      t_sum += (end_ + start) * (start - 1 - end_) / 2
##    end_ = max(end_, ranges[start])
##  
##  max_num = 10 ** 6
##  t_sum += (end_ + 1 + max_num) * (max_num - end_) / 2
##  return t_sum
##     
##n = int(stdin.readline().strip())
##ranges = {int(num[0]): int(num[1]) for num in (stdin.readline().split() for _ in range(n))}
##print(ranges)
##stdout.writelines(str(int(not_in_range(ranges))))
####end = time.time()
####print(f"Runtime of the program is {end - start}")
