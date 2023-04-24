#!/usr/bin/env python3
import rospy
import numpy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

from tf.transformations import euler_from_quaternion, quaternion_from_euler
M_PI =  numpy.pi  #3.1415
roll = pitch = yaw = 0.0
yaw = 0.1
roll = 0.2
pitch= 0.3

def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
   # print(orientation_list)
    

    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)  
    roll_deg = roll* 180.0 / M_PI
    pitch_deg = pitch* 180.0 / M_PI
    yaw_deg = yaw * 180.0 / M_PI

    print ('roll_deg=', roll_deg, 'pitch_deg=', pitch_deg, 'yaw_deg=', yaw_deg)

rospy.init_node('euler_quaternion_from_IMU')

sub = rospy.Subscriber ('/imu/data', Imu, get_rotation)

r = rospy.Rate(10)
while not rospy.is_shutdown():    
   # quat = quaternion_from_euler (roll, pitch,yaw)
   # print(quat[0])
    r.sleep()
