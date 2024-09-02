# Upper Case
# The upper() method returns the string in upper case:
a="Hello, Bangli"
upperCase = a.upper()
print(upperCase) #HELLO, BANGLI

# Lower Case
lowerCase = a.lower()
print(lowerCase) #hello, bangli

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# The strip() method removes any whitespace from the beginning or the end:
b = "  Hello, Bangli  "
print(b) #no remove
removeSpace = b.strip()
print(removeSpace)

# Replace String
replaceLeter = a.replace("H","G")
print(replaceLeter)
replaceLeter = a.replace("Hello","Guncana")

# Split String
#The split() method splits the string into substrings if it finds instances of the separator:
k = "Hello, Bangli, Papua, Jembrana, Susut"
splitList = k.split(", ")
print(splitList)
