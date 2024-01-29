#!/usr/bin/python3

''' 
Code to detect and follow a color 
    
Run the color_detection launch commands before this file 

Execute with python3 color_detection.py 

Complete this template and the template files color_image and velocity
'''

# Import libraries
########################################################################
import cv2
import numpy as np 
import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from color_image import show_image, get_color_range, detect_color, get_max_contour
from velocity import get_velocity


# Variables 
########################################################################
bridge = CvBridge()
#min_detection = # <COMPLETE> 



# Image callback -> it is called when the topic receives information
################################################################
def image_callback(msg):
    
    rospy.loginfo("Image received")
   
    # Get image and publisher 
    ##########################################
    # Convert your ros image message to opencv using bridge
    img = bridge.imgmsg_to_cv2(msg,"bgr8")

    # Show image using show_image function
    show_image(img, "(window_name)")


    # Get half width of the image 
    mid_width = w / 2
    # <COMPLETE> 

    # Create velocity publisher and variable of velocity
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    vel = Twist()
    # <COMPLETE> 

    
    # Do color detection 
    ##########################################

    # Get color range using get_color_range from color_image.py
    lower_range, upper_range = get_color_range('blue')
    # <COMPLETE> 
    
    # Get color mask using detect_color from color_image.py
    # <COMPLETE>
    mask = detect_color(img, lower_range, upper_range)
    # Show mask 
    # <COMPLETE>
    show_image(mask, "2window_name")


    # Find contours and get max area using get_max_contours from color_image.py 
    # <COMPLETE>
 #   print("Maximum area: ", area)


    # Get robot speed     
    ##########################################

    # If the area of the detected color is big enough
  #  if():
  #      print("Cylinder detected")

        # Draw contour and center of the detection and show image 
        # <COMPLETE>

        # Gets the color speed and direction depending on the color detection using get_velocity from velocity.py
        # <COMPLETE>

            
    # If the area of the detected color is not big enough, the robot spins 
  #  else:
  #      print("Looking for color: spinning")
  #      # <COMPLETE>
        

    # Publish velocity
    # <COMPLETE> 
    pub.publish(vel)



# Init node and suscribe to image topic 
################################################################
def main():
    rospy.init_node('color_detection')

    rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback )
    rospy.spin()
    cv2.destroyAllWindows()
  # Init node 'color_detection'
    # <COMPLETE>

    # Suscribe to image topic and add callback + spin
    # <COMPLETE>

if __name__ == '__main__':
    main()