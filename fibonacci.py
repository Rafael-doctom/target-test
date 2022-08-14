# This program prints if a number belongs or doesn`t belong to Fibonacci sequence

# The first terms of Fibonacci sequence
n1 = 0
n2 = 1

# Get an integer and positive number from keyboard input
num_desired = input('Type in a number to see if it belongs to Fibonacci sequence: ')
while True:
    try:
        num_desired = float(num_desired)
        break
    except ValueError:
        print('Please type in a number.')
        num_desired = input('Type in a number to see if it belongs to Fibonacci sequence: ')

while (num_desired < 0) or (num_desired//1 != num_desired):
    print('Negative and not integers numbers are not part of Fibonacci sequence. Please type in an positive integer number')
    num_desired = float(input('Type in a number to see if it belongs to Fibonacci sequence: '))

# Print to user the chosen number
num_desired = int(num_desired)
print(f'You typed {num_desired}')

# Builds a fibonacci sequence with numbers that are <= the desired number
fibonacci_sequence = [n1, n2]
while True:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    fibonacci_sequence.append(nth)
    if nth >= num_desired:
        break

# Sees if the desired number is in the sequence
if num_desired in fibonacci_sequence:
    print(f'The number {num_desired} is in the Fibonacci sequence')
elif num_desired not in fibonacci_sequence:
    print(f'The number {num_desired} is not in the Fibonacci sequence')
