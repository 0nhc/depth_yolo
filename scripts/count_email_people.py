#!/usr/bin/env python
import rospy
from darknet_ros_msgs.msg import BoundingBoxes
import smtplib
from email.mime.text import MIMEText
'''from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib'''

sent_email=False
sent_motion=False

def darknet_callback(data):
    global sent_email
    global sent_motion
    
    people_num = 0
    for i in data.bounding_boxes:
        if(i.Class == "person"):
            people_num = people_num + 1
    print(people_num)
    
    if people_num > 0 and not sent_email:
	smtp_server ='smtp.gmail.com'
	smtp_port = 587
	sender_email = 'e7ee59sjy@gmail.com'
	sender_password = 'jsetnmivkvkessss'
	recipient_email = 'zhouru2@udmercy.edu'
	message = 'The number of people counting: %s' % people_num

	msg=MIMEText(message)
	msg['Subject'] = 'Counting People Number'
	msg['From'] = sender_email
	msg['To'] = recipient_email
	
	smtp=smtplib.SMTP(smtp_server, smtp_port)
	smtp.starttls()
	smtp.login(sender_email, sender_password)
	try:
	    smtp.sendmail(sender_email, recipient_email, msg.as_string())
	    sent_email = True
	finally:
	    smtp.quit()
    rospy.sleep(1.0)
    
def listener():
    rospy.init_node('counting_people', anonymous=True)
    rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, darknet_callback)
    rospy.spin()
 
if __name__ == '__main__':
    listener()
