# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Script URL: http://www.codeskulptor.org/#user3-QAwawnboHX-10.py
# https://class.coursera.org/interactivepython-2012-001/human_grading/view_app/courses/204/assessments/12/submissions/18904
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code

num_range = 100

# helper function to initial game    
def init():
    if num_range == 100:
        range100()
    else:
        range1000()
        
# define event handlers for control panel    
def range100():
    global secretNumber
    global guesses
    global num_range
    num_range = 100
    secretNumber = random.randrange(0,num_range)
    guesses = math.ceil((math.log((num_range - 0)-1))/(math.log(2)))
    print ""
    print "New game. Range is from 0 to "+str(num_range)
    print "Number of remainin guesses is "+str(guesses)
    print ""
      
def range1000():
    global secretNumber
    global guesses
    global num_range
    num_range = 1000
    secretNumber = random.randrange(0,num_range)
    guesses = math.ceil((math.log((num_range - 0)-1))/(math.log(2)))
    print ""
    print "New game. Range is from 0 to "+str(num_range)
    print "Number of remainin guesses is "+str(guesses)
    print ""
    
def get_input(guess):
    if guess != "":
        global guesses
        global secretNumber
        guesses -=1
        if secretNumber > int(guess):
            msg = "Higher!"
        elif secretNumber < int(guess):
            msg = "Lower!"
        else:
            msg = "Win!"    
        print "Guess was "+guess
        print "Number of remainin guesses is "+str(guesses)
        
        if guesses == 0 and msg != "Win!":
            msg = "You Lose!"
        
        print msg
        
        if msg == "You Lose!":
            print "The Secret number was: "+str(secretNumber)
        
        if msg == "Win!" or msg == "You Lose!":
            init()
    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter a guess",get_input,200)

# register event handlers for control elements


# start frame
frame.start()
init()
# always remember to check your completed program against the grading rubric
