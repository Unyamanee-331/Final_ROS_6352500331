#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
def talker():
    pub = rospy.Publisher('sum_std_id', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        std_id = 6+3+5+2+5+0+0+3+3+1
        rospy.loginfo(std_id)
        pub.publish(std_id)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

