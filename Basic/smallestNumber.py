25. Find the Smallest Number in an Array (Simplified)

Question: Given an array of integers, find the smallest number.
Hint: Iterate through the array, keeping track of the current smallest number.
Sample Input: [5, 2, 8, 1, 9]
Sample Output: 1


def findSmallest(num):
	
	min=num[0]
	
	for n in num:
		if n<num:
			min=num

	return num


inputNum=input("Enter elements")
number=list((map(int, inputNum.split())

print(findSmallest(number))
