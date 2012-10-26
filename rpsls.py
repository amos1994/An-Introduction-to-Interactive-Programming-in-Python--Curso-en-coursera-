#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  RPSLS.py
#  Juego de Rock-paper-scissors-lizard-Spock
#  Primer mini-proyecto de este curso, lo estoy haciendo a destiempo pero igual debo hacerlo
#  
#  Copyright 2012 Alexis Sánchez <alexis@laptop>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions
def number_to_name(number):
    # fill in your code below
	if number == 0:
		return "rock"
	elif number == 1:
		return "Spock"
	elif number == 2:
		return "paper"
	elif number == 3:
		return "lizard"
	elif number == 4:
		return "scissors"	
	
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
	if name=="rock":
		return 0
	elif name == "Spock":
		return 1
	elif name == "paper":
		return 2
	elif name == "lizard":
		return 3
	elif name == "scissors":
		return 4
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below
    # convert name to player_number using name_to_number
	player = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
	comp = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
	mod = (player - comp) % 5
    # use if/elif/else to determine winner
	if mod == 3 or mod == 4:
		result = "Computer wins!"
	elif mod == 2 or mod == 1:
		result = "Player wins!"
	else:
		result  = "Player and computer tie!"
    # print results
	print "Player chooses",number_to_name(player)
	print "Computer chooses",number_to_name(comp)
	print result
	print ""
   
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
# always remember to check your completed program against the grading rubric

