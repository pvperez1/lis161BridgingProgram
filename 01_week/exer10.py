# Write a while loop that starts at
# the last character in the string
# and works its way backwards to the
# first character in the string,
# printing each letter on a separate line,
# except backwards.

str = input("Enter word: ")

for i in range(len(str), 0, -1):
    print(str[i-1])

# Another solution:
# length = len(str)
# while length > 0:
#     print(str[length - 1])
#     length -= 1
