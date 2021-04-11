# print("Hello World!")

print("What is your name?")
name = input()
print("Hello, " + name)

print("-----------------------------------------")

# sum up (as a string, will return error if you put numbers as inputs)

print("First Number:")
first_number = input()
print("Second Number:")
second_number = input()
sum = first_number + second_number
print(sum)

print("-----------------------------------------")

# sum up (int version)
print("First Number:")
first_number = int(input())
print("Second Number:")
second_number = int(input())
sum = first_number + second_number
# it is a wrong way
#print("Sum: " + sum)
# important to transform into string before to combine with another string
print("Sum: " + str(sum))