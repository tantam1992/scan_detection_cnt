#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int16
import math

rospy.init_node('laser_sub', anonymous=True)
pub = rospy.Publisher('detections', Int16, queue_size=10)

# Counts the number of valid range values in a LaserScan message.
# Publishes the count as an Int16 message on the 'detections' topic.
def callback(data):
    count = 0
    for i in range(len(data.ranges)):
        # check if value is not nan
        if not math.isnan(data.ranges[i]):
            count += 1
    # rospy.loginfo("Number of obstacle detected: %d", count)
    pub.publish(count)   
    
def laser_sub():
    rospy.Subscriber("scan_filtered", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    laser_sub()