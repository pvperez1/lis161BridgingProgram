# Write another program that prompts
# for a list of numbers as the previous
# exercise and at the end prints out both
# the maximum and minimum of the numbers
# instead of the average.

sum = 0
count = 0
max = None
min = None

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

    if max is None or max < num:
        max = num

    if min is None or min > num:
        min = num

print(sum, count, max, min)
