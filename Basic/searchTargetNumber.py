10. Write a Binary Search Algorithm

Question: Implement binary search to find if a target exists in a sorted array.

Hint: Use two pointers, one for the start and one for the end, and repeatedly divide the array in half.

Sample Input: [1, 2, 3, 4, 5, 6, 7], target = 4

Sample Output: true

def findTarget(arr, n):
    for x in arr:
        if x==n:
            return True
    return False

arr_input=input("Enter elements for arrary incuding spaces:") 
Arr=list(map(int, arr_input.split()))
N=int(input("Enter target number: "))

print("Target found?", findTarget(Arr, N))