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

#def number_to_name(number):
    # fill in your code below
    
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


#def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

   
# test your code
print name_to_number("rock")
print name_to_number("Spock")
print name_to_number("paper")
print name_to_number("lizard")
print name_to_number("scissors")
# always remember to check your completed program against the grading rubric

