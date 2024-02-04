#!/usr/bin/python3

''' 
Code to develop an algorithm to avoid obstacles 
    
Run the color_detection launch commands before this file 

Execute with python3 obstacle_avoidance.py 

Complete this template and the template file obstacle_functions.py 
'''


import cv2
import numpy as np 
import rospy
import numpy as np 
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

from obstacle_functions import get_all_section_values, get_velocity


# Variables 
########################################################################
turning_left = False   


# Laser callback -> it is called when the topic receives information
################################################################
def laser_callback(msg):

    # Declare turning_left as a global variable 
    global turning_left
	
    # Create velocity publisher and velocity variable
	################################################################
    # <COMPLETE>

    # Read laser scan data and get section values
    ################################################################
    # Use get_all_section_values from obstacle.py
    # <COMPLETE>    

    # Get the clearest path 
    ################################################################
	
    # Sort laser scan section indexes using the means from clearer sections to less clear sections
    # The clearest paths will be the ones with higher means 
    # Hint: use numpy
    clearer_path_indexes = # <COMPLETE>

    # Extract the 3 most clearer sections 
    three_clearest_paths = # <COMPLETE>
    

    # Get robot velocity depending on laser values  
    ################################################################
    # Use get_velocity function from obstacle_function.py
    # Update turning_left variable inside the function 
    vel, turning_left = # <COMPLETE> 

       
    # Publish velocity 
    # <COMPLETE>



   
# Init node and suscribe to laser scan topic 
################################################################
def main():

    # Init obstacle_avoidance node 
    # <COMPLETE>

    # Suscribe to laser scan topic and add callback + spin
    # <COMPLETE>


if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    