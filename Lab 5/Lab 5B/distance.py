###############################################################################################################################################################
# Program Name: Falling Distance Module          Author: Sierra E. Stokes
# Date Created: 10/10/2021                                                   
# Created in partial fulfillment of the coursework for COSC 1336-0XX at Austin Community College
###############################################################################################################################################################
# Purpose of Program: This module calculates and returns the distance in meters(m) the object falls in a specific time period (seconds(s))
###############################################################################################################################################################
# Data Dictionary: 
# Name                       Type        Range         Use
# ----------------           -------     ----------    -------------------
# gravity                    Float       9.8           represents the gravitational constant
# distance                   Float       float         represents the distance the object falls(m) in a specific time period(s)
###############################################################################################################################################################
# Functions used:
# Name                    Inputs                  Use
# ----------------        -------------------     ---------------------------------------
# main                                            displays the distance an object falls in meters for 1-10 seconds
# falling_distance         time                   calculates and returns the distance the object falls(m) in a specific time period (s)            
###############################################################################################################################################################

# This function calculates and returns the distance the object falls(m) in a specific time period(s) 
def falling_distance(seconds):
    gravity = 9.8
    distance = .5*(seconds**2)*gravity
    return distance