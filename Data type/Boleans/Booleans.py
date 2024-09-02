# Booleans represent one of two values: True or False.
#example
print(10>9)
print(10==10)
print(10==9)
print(10>20)

# Print a message based on whether the condition is True or False:
a=30
b=70

if a>b:
  print("b is greater thsn a")
else:
  print("a is smaler than b")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("hello")) #true
print(bool(123)) #true
print(bool(["apple", "cherry", "banana"])) #true
print(bool("")) #False
print(bool([])) #False
print(f"{bool(0)}"+ " Nol itu false") #False

# ond one more has return false is
class myClass():
  def __len__(self):
    return 0
  
myobj = myClass()
print(bool(myobj)) #False

# Functions can Return a Boolean
def myFucn():
  return True
print(myFucn())
# another example
if myFucn():
  print("YES")
else:
  print("NO")

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x,int))