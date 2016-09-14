sentence = input("Enter sentence to compress: \n>") #user enters a sentence
sentencelist = sentence.split() #sentence is split into induvidual words and then stored in a list called sentencelist
words = {} #create a blank array for later
index = 0 #set the index value at 0 to start
for word in sentencelist: #goes through each item in the sentencelist
    if word not in words: #if the item isn't in the words array
        words[word] = index #the item in the words arrays index is changed to the apropriate position
        index += 1 #the index variable is increased by one, so the next item found can have its index set to the second position

with open('index.txt', 'w') as f: #opens or creates a file called index
    for word in sentencelist: #for each item in the sentencelist
        f.write('%d\n' % words[word]) #write the items position number onto the text document along with a newline for the next item

with open('words.txt', 'w') as f: #opens or creates a file called words
    for word in sentencelist:#for each item in sentencelist
        f.write(word + '\n') #write the item onto the text document along with a newline for the next item
print("File compressed into indexes and words.") #informs the user that the compressing process has compelted
