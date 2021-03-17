"""
================================ LECTURE NOTES =================================
LIST INDEXING

["w", "e", "l", "c", "o", "m", "e"]
  0    1    2    3    4    5    6

lst1 = ["w","e","l","c","o","m","e"]

print(lst1)
print()
print(lst1[0])

-------------------------------------------------------------------------------
Built-in Funtions:

print( )  : prints the given value to the shell/console/output_screen

int( )    : Converts the given value into an integer
str( )    : Converts the given value into a  string

-------------------------------------------------------------------------------
LOGIC OPERATORS:

equal to                    : ==
smaller than                : < 
smaller than or equal to    : <=
greater than                : >
greater than or equal to    : >=

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

-------------------------------------------------------------------------------
for i in range(10):
    print("I am a patato!")

for i in [0,1,2,3,4,5,6,7,8,9]:
    print("I am a patato!")

while True:
    print("I am a tomato!")


"""

def calculator():

    operator = input("Enter a math operator: ")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if (operator == "+"):
        print("Result:", num1 + num2)

    elif (operator == "-"):
        print("Result:", num1 - num2)

    elif (operator == "*"):
        print("Result:", num1 * num2)

    elif (operator == "/"):
        print("Result:", num1 / num2)

    else:
        print("Invalid operator!")
    

print()
calculator()
