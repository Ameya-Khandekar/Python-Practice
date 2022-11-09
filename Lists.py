names = ['Ameya', 'John', "Nick", 'Steve']
print(names)

#Printing Specific names
names = ['Ameya', 'John', "Nick", 'Steve']
print(names[1])

#Printing all items beginning from a specific index
names = ['Ameya', 'John', "Nick", 'Steve']
print(names[1:])

#Specifiying Index range
names = ['Ameya', 'John', "Nick", 'Steve']
print(names[0:2])

 #Renaming a value in Index

names = ['Ameya', 'John', "Nick", 'Steve']
names[0] = 'Mack'
print(names)
#  ['Mack', 'John', 'Nick', 'Steve']



#Program to find largest number in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 66, 21, 8]
max = numbers[0]  #Assuming 1st number is the greatest

for number in numbers:
    if number > max:
        max = number

print(max)
# 66
