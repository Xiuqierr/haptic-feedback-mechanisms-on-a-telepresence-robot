#!/usr/bin/env python
import rospy
import tf
import random
import numpy as np

from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import Twist, PoseStamped, Pose
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String, Float64MultiArray

from abc import abstractmethod
from math import pi as PI, radians, degrees, sqrt, cos

class RobotControl():
    def __init__(self):
        rospy.init_node('robot_control',anonymous = True)
        self.vel_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
        self.threshold = 1
        self.region_value = np.zeros(8)
        self.pub = rospy.Publisher('chatter',Float64MultiArray,queue_size=10)
        
    def start(self):
        self.scan_sub = rospy.Subscriber("/scan",LaserScan,self.onscan)
        rospy.spin()

    def onscan(self,scandata):
        '''
        Callback for scan data
        '''
        '''
        print "0"
        print scandata.ranges[0]
        print "90"
        print scandata.ranges[90]
        print "180"
        print scandata.ranges[180]
        print "270"
        print scandata.ranges[270]
        '''
        max_val = np.zeros(8)
        max_val[0] = max(self.scan_region(scandata,0,23),self.scan_region(scandata,338,359))
        max_val[1] = self.scan_region(scandata,23,68)
        max_val[2] = self.scan_region(scandata,68,113)
        max_val[3] = self.scan_region(scandata,113,158)
        max_val[4] = self.scan_region(scandata,158,203)
        max_val[5] = self.scan_region(scandata,203,248)
        max_val[6] = self.scan_region(scandata,248,293)
        max_val[7] = self.scan_region(scandata,293,338)

        for i in range(0,8):
            print(i)
            print(max_val[i])

        self.region_value = max_val
        self.publisher()

    def publisher(self):
        rate = rospy.Rate(10)
        array=self.region_value
        region_info=Float64MultiArray(data=array)
        self.pub.publish(region_info)
        rate.sleep()


    def scan_region(self,scandata,minv,maxv):
        max_val = scandata.ranges[minv]
        for i in range(minv,maxv):
            max_val = min(scandata.ranges[i],max_val)
        if(max_val>self.threshold):
            max_val=0.0
        return max_val


    def run(self,scandata):
        pass

if __name__ == "__main__":
    try:
        RobotControl().start()
    except rospy.ROSInterruptException:
        pass
