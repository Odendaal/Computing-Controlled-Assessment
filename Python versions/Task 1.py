sentence = input("Enter sentence: \n>")  #user enters sentence which is stored in the variable as sentence.
sentence = sentence.lower() #turns the sentence into all lower case to prevent case senstivity.
sentencelist = sentence.split() #splits the sentence into individual words and stores it in this variable as a list.
search = input("Word to find:\n>") #user enters word they wish to find which is also stored as a variable.
search = search.lower() #again, the word the user wishes to search is turned into lower case to match the sentence, avoiding case senstivity.
position = [i for i, found in enumerate(sentencelist) if found == search] #this loop goes through each induvidual word in the sentence list, and see's if it matches with the search variable. The use of enumerate is so that the loop will work throughout the entire sentence, not just stopping at the first word it finds.
if len(position) >1: plural = "s" #used to help the following output make more sense. basically, if the word has been found more than one time, the sentence will say "positions" instead of "position"
else:
    plural = "" #sets the variable plural as nothing so it knows not to add an s on the end of positions.
if not position: #basically, if no positions are found, then output it no word found.
	print("The word", search, "wasn't found.")
else: #self explanitory, if the word was found, output the success, and it's positions.
    print("The word,", search, ", was found at position"+ plural, position, ".")
input() #creates a break so the user can press enter when they wish to close the program.

