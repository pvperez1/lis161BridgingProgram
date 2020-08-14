# Modify the program that prompts the user
# for the file name so that it prints a funny
# message when the user types in exact file name:
# "na na boo boo". The program should behave normally
# for all other files which exist or don't exist.
# Compute for the number of subject lines.

filename = input("Enter filename: ")

if filename == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    exit()

try:
    fhandle = open(filename)
except:
    print("File not found")
    exit()

subject_lines = 0
for line in fhandle:
    if line.startswith('Subject'):
        subject_lines += 1

print("There were {sub} subject lines in {file}".format(
            sub=subject_lines,file=filename)
    )
