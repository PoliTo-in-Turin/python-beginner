first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.strip().lower().title()

# Second challenge
second_value = second_value.title().strip().replace("-","")

# Third challenge
third_value = third_value.lower().strip().replace(" ","").replace("-"," ").title()

#print(first_value)
print(f'{first_value:^30}')
print(second_value)
print(f'{third_value:>30}')

# Fourth challenge - use only the print() function (no f-strings)
print("{}#{}#{}!"
.format(fourth_value, fifth_value, sixth_value))

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
str = "\t{}\n\t{}\n\t{}\n".format(fourth_value, fifth_value, sixth_value)
#print(f'{str:30}')  useless :'(
print(str)