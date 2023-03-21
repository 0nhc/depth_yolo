#!/usr/bin/env python
import rospy
from darknet_ros_msgs.msg import BoundingBoxes

def darknet_callback(data):
    people_num = 0
    for i in data.bounding_boxes:
        if(i.Class == "person"):
            people_num = people_num + 1
    print(people_num)
    'rospy.loginfo(people_num)
    
def listener():
    rospy.init_node('counting_people', anonymous=True)
    rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, darknet_callback)
    rospy.spin()
 
if __name__ == '__main__':
    listener()
