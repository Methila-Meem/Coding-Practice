
def isPalindrome(string):
    normalStr=string.lower()
    reversStr=normalStr[::-1]
    if reversStr==normalStr:
        return True
    else:
	    return False

eStr=input("Enter the string:") 

print("The string is palindrome?", isPalindrome(eStr))