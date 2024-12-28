19. Find the Second Largest Element in an Array

Question: Write a program to find the second largest number in an array.

Hint: Iterate through the array while maintaining the largest and second-largest elements.

Sample Input: [10, 5, 20, 8]

Sample Output: 10


def secondLargest(arr):
	n=len(arr)
	for i in range(n):
		for j in range(0,n-i-1):
			if arr[j]<arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				
	
	
	return arr[1]
	
inputArr=input("Enter elements: ")
arr=list(map(int, inputArr.split()))

print(secondLargest(arr))
