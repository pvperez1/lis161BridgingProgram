# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475’
# Use find and string slicing to extract
# the portion of the string after the colon
# character and then use the float function
# to convert the extracted string into a floating
# point number.

str = "X-DSPAM-Confidence:0.8475"
dspam = float(str[str.find(':') + 1:])
print(dspam)
