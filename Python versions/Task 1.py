sentence = input("Enter sentence: \n>") 
sentence = sentence.lower()
sentencelist = sentence.split() 
search = input("Word to find:\n>") 
search = search.lower()
position = [i for i, found in enumerate(sentencelist) if found == search]
if len(position) >1: plural = "s"
else:
    plural = "" 
if any(n in position for n in range(0, 9999999)):
    print("The word,", search, ", was found at position"+ plural, position, ".")
else:
    print("The word", search, "wasn't found.")
input()

