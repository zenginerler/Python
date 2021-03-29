"""
================================ LECTURE NOTES =================================
# LOOP EXAMPLES:

for i in [0,1,2,3,4,5,6,7,8,9]:
    print("I am a patato!")

for i in range(10):
    print("I am a patato!")

for i in range(10):
    print(i)


counter = 0
while counter < 10:
    print("I am a tomato!")
    counter += 1


# this is a infinite loop. Press "Ctrl+C" to stop executing
while True:
    print("I am a tomato!")


-------------------------------------------------------------------------------
# Terminal & CMD (Command Prompt)

CMD commands (windows):
*if you use a system with Mac OS(Apple)/Unix/Linux, most of these commands will be different 

dir               :  Displays a list of files and folders contained inside the folder that you are currently working in. ("ls" in Mac)
                   
cd <folderName>   :  Changes the current working directory to specified directory (folder).

python <fileName> :  Run a python file in Command Prompt (should have python installed and added to path)


-------------------------------------------------------------------------------
# Importing libraries:


import math 

# this imports the whole math library. 
# Example ==>  math.sqrt(4)



import math as keko
# this imports the whole math library but with the name you specified
# Example ==>  keko.sqrt(4)


from math import sqrt

# this only imports the specified function/s (this doesn't requires you to use "math." )
# Example ==>  sqrt(4)


"""

import math

print( math.sqrt(25) )
print( math.sqrt(4) )
