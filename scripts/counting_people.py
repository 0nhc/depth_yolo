# Copyright (C) 2023  0nhc
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.If not, see <https://www.gnu.org/licenses/>.         

#!/usr/bin/env python3  
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
