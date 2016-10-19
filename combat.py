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

def entrance():
    print("Welcome, noble hero of the kingdom of Din!")

    text1 = "You stand at the entrance to Garmag's cave..."
    text2 = '... A wretched den belonging to an evil sorcerer!'
    # One problem with strings that span multiple lines is that you can't indent 
    # any of the lines inside of your string, or the indent
    # will be read as part of it!
    text3 = """Herein dwell a small army of golems, every shape and every size.
These thoughtless automata are built with but one purpose...
TO CONQUER YOUR KINGDOM!"""
    text4 = "Noble hero, noblest of the noble, here you have come \
to defeat... at least some of these golems"
    text5 = "And just as importantly...\nClaim Garmag's treasure while he's away!"
    text6 = "Before you is the door to Garmag's fetid Cave. \n\
Noble hero, what do you do?\n" 

    print(text1)
    print(text2)
    print(text3)
    print(text4)
    print(text5) 
    print(text6)

    door_hp = 100

    combat(door_hp)

def combat(door_hp)
    action = input('I will ')
    door_hp = kick(door_hp)

    if action == "kick in the door":
        # We've nested our if statements so that we will only try to kick in the door if the
        # player says so
        if door_hp <= 0:
            print("The door buckles against your mighty kick! Garmag's dank cave awaits you...")
            laboratory()
        else:
            print("The door shudders, but it does not break.")
            combat(door_hp)
    else
        print("Adventurers open doors by kicking them in and darn it that is what you are going to do!")
        combat(door_hp)

def laboratory():
    # This will be our second room, we're just leaving it empty for now
    pass

def kick(enemy_hp):
    # the value has been reduced in order to demonstrate the looping combat
    damage = 30
    return enemy_hp - damage

# Now that we're back to no indentation, Python knows that we're not in 
# the entrance() code block anymore
# calling entrance() here tells Python to execute the function
entrance()

# If you indent any lines after this, they'll be members of a new block
def does_nothing():
    pass 
    # pass is a keyword that tells a function not to do anything
    # if you call does_nothing, it will do nothing
    # this exists so that you can test code with empty functions and not
    # get any errors
