# Write a program which repeatedly reads
# numbers until the user enters "done".
# Once "done" is entered, print out the
# total, count, and average of the numbers.
# If the user enters anything other than a
# number, detect their mistake using try and
# except and print an error message and skip
# to the next number.

sum = 0
count = 0

while True:
    num = input("Enter number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue

    sum += num
    count += 1

if count == 0:
    print(sum, count, None)
else:
    print(sum, count, sum/count)
