# calculate the sum of digits of a number
number = 486
sum = 0
for digit in str(number):
    sum = sum + int(digit)
print(sum)