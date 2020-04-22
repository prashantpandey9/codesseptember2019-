##def merge(arr, l, m, r): 
##	n1 = m - l + 1
##	n2 = r- m 
##	L = [0] * (n1) 
##	R = [0] * (n2)
##	for i in range(0 , n1): 
##		L[i] = arr[l + i] 
##
##	for j in range(0 , n2): 
##		R[j] = arr[m + 1 + j] 
##	i = 0	
##	j = 0	 
##	k = l	 
##
##	while i < n1 and j < n2 : 
##		if L[i] <= R[j]: 
##			arr[k] = L[i] 
##			i += 1
##		else: 
##			arr[k] = R[j] 
##			j += 1
##		k += 1
##	while i < n1: 
##		arr[k] = L[i] 
##		i += 1
##		k += 1
##	while j < n2: 
##		arr[k] = R[j] 
##		j += 1
##		k += 1
##def mergeSort(arr,l,r): 
##	if l < r: 
##		m = (l+(r-1))//2 
##		mergeSort(arr, l, m) 
##		mergeSort(arr, m+1, r) 
##		merge(arr, l, m, r) 
##
##arr = list(map(int,input().split()))
##n = len(arr) 
##print ("Given array is") 
##for i in range(n): 
##	print ("%d" %arr[i]), 
##mergeSort(arr,0,n-1) 
##print ("\n\nSorted array is") 
##for i in range(n): 
##	print ("%d" %arr[i]),
def msort(array): 
    if len(array)>1: 
        mid=len(array) // 2
        L=array[:mid] 
        R=array[mid:] 
        msort(L)
        msort(R)	
        array.clear() 
        while len(L)>0 and len(R)<0 : 
            if L[0] <= R[0]:
                array.append(L[0])
                L.pop(0)
            else:
                array.append(R[0])
                R.pop(0) 
            for i in L: 
                array.append(i) 
            for i in R:
                array.append(i)
    print(array)
array=list(map(int,input().split()))
print(array)
msort(array)
