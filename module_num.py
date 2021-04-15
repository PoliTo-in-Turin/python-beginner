def add_two_numbers(x, y):
    return x + y

add_two_numbers(4, 6)
result = add_two_numbers(5, 7)
print(result)

print("-----------total #card------------------")

def create_deck():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = []

  for  suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

  return deck

my_deck = create_deck()
print(len(my_deck))


print("------------value is not global-----------------")

value = 1

def some_function():
    value = 10
    return value

print(value)
some_function()
print(value)

print("----------sponge parameter-------------------")

# flexible #input
def print_args(*args):
  for arg in args:
    print(f'arg = {arg}')

print_args('a')
print_args('a', 'b')
print_args('a', 'b', 'c')

print("------------keyword-----------------")

def print_keyword_args(**kwargs):

  third = kwargs.get('third', None)
  if third != None:
    print('third arg =', third)


print_keyword_args(first='a')
print_keyword_args(first='b', second='c')
print_keyword_args(first='d', second='e', third='f')

print("------------if we don't have specified keyword-----------------")

# NO OUTPUT
print_keyword_args(first='a')
print_keyword_args(first='b', second='c')

print("------------all print-----------------")

def print_keyword_args2(**kwargs):

  print('\n')
  print(kwargs)
  print(type(kwargs))

  print("------------for in-----------------")

  for key, value in kwargs.items():
    print(f'{key} = {value}')

  third = kwargs.get('third', None)
  if third != None:
    print('third arg =', third)


print_keyword_args2(first='a')
print_keyword_args2(first='b', second='c')
print_keyword_args2(first='d', second='e', third='f')