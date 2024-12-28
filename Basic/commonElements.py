8. Find the Intersection of Two Arrays

Question: Find the common elements between two arrays.

Hint: Use a hash set to store elements of one array and check against the second array.

Sample Input: [1, 2, 3, 4], [3, 4, 5, 6]

Sample Output: [3, 4]

def matchArray(ar1, ar2):

	ar3=ar1.intersection(ar2)

	return ar3

arr1=input("Enter first array: ")
Arr1=set(map(int, arr1.split()))
arr2=input("Enter second array: ")
Arr2=set(map(int, arr2.split()))
 
print("The common elements between two arrays are: ", matchArray(Arr1, Arr2))