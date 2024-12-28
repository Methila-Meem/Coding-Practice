24. Find the Intersection of Two Strings

Question: Find the characters common between two strings.

Hint: Use a hash map to count characters in one string and check for matches in the other.

Sample Input: "abcdef", "acdfg"

Sample Output: ["a", "c", "d", "f”]



def intersectTwoString(arr1,arr2):

	arr3=arr1.intersection(arr2)
	arr3=list(arr3)
	
	return arr3


arr1=input("Enter first string: ")
Arr1=set(arr1)
arr2=input("Enter second string: ")
Arr2=set(arr2)
 
print(intersectTwoString(Arr1, Arr2))










