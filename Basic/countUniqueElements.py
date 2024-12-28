21. Count Unique Elements in an Array

Question: Count the number of unique elements in an array.

Hint: Use a hash set to store unique elements as you iterate through the array.

Sample Input: [1, 2, 2, 3, 4, 4]

Sample Output: 4


def uniqueElementCount(arr):
	
	unique=set()
	for x in arr:
		if x not in count:
			unique.append(x)
			
	count=len(unique)
	
	return count


inputArr=input("Enter elements: ")
arr=list(map(int, inputArr.split()))

print(uniqueElementCount(arr))








