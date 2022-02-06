#read the file 
name = input("Enter file name: ") 
text = open(name, "r") 

#a list to store the words 
words = []

#loop and add the new words to the words list  
for line in text: 
    x = line.split()

    for word in x: 
        if word not in words: 
            words.append(word) 

#sort and print the words 
words.sort() 
print(words)