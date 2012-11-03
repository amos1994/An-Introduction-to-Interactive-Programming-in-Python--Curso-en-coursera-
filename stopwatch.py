# template for "Stopwatch: The Game"
# URL:http://www.codeskulptor.org/#user4-2RWIboh1eA-3.py
import simplegui
# define global variables

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
#def format(t):

time = 0

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    print "start"

def stop():
    print "stop"
    
def reset():
    print "reset"
# define event handler for timer with 0.1 sec interval
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200,100)
frame.set_canvas_background("Black")
button1 = frame.add_button("Start", start, 100)
button2 = frame.add_button("Stop", stop, 100)
button3 = frame.add_button("Reset", reset, 100)

# register event handlers

# start timer and frame
frame.start()

# remember to review the grading rubric
#1 pt - The program successfully opens a frame.

#TODO
#1 pt - The program has a working "Start" button 
#		that starts the timer.
#1 pt - The program has a working "Stop" button 
#		that stops the timer.
#1 pt - The program has a working "Reset" button 
#		that stops the timer (if running) and resets the 
#		timer to 0.
#2 pts -The "Stop" button correctly updates the 
#		success/attempts counters.  Give only one point 
#		if hitting the "Stop" button changes the score 
#		when the timer is already stopped.
#1 pt - The "Reset" button clears the success/attempts 
#		counters.
#4 pts -The time is formatted according to the description 
#		in step 4 above.  Award partial credit 
#		corresponding to 1 pt per correct digit.  
#		For example, a version that just draw tenths of 
#		seconds as a whole number should recieve 1 pt. 	
#		A version that draws the time with correctly placed
#		decimal point (but no leading zeros) only should 
#		receive 2 pts. A version that draws minutes, 
#		seconds and tenths of seconds but fails to always 
#		allocate two digits 
#		to seconds should receive 3 pts.
#2 pts -The program correctly draws the number of 
#		successful stops at a whole second versus total 
#		stops.  You should give one point each for 
#		successful and total stops.  If the score is 
#		correctly reported as a percentage instead, 
#		give only one point.
