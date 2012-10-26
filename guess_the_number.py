# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Script URL: http://www.codeskulptor.org/#user3-QAwawnboHX-1.py

import simplegui
import random
import math

# initialize global variables used in your code
global secretNumber
global guesses

# define event handlers for control panel    
def range100():
    # button that changes range to range [0,100) and restarts
    secretNumber = random.randrange(0,100)
    guesses = 7
      
def range1000():
    # button that changes range to range [0,1000) and restarts
    secretNumber = random.randrange(0,1000)
    guesses = 10

#def init():
    
#def get_input(guess):
    # main game logic goes here	

    
# create frame


# register event handlers for control elements


# start frame
#init()
# always remember to check your completed program against the grading rubric

