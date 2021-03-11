"""
================================ LECTURE NOTES =================================
INDEXING

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

-------------------------------------------------------------------------------
# Defining a your own funtion:

def functionName():
    <some code>
    <some code>
    <some code>
    <some code>
    

# calling a funtion:

functionName()

"""

def calculator():

    operator = input("Enter a math operator: ")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if (operator == "+"):
        print(num1 + num2)

    elif (operator == "-"):
        print(num1 - num2)

    elif (operator == "*"):
        print(num1 * num2)

    elif (operator == "/"):
        print(num1 / num2)

    else:
        print("Invalid operator!")