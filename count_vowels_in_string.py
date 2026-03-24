# count the number of vowels in a string
string = "Hello America"
lower_string = string.lower()
vowels = "aeiou"
count = 0
for char in lower_string:
    if char in vowels:
        count += 1
print(count)
