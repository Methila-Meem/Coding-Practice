27. Check if a Number is Even or Odd

Question: Write a function to determine if a given number is even or odd.
Hint: Use the modulo operator (%). If number % 2 == 0, it's even.
Sample Input: 7
Sample Output: "Odd"


def oddEven(num):

	if num%2==0:
		return "Even"
	else:
		return "Odd"


number = int(input("Enter number: "))

print(oddEven(number))










