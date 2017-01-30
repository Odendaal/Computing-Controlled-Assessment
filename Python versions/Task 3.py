import string
def readfile():                         #creates the function which will be used to read compressed files.
    sentencelist = []                   #creates a blank array which will be added to later.
    attempt = "no"                      #creates a variable witht he value of "no" to be used for a while loop
    while attempt == "no":              #creates a loop so if an invalid input has been entered by the user, it loops back to the begining
        filename = input("Enter file name or type cancel. If you used this program to create the file, the filename will be whatever you called it plus 'words' on the end of it. (leave out the txt): ") #user enters the name of the file they wish to read here
        filenamecheck = filename.lower()    #makes another variable that turns the input into lower to allow non-case senstivity for a cancel input
        if filenamecheck == "cancel":       #if the user enters cancel it takes them back to the starting screen
            menu()                      #starting screen where user enters what they wish to do (read, write or compress)
        elif not any(word in filename for word in string.ascii_letters):                    #if there are no letters from the alphabet in the sentence then get angry
            print("What do you expect me to do with this? (please enter something)")				    #output that nothing was entered
        try:                            #runs this peice of code within an error exception
            with open(filename + '.txt', 'r') as f:         #opens the file that the user identified previously in the filename variable
                words = f.readlines()                       #sets the varaible words to have all the data in the file
                for word in words:                          #for each word in the file
                    if word not in sentencelist:            #if any of the words it goes through is not in the empty array sentencelist
                        word = word.strip('\n')             #removes the newline from the word to prevent logical errors
                        sentencelist.append(word)           #adds the word to the previously empty array
                        attempt = "yes"                     #ends the while loop so the code continues to the user being takent to the menu screen
        except FileNotFoundError:                           #if this error occurs, do the following
            print("Oops! Doesn't look like there's a file with that name (not locally anyway).")    #prints that a file was not found
            attempt = "no"                                                                          #attempt remains "no" so it loops back to asking for the file name until they enter a valid response or cancel and return to the main menu
    sentencestring = " ".join(sentencelist)                                                         #assigns a space character and the the sentence in the sentence list to this variable
    print("The following sentence has been constucted: \n \n" + sentencestring)                     #outputs the sentence that was put together
    menu()                                                                                          #returns user to main screen
    
def compressfile():                                                                                 #the following code will make the compress file function
    loop = True
    while loop is True:
        sentence = input("Enter sentence to compress: \n>")             #user enters a sentence
        if not any(word in sentence for word in string.ascii_letters):  #if there are no letters from the alphabet in the sentence then get angry
            print("What do you expect me to do with this?")
        else:
            loop = False                                                #end the while loop
    while loop is False:
        sentencename = input("Enter name of sentence: \n>")             #user enters the name they wish to to give the sentence which is used for naming the files
        if not any(word in sentencename for word in string.ascii_letters):
            print("I think a name would be nice...")
        else:
            loop = True
    sentencelist = sentence.split()                                     # sentence is split into induvidual words and then stored in a list called sentencelist
    words = {}                                                          #create a blank array for later
    index = 0                                                           #set the index value at 0 to start
    for word in sentencelist:                                           #goes through each item in the sentencelist
        if word not in words:                                           #if the item isn't in the words array
            words[word] = index                                         #the item in the words arrays index is changed to the apropriate position
            index += 1                                                  #the index variable is increased by one, so the next item found can have its index set to the second position

    with open('index.txt', 'w') as f:                                   #opens or creates a file called index
        for word in sentencelist:                                       #for each item in the sentencelist
            f.write('%d\n' % words[word])                               #write the items position number onto the text document along with a newline for the next item

    with open('words.txt', 'w') as f:                                   #opens or creates a file called words
        for word in sentencelist:                                       #for each item in sentencelist
            f.write(word + '\n')                                        #write the item onto the text document along with a newline for the next item
    print("File compressed into indexes and words.")                    #informs the user that the compressing process has compelted
    menu()

def menu():                                                 #the following code will be the functioning for the main menu
    print("Hello welcome to my controlled assessement task 3. What do you want to do? \n A) Read file \n B) Compress sentence into file \n C) Exit") #give the user multiple choices for what they want to do
    optionloop = True                                       #set a loop as TRUE.
    while optionloop is True:                               #while the option loop is True do the following code
        choices = ["a","b","c"]                                   #all the options the user can enter
        choice = input(">")                                 #user inputs choice here
        choice = choice.lower()                             #makes input lowercase for case senstivity
        if choice not in choices:
            print("Come on dude choose one of the options above!")
        elif choice == "a":
            readfile()
        elif choice == "b":
            compressfile()
        elif choice == "c":
            print("CYA!")
            exit
menu()                                                      #the first peace of code the program actually runs is this. Shows the user the menu function, refer to line 52 to see what will appear.
