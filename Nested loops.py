# Printing coordinates

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')


# Print xxx in shape of F
number = [5, 2, 5, 2, 2]
for x_count in number:
    print('x'* x_count)

# Doing the same using Nested loop

number = [5, 2, 5, 2, 2]
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

