import random
roll = random.randint(1, 10)
print(f'1: You rolled {roll}.\n')

import random as alias
roll = alias.randint(1, 10)
print(f'2: You rolled {roll}\n')

import random as dice
roll = dice.randint(1, 10)
print(f'3: You rolled {roll}\n')