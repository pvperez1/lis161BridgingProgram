# Write a program to read through a file
# and print the contents of the file (line
# by line) all in upper case

filename = input("Enter filename: ")

try:
    fhandle = open(filename)
except:
    print("File not found")
    exit()

for line in fhandle:
    print(line.strip().upper())
