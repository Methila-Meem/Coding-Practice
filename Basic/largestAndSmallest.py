11. Find the Largest and Smallest Numbers in an Array
Question: Write a program to find the largest and smallest numbers in an array.
Hint: Iterate through the array, updating the minimum and maximum values as you go.
Sample Input: [3, 5, 1, 8, 2, 7]
Sample Output: Largest: 8, Smallest: 1


in_arr=input("Enter the elements: ")
arr=list(map(int, in_arr.split()))

print("The elements are: ", arr)
	
min=arr[0]
max=arr[0]

for x in arr:
    if x<min:
        min=x
    if x>max:
        max=x
	
print(f"Largest number {max}, smalllest number {min}")	
	
	
	
	
	
