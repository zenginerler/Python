"""
================================ LECTURE NOTES =================================
# From Lecture 2

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

def functionName():
    print("some code 1")
    print("some code 2")
    print("some code 3")
    print("some code 4")


def add():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print()
    print("Sum of your numbers:", num1 + num2)



def calculator():
    print()
    print("Try to complete the calculator function")

    # 1 - Obtain two integers from the user; hint --> input()

    # 2 - Obtain an math operator from the user; hint --> ("+", "-", "*", "/")

    # 3 - Use conditional statements detect the math operator,
    #     then apply the math and print the result


calculator()
