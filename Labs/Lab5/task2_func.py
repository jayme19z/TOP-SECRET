# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def ftoc(f):
    c = (5 / 9) * (f - 32)
    print(c)

f = int(input())
ftoc(f)
