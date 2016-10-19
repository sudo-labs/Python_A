# The code just below isn't important for now, all it does is clear our console
# it's an example of some of the clever things we can do with Python
# There's loads of explanation so you can follow along with what's happening

# This line is an import statement, which will be important in Python B
# It allows us to use the functions and classes in the "os" library,
# the Python tools for communicating with the operating system

# Some common functions are always available for convenience, but others
# need to be brought in from libraries, because Python has a lot of tools
# and you can write your own as well!
import os

# This line is doing several things - First, it defines a lambda function,
# otherwise called an anonymous function, it's mostly for style and compactness
# The function is assigned the name "clear", so later we'll be able to call
# clear() to use it

# Next, it uses system from the os library, this is for sending commands directly
# to the shell
# inside that is a simple if statement, Python allows single-line conditionals
# although we won't be using them in this tutorial

# We're told to use the 'cls' command if the value name from os is 'nt',
# or clear if it isn't
# 'nt' is the code for Windows, because Windows NT is the fundamental 
# part of Windows

# 'cls' and 'clear' do the same thing, but 'cls' is the command you can give
# to the Windows shell to clear it, whereas on UNIX-like systems (Mac, Linux,
# and most others), the command is 'clear'
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Lastly, we call the function we created, which just gives our console the command
# to clear itself
clear()



###############################################################################
######################### Tutorial code begins here ###########################
###############################################################################

# You can include a string in a print() function, and the string will be written
# directly to the console

print("Welcome, noble hero of the kingdom of Din!")

# Strings are typically written with quotation marks
text1 = "You stand at the entrance to Garmag's cave..."

# You can also write them with apostrophes or "single quotes" in Python
text2 = '... A wretched den belonging to an evil sorcerer!'

# By using three single quotes ''' or double quotes """, Python will let you
# write your string on multiple lines

text3 = """Herein dwell a small army of golems, every shape and every size.
These thoughtless automata are built with but one purpose...
TO CONQUER YOUR KINGDOM!"""

# You can also continue your string on the next line with a backslash \, 
# but be careful, the backslash tells Python not to recognize a line break, 
# so everything you type afterwards will appear on the same line!

text4 = "Noble hero, noblest of the noble, here you have come \
to defeat... at least some of these golems"

# You can tell Python to start a new line using the newline \n character
# This is called an escape character, there are several, and each designates
# a special character that you can't normally type

text5 = "And just as importantly...\nClaim Garmag's treasure while he's away!"

# Backslashes in front of special characters, such as line breaks and 
# quotation marks, tell python to ignore their special properties and 
# print them normally, but they give special properties to some regular characters!

# Let's write our last string and run this file
# In the future, you'll probably want to write your room descriptions as
# a single string for convenience

text6 = "Before you is the door to Garmag's fetid Cave. \n\
Noble hero, what do you do?\n" 

# this last newline character will put in an extra line for readability

# Above, we've declared all the strings we're going to use
# By putting those variables into a print() function, we will write their
# contents to the console

print(text1)
print(text2)
print(text3)
print(text4)
print(text5) 
print(text6)

# Some text adventures use '> ' as their standard prompt, but yours can be anything
# you want
# Here, we set the value of action equal to the result of input(), if the player types
# "kick in the door" after the prompt, then action will contain the string "kick in the door"
action = input('I will ')

# This line is just to demonstrate that action now contains the text that was entered
# after the prompt
print(action)
