# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# txt = "My name is John, I am " + age
# print(txt) #error

# But we can combine strings and numbers by using "f"-strings or the format() method!
age = 36
txt = f"My name is Marsel, i am {age} ylears old"
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 20
txt=f"The price is {price:.2f} dollars"
# or
txt=f"The total is {20*35:.2f}"
print(txt)