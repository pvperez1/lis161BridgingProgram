# Write a program to prompt for a file name
# and then read through the file and look for
# lines of the form: X-DSPAM-Confidence:0.8475
# Compute for the Average X-DSPAM-Confidence

filename = input("Enter filename: ")
try:
  fhandle = open(filename)
except:
  print("File not found")
  exit()

dspam_sum = 0
dspam_count = 0

for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        dspam = float(line[line.find(':')+1:])
        dspam_sum += dspam
        dspam_count += 1

print("Average D-SPAM:", dspam_sum/dspam_count)
