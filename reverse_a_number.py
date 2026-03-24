# reverse a number
number = 12345
reverse = ""
for digit in str(number):
    reverse = str(digit) + str(reverse)
print(reverse)

# reverse string
string = "Hello World"
reverse_string = ""
for char in string:
    reverse_string = char + reverse_string
    print(reverse_string)
print(reverse_string)