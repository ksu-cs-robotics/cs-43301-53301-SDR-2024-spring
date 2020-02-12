#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String

name = ""
operation = ""
num1 = 0
num2 = 0
result = 0  

num1_flag = True
num2_flag = True

result_pub = rospy.Publisher('result_topic', Int16, queue_size=10)

def name_callback(data):
    global name
    name = data.data
    
def operation_callback(data):
    global operation
    operation = data.data

def num1_callback(data):
    global num1
    global num1_flag
    num1 = data.data
    num1_flag = not num1_flag
    
def num2_callback(data):
    global num2
    global num2_flag
    num2 = data.data
    num2_flag = not num2_flag
    if num1_flag == num2_flag:
        result = operate()
        result_pub.publish(result)
        rospy.loginfo("My name is %s. I want to do %s operation. The result of %i and %i is %i.", name, operation, num1, num2, result)
    else:
        result_pub.publish(0)
        rospy.loginfo("message missmatch")


def operate():
    if operation == "+":
        return (num1 + num2)
    elif operation == "-":
        return (num1 - num2)
    elif operation == "*":
        return (num1 * num2)
    elif operation == "/":
        return (num1 / num2)
    else:
        return 0

def main():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("name_topic", String, name_callback)
    rospy.Subscriber("operation_topic", String, operation_callback)
    rospy.Subscriber("num1_topic", Int16, num1_callback)
    rospy.Subscriber("num2_topic", Int16, num2_callback)
  

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()