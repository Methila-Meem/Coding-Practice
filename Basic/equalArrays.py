20. Check If Two Arrays are Equal

Question: Write a program to check if two arrays contain the same elements (order does not matter).

Hint: Sort both arrays and compare element by element.

Sample Input: arr1 = [1, 2, 3], arr2 = [3, 1, 2]

Sample Output: true


def arraysAreequal(arr1,arr2):

	n1=len(arr1)
	for i in range(n1):
		for j in range(0,n1-i-1):
			if arr1[j]<arr1[j+1]:
				arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
				
	n2=len(arr2)
	for i in range(n2):
		for j in range(0,n2-i-1):
			if arr2[j]<arr2[j+1]:
				arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
				
	if arr1!=arr2:
		return False
				
	
	
	return True
	
inputArr1=input("Enter elements for array 1: ")
arr1=list(map(int, inputArr1.split()))
inputArr2=input("Enter elements for array 2: ")
arr2=list(map(int, inputArr2.split()))

print(arraysAreequal(arr1,arr2))















