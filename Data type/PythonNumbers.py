x = 2234567890# int = integer whole number, positive or negative, without decimals, of unlimited length
y =-2.4567# float floating point number  positive or negative, containing one or more decimals.
y = 2222e1
y = 23.45
z = 2j
z = 35 +3j #Complex numbers are written with a "j" as the imaginary part:

# print(type(x))
# print(type(y))
# print(type(z))
# print(z)

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
# Note: You cannot convert complex numbers into another number type.

#Random Number. Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1,10))