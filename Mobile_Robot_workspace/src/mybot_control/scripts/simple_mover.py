#!/usr/bin/env python


import math
import rospy
from std_msgs.msg import Float64

def mover():

    pub1 = rospy.Publisher('/mybot/frontCaster_effort_controller/command', Float64, queue_size=10)

    pub2 = rospy.Publisher('/mybot/leftWheel_effort_controller/command', Float64, queue_size=10)

    pub3 = rospy.Publisher('/mybot/rightWheel_effort_controller/command', Float64, queue_size=10)


    rospy.init_node('bot_mover')
    rate = rospy.Rate(10)
    start_time = 0

    while not start_time:
        start_time = rospy.Time.now().to_sec()
    
    while not rospy.is_shutdown():
        elapsed = rospy.Time.now().to_sec() - start_time
        pub1.publish(100*math.sin(2*math.pi*0.1*elapsed))
        pub2.publish(7)
        pub3.publish(7)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
