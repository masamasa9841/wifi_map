import commands
import time
import rospy
def signal_level():
    return commands.getoutput("cat /proc/net/wireless | awk 'NR==3 {print $4}'") 
if __name__ == '__main__':
    rospy.init_node('wifi_signal_level') 
    while not rospy.is_shutdown():
        print signal_level()
        time.sleep(0.1)
