import string 									    #acts like a dictionary so later I can use short phrases which can be lookedup in this
empty = True
while empty is True: 								    #just a while loop to make sure the user actually enters somthing as entering nothing could cause errors..
    sentence = input("Enter sentence (without punctuation): \n>")		    #user enters sentence which is stored in the variable as sentence.
    if not any(word in sentence for word in string.ascii_letters):                  #if there are no letters from the alphabet in the sentence then get angry
        print("What do you expect me to do with this?")				    #output that nothing was entered
    elif any(punctuation in sentence for punctuation in string.punctuation):	    #or if any item in the string.punctuation list is in the sentence, output that punctuation was found.
        print("Punctuation found!")
    else:									    #if the sentence passes all of these conditions then
        empty = False 								    #end the while loop and procede
sentence = sentence.lower() 							    #turns the sentence into all lower case to prevent case senstivity.
sentencelist = sentence.split()							    #splits the sentence into individual words and stores it in this variable as a list.
loop = True
while loop is True:
    search = input("Word to find:\n>") 						    #user enters word they wish to find which is also stored as a variable.
    search = search.lower()							    #again, the word the user wishes to search is turned into lower case to match the sentence, avoiding case senstivity.
    if not any(word in sentence for word in string.ascii_letters):                  #if there are no letters from the alphabet in the sentence then get angry
        print("What do you expect me to do with this?")
    elif any(punctuation in search for punctuation in string.punctuation):
        print("There's punctuation in this word, did you miss click?")
    else:
        loop = False
position = [i for i, found in enumerate(sentencelist) if found == search] 	    #For every word in sentencelist that matches search, it will add the index (position) of that word to the position list.
if len(position) >1: plural = "s" 						    #used to help the following output make more sense. basically, if the word has been found more than one time, the sentence will say "positions" instead of "position"
else:
    plural = "" 								    #sets the variable plural as nothing so it knows not to add an s on the end of positions.
if not position: 								    #basically, if no positions are found, then output it no word found.
	print("The word", search, "wasn't found.")
else: 										    #self explanitory, if the word was found, output the success, and it's positions.
    print("The word,", search, ", was found at position"+ plural, position, ".")
input()										    #creates a break so the user can press enter when they wish to close the program.
