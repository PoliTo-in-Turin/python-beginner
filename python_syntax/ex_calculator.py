# Simple calculator!
# First number? 4
# Operation? *
# Second number? 5
# product of 4 * 5 equals 20

def cal(op):
    switcher={
        "+": float(first_value) + float(second_value),
        "-": float(first_value) - float(second_value),
        "*": float(first_value) * float(second_value),
        "/": float(first_value) / float(second_value)
    }
    return switcher.get(op, "Invalid operator")

print("Simple calculator!")
first_value = input('First Number? ')
op = input('Operation? ')
second_value = input('Second Number? ')
print("product of " + first_value + op + second_value + " equals " + str(cal(op)))

