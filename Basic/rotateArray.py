12. Rotate an Array
Question: Rotate an array k steps to the right.
Hint: Use slicing to separate and recombine the array.
Sample Input: arr = [1, 2, 3, 4, 5], k = 2
Sample Output: [4, 5, 1, 2, 3]

def rotateToRight(arr,k):
    n=len(arr)
    if n==0:
        return arr
    k=k%n
    arr1=arr[-k:]
    arr2=arr[0:-k]
    arr=arr1+arr2
    return arr

inArr=input("Enter array elements: ")
Arr=list(map(int, inArr.split()))

K=int(input("Enter step number:"))

print(rotateToRight(Arr,K))