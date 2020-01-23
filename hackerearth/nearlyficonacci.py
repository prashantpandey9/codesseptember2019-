"""
aa=int(input())
def hcf(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcf(b,a%b)
for n in range(aa):
    a,b,n=input().split()
    a,b,n=int(a),int(b),int(n)
    d=hcf(a,b)
    print(d)
    
"""
# A O(n) solution for finding rank of string 
MAX_CHAR=256; 

# all elements of count[] are initialized with 0 
count=[0]*(MAX_CHAR + 1); 

# A utility function to find factorial of n 
def fact(n): 
	return 1 if(n <= 1) else (n * fact(n - 1)); 

# Construct a count array where value at every index 
# contains count of smaller characters in whole string 
def populateAndIncreaseCount(str): 
	for i in range(len(str)): 
		count[ord(str[i])]+=1; 

	for i in range(1,MAX_CHAR): 
		count[i] += count[i - 1]; 

# Removes a character ch from count[] array 
# constructed by populateAndIncreaseCount() 
def updatecount(ch): 

	for i in range(ord(ch),MAX_CHAR): 
		count[i]-=1; 

# A function to find rank of a string in all permutations 
# of characters 
def findRank(str): 
	len1 = len(str); 
	mul = fact(len1); 
	rank = 1; 


	# Populate the count array such that count[i] 
	# contains count of characters which are present 
	# in str and are smaller than i 
	populateAndIncreaseCount(str); 

	for i in range(len1): 
		mul = mul//(len1 - i); 

		# count number of chars smaller than str[i] 
		# fron str[i+1] to str[len-1] 
		rank += count[ord(str[i]) - 1] * mul; 

		# Reduce count of characters greater than str[i] 
		updatecount(str[i]); 

	return rank; 

# Driver code 
str =input(); 
print(findRank(str)); 

# This is code is contributed by chandan_jnu 
