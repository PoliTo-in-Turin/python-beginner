count = 0
while count != 5:
    count += 1
    print(count)

print("-----------------------------")

count = 0
while count <= 20:
    count += 3
    print(count)

print("-----------------------------")

count = 20
while count >= 0:
    count -= 3
    print(count)

print("------------EX-----------------")

import random

value = random.randint(1, 5)
count = 0
guess = 0

# go out from loop only if guess == value
while guess != value:

    count += 1
    guess = input('Guess a number between 1 and 5: ')
    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue

    if guess > value:
        print('Your guess is too high, try again!')
    elif guess < value:
        print('Your guess is too low, try again!')


else:
    # right after out of loop
    print(f'You guessed it in {count} tries!')

