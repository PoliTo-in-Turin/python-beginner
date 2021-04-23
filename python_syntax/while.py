import random 

roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:
  name = input('Enter a name, or \'q\' to quit:  ' )

  if name.strip() == '':
    continue

  if name.strip() == 'q':
      break
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')

# <output>
# First person to roll a 5 wins!
# Enter a name, or 'q' to quit:  yui
# yui rolled 2
# Enter a name, or 'q' to quit:  miya
# miya rolled 5
# miya Wins!!!
# You rolled the dice 2 times.