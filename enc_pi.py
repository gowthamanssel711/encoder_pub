import rospy
from geometry_msgs.msg import Twist
import Encoder

enc_one = Encoder.Encoder(24, 10)       #motor one encoder pins
enc_two = Encoder.Encoder(24, 10)       #motor two encoder pins
enc_three = Encoder.Encoder(24, 10)     #motor three encoder pins

def pub_encoder():

    pub = rospy.Publisher('encoder_readings', Twist, queue_size=1)
      
    move_cmd = Twist()
    move_cmd.linear.x = int(enc_one)
    move_cmd.linear.y = int(enc_two)
    move_cmd.angular.z = int(enc_three)

    now = rospy.Time.now()
    rate = rospy.Rate(10)

    while rospy.Time.now() < now + rospy.Duration.from_sec(6):
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        pub_encoder()
    except rospy.ROSInterruptException:
        pass