# Write a function called count()
# that accepts a string (word) and
# a character (char) and outputs the
# number of occurrences of char in word

def count(word, char):
    char_count = 0
    for c in word:
        if c == char:
            char_count += 1
    return char_count

inp_word = input("Enter word: ")
inp_char = input("Enter char: ")

print(count(inp_word, inp_char))
