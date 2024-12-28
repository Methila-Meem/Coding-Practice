17. Remove Duplicates from a Sorted Array
Question: Write a program to remove duplicates from a sorted array in place, such that each element appears only once. Return the new length of the array.
Hint: Use two pointers: one for the current position and one to track unique elements.
Sample Input: [1, 1, 2, 3, 3, 4, 5, 5]
Sample Output: Length: 5, Array: [1, 2, 3, 4, 5]


def removeDuplicate(arr):
	
	seen=set()
	sortArr=[]
	
	for x in arr:
		if x not in seen:
			seen.add(x)
			sortArr.append(x)
			
	return sortArr


inArray=input("Enter elements: ")
arr=list(map(int, inArray.split()))
newArray=removeDuplicate(arr)

print(f"Lengteh: {len(newArray)}, Array: {newArray}")
