#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

num1 = 0

result_pub = rospy.Publisher('result_topic', Int16, queue_size=10)

def num1_callback(data):
    global num1
    num1 = data.data
    
    result_pub.publish(num1)

def main():

    rospy.init_node('listener', anonymous=True)
    
    rospy.Subscriber("num1_topic", Int16, num1_callback)
  
    rospy.spin()

if __name__ == '__main__':
    main()
