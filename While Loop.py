i = 1
while i <=5:
    print(i)
    i = i+1
print("Done")

i = 1
while i <=5:
    print('*' * i)
    i = i+1
print("Done")

# Secret Number
secret_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess The Number "))
    guess_count += 1
     if guess == secret_no:
    print("You won")
    break



