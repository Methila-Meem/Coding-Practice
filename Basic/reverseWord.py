5. Reverse Words in a String

Question: Given a string, reverse the order of words.

def reverseWord(string):

	normalOrder=list(string.split())
	reverseOrder=normalOrder[::-1]
	reverseOrder=" ".join(reverseOrder)
	
	return reverseOrder

Sent=input("Enter the sentence:") 

print("The reversed words are: ", reverseWord(Sent))