#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3
import geometry_msgs.msg
import tf
import tf2_ros


def callback(data):
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    static_transformStamped = geometry_msgs.msg.TransformStamped()

    static_transformStamped.header.stamp = rospy.Time.now()
    static_transformStamped.header.frame_id = "world"
    static_transformStamped.child_frame_id = "imu_pose"

    static_transformStamped.transform.translation.x = 0.0
    static_transformStamped.transform.translation.y = 0.0
    static_transformStamped.transform.translation.z = 0.0

    quat = tf.transformations.quaternion_from_euler(
        float(data.x), float(data.y), float(data.z))

    static_transformStamped.transform.rotation.x = quat[0]
    static_transformStamped.transform.rotation.y = quat[1]
    static_transformStamped.transform.rotation.z = quat[2]
    static_transformStamped.transform.rotation.w = quat[3]

    broadcaster.sendTransform(static_transformStamped)


if __name__ == '__main__':
    rospy.init_node('get_pose', anonymous=True)
    rospy.Subscriber("imu_pose", Vector3, callback)
    rospy.spin()
