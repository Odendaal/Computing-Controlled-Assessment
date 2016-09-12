sentence = input("Enter sentence to compress: \n>")
sentencelist = sentence.split()
words = {}
index = 0
for word in sentencelist:
    if word not in words:
        words[word] = index
        index += 1

with open('index.txt', 'w') as f:
    for word in sentencelist:
        f.write('%d\n' % words[word])

with open('words.txt', 'w') as f:
    for word in sentencelist:
        f.write(word)
        f.write('\n')
print("File compressed into indexes and words.")
