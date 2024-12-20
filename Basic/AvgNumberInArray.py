# Calculate the Average of Numbers in an Array
#
# 30. Calculate the Average of Numbers in an Array
# Question: Given an array of numbers, calculate the average.
# Hint: Sum all the numbers in the array and divide by the number of elements. Be mindful of potential division by zero if the array is empty.
# Sample Input: [2, 4, 6, 8]
# Sample Output: 5
# Update

def calculateAVG(Array, length):
    total = 0
    for item in Array:
        total += item

    average = total // length
    return average


inArray = input("Enter elements: ")
Array = list(map(int, inArray.split()))
length = len(Array)

if length == 0:
    print("Array has no numbers.")
else:
    print(calculateAVG(Array, length))
