#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

num1 = 0

# init a publisher as global variable so that it is able to be used any where in the code
result_pub = rospy.Publisher('result_topic', Int16, queue_size=10)

# define callback function which will be called when a message going though topic
def num1_callback(data):
    global num1
    num1 = data.data
    rospy.loginfo(num1)
    result_pub.publish(num1)

def main():
    # init node name
    rospy.init_node('listener', anonymous=True)
    
    # init subscriber that listen to a topic
    rospy.Subscriber("num1_topic", Int16, num1_callback)
    
    # define the flash rate for the program to loop
    # !!!!!!!!!!!!!!!
    # -------------------------------
    # rate = rospy.Rate(10) # 10hz
    # while not rospy.is_shutdown(): 
    #    rate.sleep()
    # -------------------------------
    # above code serves the same purpose as the one below, they all keep the script running so that it is able to keep subscribe or publish to a topic and prevent script kill themselves 
    # -------------------------------
    # rospy.spin()
    # ------------------------------- 
    # the difference between them is that while loop is useful when you try to keep publish to a topic by itself
    rospy.spin()

if __name__ == '__main__':
    main()
