# def say_hello():
#   print('Hello World!')

# say_hello()

print("-----------------------------")

# def say_hello(name):
#   print(f'Hello {name}!')

# say_hello('Bob')

print("-----------------------------")

# in nil input, then asign World as a default
# def say_hello(name='World'):
#   print(f'Hello {name}!')

# say_hello()
# say_hello('Bob')

print("-----------------------------")

def say_hello(name='World', greeting=None):
  if greeting == None:
    print(f'Hello {name}!')
  else:
    print(f'{greeting} {name}!')

say_hello()
say_hello('Bob')
say_hello(greeting='Howdy')
say_hello('Bob', 'Howdy')

