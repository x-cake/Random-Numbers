import random

def rand(x):
    random_numb = random.randint(1, x)
    rand = 0
    while rand != random_numb:
        rand = int(input(f'Pick a number between 1 and {x}: '))
        if rand < random_numb:
            print('Try again, this number is too low.')
        elif rand > random_numb:
            print('Try again, this number is too high.')
    
    print(f'Wow! You pick the right number {random_numb}!')


rand(100)