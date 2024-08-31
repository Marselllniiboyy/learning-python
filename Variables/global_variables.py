# Global variables can be used by everyone, both inside of functions and outside.
x = "Niceseee"

def myFucn():
  x = "Awsome"
  print("Python is " + x + " for bigginer")

# print("Python is " + x + " for bigginer")
y = "Jelek"

def myLocaltoGlobal():
  global y #To create a global variable inside a function, you can use the global keyword.,Also, use the global keyword if you want to change a global variable inside a function.
  y = "Menyenangkan" 
  print("Python is " + y)
myLocaltoGlobal()

print("Yang " + y + " itu kamu")