#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

# init a publisher as global variable so that it is able to be used any where in the code
num1_pub = rospy.Publisher('num1_topic', Int16, queue_size=10)
 
# define callback function which will be called when a message going though topic
def result_callback(data):
    result = data.data
    rospy.loginfo("the result I am getting is: " + str(result))

def main():
    # init node name
    rospy.init_node('talker', anonymous=True)
    
    # init subscriber that listen to a topic
    rospy.Subscriber("result_topic", Int16, result_callback)

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
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown(): 
        num1_pub.publish(123)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
