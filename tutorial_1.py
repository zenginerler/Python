"""
================================ LECTURE NOTES =================================
# Interpreter - Script - Data Types - Operators

DATA TYPES: 

String  - str()   :	"this is a string"
Integer - int()   :	571
Float   - float() : 2.5
Boolean - bool()  :	True, False

* (I haven't explained these yet)
Other Known Data types: list, tuple, set, dict, bytes, etc.


special strings:

"\n"   : nextline
"\t"   : tab

--------------------------------------------------------------------------------

VARIABLE: storage location paired with an associated symbolic name

variableName = storedValue

--------------------------------------------------------------------------------

COMMENT TYPES:

* Comments are ignored by the python interpreter

hashtag - "#" : comment out a single line
triple quote  : comment out a block of code

===============================================================================

OPERATORS:

Comma     : useful to seperate different types of data (adds a single space)
Plus sign : Concatenates multiple data into one (might throw an error for different types)


Math operators:

add              :  +
substract        :  -
multiply         :  *
division (int)   :  /
division (float) :  // 

--------------------------------------------------------------------------------

BUILT-IN FUNCTIONS:

max()   : returns the maximum value
min()   : returns the minimum value

===============================================================================

IDLE Shortcuts:

Ctrl + N    : Open a new Script
Ctrl + S    : Save the Script
F5          : Run the file
"""



print("\t")

variableName = "I can store whatever I want!"

var0 = "Hello"
var1 = "World"

var2 = 1899
var3 = 18.75
var4 = False

# This is a comment and will be ignored by our program
""" this is also a comment and will also be ignored by our program """

print(var0 + var1)
print(var0 , var1)

print("\n")

print(100 + 50)
print(100 - 50)
print(10 * 2)
print(10 /  2)
print(10 // 2)

print("\n")

print( max(5, 100, 3000) )
print( min(5, 100, 3000) )