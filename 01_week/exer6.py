# Rewrite your pay computation with
# time-and-a-half for overtime and
# create a function called computepay
# which takes two parameters
# ( hours and  rate).

def computepay(h,r):
    if h > 40:
        pay = 40 * r + (h - 40)*r*1.5
    else:
        pay = h * r
    return pay

hours = input("Enter hour: ")

try:
    hours = float(hours)
except:
    print("Value Error for hours")
    exit()

rate = input("Enter rate: ")
try:
    rate = float(rate)
except:
    print("Value Error for rate")
    exit()

print("Pay:", computepay(hours,rate))
