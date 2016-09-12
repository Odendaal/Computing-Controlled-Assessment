def readfile():
    sentencelist = []
    attempt = "no"
    while attempt == "no":
        filename = input("Enter file name or type cancel. If you used this program to create the file, the filename will be whatever you called it plus 'words' on the end of it. (leave out the txt): ")
        if filename == "cancel":
            menu()
        elif filename == "Cancel":
            menu()
        try:
            with open(filename + '.txt', 'r') as f:
                words = f.readlines()
                for word in words:
                    if word not in sentencelist:
                        word = word.strip('\n')
                        sentencelist.append(word)
                        attempt = "yes"
        except FileNotFoundError:
            print("Oops! Doesn't look like there's a file with that name (not locally anyway).")
            attempt = "no"
    sentencestring = " ".join(sentencelist)
    print("The following sentence has been constucted: \n \n" + sentencestring)
    menu()
    
def compressfile():
    sentence = input("Enter sentence to compress or type cancel \n > ")
    sentencename = input("Enter the sentences' name or type cancel \n > ")
    if sentence == "cancel" or sentencename == "cancel":
        menu()
    elif sentence == "Cancel" or sentencename == "Cancel":
        menu()
    sentencelist = sentence.split()
    words = {}
    index = 0
    for word in sentencelist:
        if word not in words:
            words[word] = index
            index += 1

    with open(sentencename + 'index.txt', 'w') as f:
        for word in sentencelist:
            f.write('%d\n' % words[word])

    with open(sentencename + 'words.txt', 'w') as f:
        for word in sentencelist:
            f.write(word)
            f.write('\n')
    print("File successfully compressed!")
    menu()

def menu():
    print("Hello welcome to my controlled assessement task 3. What do you want to do? \n 1) Read file \n 2) Compress sentence into file \n 3) Exit")
    optionloop = int(0)
    while optionloop == 0:
        try:
            choice = int(input("> "))
            while choice not in (1, 2, 3):
                choice = int(input("Enter a valid choice (1 to 3). \n >  "))
            if choice == 1:
                optionloop == 1
                readfile()
            elif choice == 2:
                optionloop == 1
                compressfile()
            elif choice == 3:
                optionloop == 1
                print("Cya!")
                exit
        except ValueError:
            optionloop == 0
menu()
