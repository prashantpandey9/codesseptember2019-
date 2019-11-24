"""
def findMinimumAdjacentSwaps(arr, N) :  
	visited = [False] * (N + 1) 
	minimumSwaps = 0
	for i in range(2 * N) : 
		if (visited[arr[i]] == False) : 
			visited[arr[i]] = True
			count = 0

			for j in range( i + 1, 2 * N) : 
				if (visited[arr[j]] == False) : 
					count += 1 
				elif (arr[i] == arr[j]) : 
					minimumSwaps += count 
		
	return minimumSwaps
o=[0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for n in range(int(input())):
    arra =input()
    arr=[3,2,2,1,3,3]
    for n in arr:
        if n in o:
            l.append(o.index(n))
    N = len(arr) 
    N //= 2
    print(findMinimumAdjacentSwaps(arr, N)) 
# Python3 code to print all possible subarrays 
# for given array using recursion 

# Recursive function to print all possible subarrays 
# for given array 
def printSubArrays(arr, start, end): 
	
	# Stop if we have reached the end of the array	 
	if end == len(arr): 
		return
	
	# Increment the end point and start from 0 
	elif start > end: 
		return printSubArrays(arr, 0, end + 1) 
		
	# Print the subarray and increment the starting 
	# point 
	else: 
		rarr[start:end + 1]) 
		return printSubArrays(arr, start + 1, end) 
		
# Driver code 
arr = [4,8,12,16,18] 
printSubArrays(arr, 0, 0) 
"""
"""
from shapely.geometry import Point, Polygon, LineString

n, m = map(int, input().split())
p1 = []
p2 = []

for i in range(n):
    x, y = map(int, input().split())
    p1.append((x, y))

for i in range(m):
    x, y = map(int, input().split())
    p2.append((x, y))

#print(p1, p2)
poly = Polygon(p1)

inside = 0
p3 = []
for i in range(m):
    if Point(p2[i]).within(poly):
        inside += 1
    else: p3.append(p2[i])
ans = 0
#print(inside, p3)
ans += inside * (inside-1) // 2

pLines = []
for i in range(n):
    pLines.append(LineString([p1[i], p1[(i+1) % n]]))
#print(pLines)
l = len(p3)
for i in range(l):
    for j in range(i+1, l):
        line = LineString([p3[i], p3[j]])
        flag = 1
        for k in range(n):
            if line.intersects(pLines[k]):
                flag = 0
                break
        if flag: ans += 1

print(ans)
"""
import string 
import random 
N =int(input())
res = ''.join(random.choices("Y"+"y", k = N)) 
print(str(res)) 
