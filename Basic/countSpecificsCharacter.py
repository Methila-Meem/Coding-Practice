26. Count Occurrences of a Specific Character

Question: Given a string and a character, count how many times the character appears in the string.
Hint: Iterate through the string and increment a counter if the character matches.
Sample Input: String: "hello", Character: 'l'
Sample Output: 2


def countCharacter(string, ch):
	
	counter= 0 
	
	for s in string: 
		if s==ch:
			counter += 1
			
	return counter


string=input("String: ")
char=input("Character: ")

print(countCharacter(string, char))