6. Validate Parentheses

Question: Check if a string containing parentheses is valid. A string is valid if all open parentheses are closed in the correct order.

Sample Input: "({[()]})"

Sample Output: true

def matchParentheses(string):
	
	mathingPairs={"(":")", "{":"}", "[":"]"}
	stack=[]
	
	for x in string:
		if x in mathingPairs.values():
			stack.append(x)
		elif x in mathingPairs.keys():
			if not stack of stack[-1]!=matching[char]:
				return False
		stack.pop()
	return not stack

Sent=input("Enter the string:") 

print("String of parentheses is valid? ", matchParentheses(Sent))



