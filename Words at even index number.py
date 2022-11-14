#Print characters from a string that are present at an even index number

word = input("Enter word:  ")
print("Word is:",word)

x = list(word)
for i in x[0::2]:
    print(i)


