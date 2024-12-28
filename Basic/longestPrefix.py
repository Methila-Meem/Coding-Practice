22. Find the Longest Common Prefix

Question: Write a function to find the longest common prefix among an array of strings.

Hint: Compare characters of each string one by one. Stop when a mismatch is found.

Sample Input: ["flower", "flow", "flight"]

Sample Output: "fl"


def findCommonPrefix(strings):
	if not strings: 
		return ""
		
	prefix = strings[0]
	for string in strings: 
		while not string.startswith(prefix):
			prefix = prefix[:-1]
			
		if not prefix:
			return ""
	
	return prefix



inputStrings=input("Enter strings: ")
strings=list(inputStrings.split())

print(findCommonPrefix(strings))







