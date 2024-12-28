def firstUniqueLetter(string):
    newList=list()
    for i in string:
        if i not in newList:
            return newList.add(i)
    return newList[0]

i_string=input("Enter the string:")

print("The first unique letter is ", firstUniqueLetter(i_string))
