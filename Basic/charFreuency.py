# 7. Count the Frequency of Characters in a String
#
# Question: Given a string, count the frequency of each character.
#
# Sample Input: "automation"
#
# Sample Output: {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}

def charFrequency(string):
	counter={}
	for x in string:
		counter[x]=counter.get(x, 0)+1
		
	return counter
	
print("The frequency of each characters: ")