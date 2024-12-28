# 13. Check if Two Strings are Anagrams
# Question: Write a function to check if two strings are anagrams of each other.
# Hint: Sort both strings and compare them, or use a hash map to count character frequencies.
# Sample Input: "listen", "silent"
# Sample Output: true


def isAnagrams(string1, string2):
    
	if len(string1)!=len(string2):
		return False
	string1=string1.lower()
	string2=string2.lower()
	counter = dict()
	
	for char in string1:
		if char in counter:
			counter[char]+=1
		else:
			counter[char]=1
		
	for char in string2:
		if char not in counter:
			return False
		else:
			counter[char]-=1
		if counter[char]<0:
			return False
	for count in counter.values():
		if count != 0:
			return False
	
	return True

str1=input("Enter the first string: ")
str2=input("IEnter the second string: ")
print("Is the words anangrams: ", isAnagrams(str1,str2))
