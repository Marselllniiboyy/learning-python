# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello Wrold")

# Quotes Inside Quotes
# print("I said:'Get the fk up'")

# Assign String to a Variable
a = "Bodoh"
# print("kamu " + a)

# Multipel
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''


# Strings are Arrays
# strings in Python are arrays of bytes representing unicode characters.
b = "Hello, Ujang"
# print(b[1])

# Looping Through a String
d = "Mancester is red"
for x in d:
  print(x)

# String Length
# To get the length of a string, use the len() function.
e = "Hijau"
print(len(e))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
f = "buy one get two jokowi"
if "one" in f:
  print("yes, oen is present or" + " true")

# Check if NOT
#  we can use the keyword not in

txt="Coffe is free"
print("20 dolar" not in txt) #true
print("free" not in txt) #fals

if "20 dolar" not in txt:
  print("It is free bro")



