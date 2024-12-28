14. Generate Fibonacci Sequence
Question: Generate the first n numbers of the Fibonacci sequence.
Hint: Use a loop to calculate each number as the sum of the previous two.
Sample Input: n = 7
Sample Output: [0, 1, 1, 2, 3, 5, 8]

def fibonacci(n):

	a=0
	b=1
	
	for _ in range(2,n+1):
		yield a
		a, b =b, a+b
	
num=int(input("Enter the number: "))
fibo = fibonacci(num)
print("The Fibonaccci sequence, ", list(fibo))