9. FizzBuzz

Question: Print numbers from 1 to n. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for multiples of both, print "FizzBuzz".

Hint: Use modulo % to check divisibility.

Sample Input: 15

Sample Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

number=int(input("Enter the nth number: "))
Arr=[]

for x in range(1, number+1):
    if x%3==0 and x%5==0:
        Arr.append("FizzBuzz")
    elif x%5==0:
        Arr.append("Buzz")
    elif x%3==0:
        Arr.append("Fizz")
    else:
        Arr.append(x)
        
print(Arr)

