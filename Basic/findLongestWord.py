15. Find the Longest Word in a Sentence
Question: Given a sentence, find the longest word.
Hint: Split the sentence into words and compare lengths.
Sample Input: "QA automation is challenging but rewarding"
Sample Output: "challenging"

def findLongestWord(sent):
	
	wordlist= list(sent.split())
	longestword = ""
	
	for x in wordlist:
		if len(x)>len(longestword)
			longestword = word
	
	return longestword
	
sentence=input("Enter the sentence: ")
print("Longest word is, ", findLongestWord(sentence))
