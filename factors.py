number = int(input(f'Enter a positive integer: '))
i = 1
while i < number + 1:
    x = number % i
    if x == 0:
        print(f'{i} is a factor of {number}')
    i += 1