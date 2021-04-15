import deck
import processor

cards = deck.create_deck()

for card in cards:
  print(card)

# OUTPUT
# 2 of Hearts
# 3 of Hearts
# 4 of Hearts
# 5 of Hearts
# 6 of Hearts
# 7 of Hearts
# 8 of Hearts
# 9 of Hearts
# 10 of Hearts
# Jack of Hearts
# Queen of Hearts
# King of Hearts
# Ace of Hearts
# 2 of Spades
# 3 of Spades
# 4 of Spades
# 5 of Spades
# ...

print("-----------------------------")
# imported processor on top

my_list = [5, 'Dan', '4', 7, 'Steve', 'Amy', 'Rhonda', 4, '9', 'Jill', 7, 'Kim']
my_bad_list = 5

numbers = processor.process_numbers(my_list)
print(numbers)

names = processor.process_names(my_list)
print(names)

numbers = processor.process_numbers(my_bad_list)
print(numbers)

names = processor.process_names(my_bad_list)
print(names)

# OUTPUT
# [4, 4, 5, 7, 7, 9]
# ['Amy', 'Dan', 'Jill', 'Kim', 'Rhonda', 'Steve']
# []
# []