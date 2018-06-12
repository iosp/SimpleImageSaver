#!/usr/bin/env python
import sys
print(sys.version_info)

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
from gazebo_msgs.msg import ModelStates
# OpenCV2 for saving an image
import cv2
# ROS Pose message
from geometry_msgs.msg import Pose
model_name = "Sahar"
# Instantiate CvBridge
bridge = CvBridge()

def pose_callback(msg):

    global myPose , myOrientation 
 
    global model_index , model_name 

    if not (model_name in msg.name) :
        rospy.loginfo("Error : No vehicle named ' %s ' in the scen", model_name) 	 	
    else:
        model_index = msg.name.index(model_name)
        myPose = msg.pose[model_index].position	
        myOrientation = msg.pose[model_index].orientation 

def image_callback(msg):
    global myPose , myOrientation 

    file_name = "T=" + str(rospy.get_rostime()) + "   Px=" + str(round(myPose.x, 5)) + "   Py =" + str(round(myPose.y, 5)) + "   Pz =" + str(round(myPose.z, 5)) + "   Qx =" + str(round(myOrientation.x, 5)) + "   Qy =" + str(round(myOrientation.y, 5)) + "   Qz =" + str(round(myOrientation.z, 5)) + "   Qw=" + str(round(myOrientation.w, 5)) 

    print (myPose)
    print (myOrientation)
    print ("Received an image!")

    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    else:
        # Save your OpenCV2 image as a png
        cv2.imwrite("/home/robil/ " + file_name + " .png", cv2_img)

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/SENSORS/CAM/R"
    pose_topic = "/gazebo/model_states"


    # Set up your subscribers and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.Subscriber(pose_topic, ModelStates, pose_callback)

    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()
    