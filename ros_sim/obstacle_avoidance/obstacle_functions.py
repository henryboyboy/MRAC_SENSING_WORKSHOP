#!/usr/bin/python3

'''
FUNCTIONS FOR OBSTACLE AVOIDANCE CODE
'''

import numpy as np

# Gets all the values for each section of the laser scan and its mean value 
def get_all_section_values(msg):

    # We create the list where we will save the values of each sections
    all_sides = []
    all_sides_mean = []
    
    # The first section is the center, we save the laser scan values from -15º to 15º 
    side = np.array([msg.ranges[-15:], msg.ranges[:15]]).flatten()
	
    # Delete the nan values and inf values from side 
    side = # <COMPLETE>
	
    # We add the center section values and the mean
    all_sides.append(side)
    all_sides_mean.append(np.mean(side))
   
    # Add laser scan data every 30 degrees starting from 15º (the last iteration will be at 345º)
    # <COMPLETE>
	
		# Get actual laser scan values (from actual plus 30 values)
    	side = # <COMPLETE>
		
        # Delete the nan values and inf values from side 
    	# <COMPLETE>
		
        # Save side in all_sides
		# <COMPLETE>

    	# Save mean side values in all_sides_mean
		# <COMPLETE>
    
    print("\n",all_sides_mean)

    return all_sides, all_sides_mean



# Gets the robot velocity based on the clearest paths 
##############################################################################################################
# Parameters:                                                                                                #
# - all_sides_mean: mean values of each section                                                              #
# - three_clearest_paths: the indexes of the  three sections with higher means (obstacles are more far away) #
# - turning_left: it will be True if the robot is turning left, and False otherwise                          #
# - vel: velocity Twist vector                                                                               #
##############################################################################################################
# The front directions are saved at the 0, 1 and 11 indexes                                                  #
##############################################################################################################

def get_velocity(all_sides_mean, three_clearest_paths, turning_left, vel): 
	
    # Get the index of the clearest path 
    clearest_path = # <COMPLETE>
    print(clearest_path)

    # If one of the FRONT orientations means is less than 1.0 
    # <COMPLETE>
    	
    	# We want hopefully that the three front directions are contained in the three_clearest_paths 
		# If one of them is not contained in the three_clearest_paths
        # <COMPLETE>
    	
            # If the clearest_path is between 1-5 indexes (included) or we are already turning left --> Turn left
    	    # <COMPLETE>
    	       print("Turn left")
               # <COMPLETE>   # Update turning_left to True
               # <COMPLETE>   # Turn to left
			   
			# If the clearest_path is 0 or >5 or we are not turning to left --> Turn right  
    	    else: 
    	       print("Turn right")
               # <COMPLETE>   # Update turning_left to False
               # <COMPLETE>   # Turn to right
    	else:
    	   # Go straight to avoid being trapped spinning 
    	   print("Go straight 1")
           # <COMPLETE>   # Update turning_left to False
           # <COMPLETE>   # Go straight
    	
    # If none of the front directions are less than 1.0 (clear path ahead) -> Go straight
    else:
        print("Go straight 2")
        # <COMPLETE>   # Update turning_left to False
        # <COMPLETE>   # Go straight

		
    return vel, turning_left