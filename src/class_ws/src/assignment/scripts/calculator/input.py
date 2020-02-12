#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16

num1_pub = rospy.Publisher('num1_topic', Int16, queue_size=10)
# add another publish to publish another 

def result_callback(data):
    result = data.data
    rospy.loginfo("the result I am getting is: " + str(result))

def main():
    rospy.init_node('talker', anonymous=True)

    rospy.Subscriber("result_topic", Int16, result_callback)

    rospy.spin()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
