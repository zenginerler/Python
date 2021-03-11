"""
================================ LECTURE NOTES =================================
# From Lecture 1

DATA TYPES: 

String  - str()   :	"this is a string"
Integer - int()   :	571
Float   - float() :     2.571
Boolean - bool()  :	True, False

Other Known Data types: list, tuple, set, dict, bytes, etc.


MATH OPERATORS:

add              :  +
substract        :  -
multiply         :  *
division (int)   :  /
division (float) :  // 


Special strings:

"\n"   : nextline
"\t"   : tab

-------------------------------------------------------------------------------

IDLE Shortcuts:

Ctrl + N    : Open a new Script
Ctrl + S    : Save the Script
F5          : Run the file



===============================================================================
# Lecture 2

LOGIC OPERATORS:

equal to                    : ==
smaller than                : < 
smaller than or equal to    : <=
greater than                : >
greater than or equal to    : >=


-------------------------------------------------------------------------------
Indexing

welcome
0123456

word1 = "welcome"

print(word1)
print()
print(word1[0])

-------------------------------------------------------------------------------
Built-in Funtions:

max( )
min( )
len( )

print( )  : prints the given value to the shell/console/output_screen

int( )    : Converts the given value into an integer
str( )    : Converts the given value into a  string

-------------------------------------------------------------------------------
Conditional Statements

Example Figure:

if <logical condition>:
    <some code to execute>
    
elif <logical condition>:
    <some code to execute>
    
else:
    <some code to execute>

"""


name = "Yavuz"
age = 23


print(name == age)
# This is just a string!! --- Be careful about quotes!!!
print("name == age")


print()


# Mad Lib
name = input("What is your name: ")
age = input("Tell me your age: ")

print()
print("Your name is", name, "and")
print("I know that you have born in", ( 2021 - int(age) ) )
print()


if (name == "ahmet"):
    print("Computer: Hey ahmet!")

elif (name == "bera"):
    print("Computer: Hi bera!")

elif (name == "mustafa"):
    print("Computer: Hello mustafa!")

else:
    print("Computer: I guess we haven't met before, user!")
