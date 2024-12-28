16. Count Vowels and Consonants in a String
Question: Write a function to count the number of vowels and consonants in a string.
Hint: Iterate through the string and check each character against vowel and consonant sets.
Sample Input: "automation"
Sample Output: Vowels: 5, Consonants: 5

Solutn 1_________________

def countVowels(word):
	
	word=word.lower()
	count=0
	vSet={"a", "e", "i", "o", "u"}
	
	for w in word:
		if w in vSet:
			count+=1
			
	return count


inWord=input("Enter the word: ")

vowels=countVowels(inWord)
consonant=len(inWord)- vowels

print(f"Vowels: {vowels}, Consonants: {consonant}")

Solutn 1_________________

def countVowels(word):
	
	word=word.lower()
	vCount=0
	cCount=0
	vSet={"a", "e", "i", "o", "u"}
	
	for w in word:
	   if w.isalpha():
	       if w in vSet:
	           vCount+=1
	       else:
	           cCount+=1
			
	return vCount, cCount


inWord=input("Enter the word: ")

vowel, consonant =countVowels(inWord)

print(f"Vowels: {vowel}, Consonants: {consonant}")








