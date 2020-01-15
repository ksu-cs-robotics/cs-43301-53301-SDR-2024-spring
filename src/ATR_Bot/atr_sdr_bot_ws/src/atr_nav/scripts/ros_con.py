#!/usr/bin/python

import serial
import time
import rospy
import tf
from std_msgs.msg import Bool
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from tf.transformations import euler_from_quaternion, quaternion_from_euler

ARDUINO_COM = "/dev/ttyACM0"
ARDUINO_BAUD = 115200

JOY_MAX = 1023
JOY_MIN = 0

ODOM_MSG =          "o"
IMU_MSG =           "i"
CMD_MSG =           "c"
TORQUE_MSG =        "t"
GENERAL_MSG =       "g"

_TF_PREFIX_ =       "blue/"

arduino = serial.Serial(ARDUINO_COM, ARDUINO_BAUD, timeout=0.1)

odom_header_frame_id = "odom"
# odom_child_frame_id = "base_footprint"
odom_child_frame_id = "base_link"

odom = Odometry()

tf_br = tf.TransformBroadcaster()


def val_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def data_parsing_fake(data_in, msg_type):
    rospy.loginfo("I am parsing data")
    data_out = data_in

    return data_out

# TO DO
# remove type, because otherwise it will only parse first message type
def data_parsing(data_in, msg_type):
    # rospy.loginfo("data_in: " + str(data_in))
    data_out = data_in.split(",")
    # rospy.loginfo("parse data: " + str(data_out))
    if data_out[0] == "<!" and data_out[-1][:2] == "#>":
        if len(data_out) == int(data_out[2]) + 4:
            if data_out[1] == msg_type:
                return data_out[3:3 + int(data_out[2])]

def read_arduino():
    rospy.loginfo("I am reading")
    data = [0,0,0,0,0,0,0,0,0,0,0]
    odom_tmp = data_parsing(data, ODOM_MSG)

def send_arduino(data_in, size, msg_type):
    rospy.loginfo("I sending: " + str(data_in))
    data_out = ("<!" + "," + msg_type + "," + str(size) + ",")
    for i in range(size):
        data_out += str(data_in[i])
        data_out += ","
    data_out += "#>"
    rospy.loginfo("acutual data_out: " + data_out)
    
    arduino.write(data_out)

def command_callback(data):
    command = (data.data).split(',')
    command_temp = []
    if (command[0] == "shoot"):
        command_temp.append(command[0])
        send_arduino(command_temp, 1, GENERAL_MSG)


def power_callback(data):
    power_temp = [str(data.data).lower()]
    send_arduino(power_temp, 1, TORQUE_MSG)


def cmd_callback(data):
    cmd_temp = [data.linear.x, data.angular.z]
    send_arduino(cmd_temp, 2, CMD_MSG)

def odom_pub_info(odom_tmp):
    temp_quat = quaternion_from_euler(0, 0, odom_tmp[2])

    odom.header.frame_id = odom_header_frame_id
    odom.child_frame_id  = odom_child_frame_id
    odom.header.stamp = rospy.Time.now()

    odom.pose.pose.position.x = odom_tmp[0]
    odom.pose.pose.position.y = odom_tmp[1]
    odom.pose.pose.position.z = 0

    odom.pose.pose.orientation.x = temp_quat[0]
    odom.pose.pose.orientation.y = temp_quat[1]
    odom.pose.pose.orientation.z = temp_quat[2]
    odom.pose.pose.orientation.w = temp_quat[3]

    odom.twist.twist.linear.x  = odom_tmp[3]
    odom.twist.twist.angular.z = odom_tmp[4]

    tf_br.sendTransform((odom_tmp[0], odom_tmp[1], 0),
                    temp_quat,
                    rospy.Time.now(),
                    _TF_PREFIX_ + odom_child_frame_id,
                    _TF_PREFIX_ + odom_header_frame_id)

    return odom

def init():

    rospy.init_node('ros_arduino_exchange', anonymous=True)

    odom_pub = rospy.Publisher("odom", Odometry, queue_size=10)
    odom_broadcaster = tf.TransformBroadcaster()

    rospy.Subscriber("command", String, command_callback)
    rospy.Subscriber("cmd_vel", Twist, cmd_callback)
    rospy.Subscriber("motor_power", Bool, power_callback)

    rate = rospy.Rate(100) # 10hz
    twist_msg = Twist()

    time.sleep(1)
    arduino.flush()
    
    data = None

    rospy.loginfo("init")
    
    while not rospy.is_shutdown():
    # while 1:
        while arduino.inWaiting() > 0:
            data = arduino.readline()
            odom_temp = data_parsing(data, ODOM_MSG)
            cmd_temp = data_parsing(data, CMD_MSG)

            if odom_temp:
                odom_temp_folat = [ float(i) for i in data_parsing(data, ODOM_MSG) ]
                odom = odom_pub_info(odom_temp_folat)
                odom_pub.publish(odom)
            
            if cmd_temp:
                rospy.loginfo(cmd_temp)
            
        rate.sleep()

if __name__ == '__main__':
    init()