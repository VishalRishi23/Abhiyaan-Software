#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
pi=3.1415926535897
def move():
  rospy.init_node('turtle_exercise',anonymous=True)
  pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
  a=input("Move or Rotate?") #1-Move 2-Rotate
  if (float(a)==2.0):
    msg=Twist()
    speed=input('Speed?')
    angle=input('Angle?')
    direction=input('Clockwise?') #True/False
    angular_speed=(float(speed)*2*pi)/360
    relative_angle=(float(angle)*2*pi)/360
    msg.linear.x=0
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.x=0
    msg.angular.y=0
    if direction:
      msg.angular.z=-abs(angular_speed)
    else:
      msg.angular.z=abs(angular_speed)
    t0=rospy.Time.now().to_sec()
    current_angle=0
    while (current_angle<relative_angle):
      pub.publish(msg)
      t1=rospy.Time.now().to_sec()
      current_angle=angular_speed*(t1-t0)
    msg.angular.z=0
    pub.publish(msg)
    rospy.spin()
  else:
    msg=Twist()
    speed=input('Speed?')
    distance=input('Distance?')
    direction=input('Forward?')  #True/False
    msg.linear.y=0
    msg.linear.z=0
    msg.angular.z=0
    msg.angular.x=0
    msg.angular.y=0   
    if direction:
      msg.linear.x=abs(float(speed))
    else:
      msg.linear.x=-abs(float(speed))
    while not rospy.is_shutdown():
      t0=rospy.Time.now().to_sec()
      current_distance=0
      while (current_distance<float(distance)):
        pub.publish(msg)
        t1=rospy.Time.now().to_sec()
        current_distance=speed*(t1-t0)
      msg.linear.x=0
      pub.publish(msg)  


if __name__=='__main__':
  try:
    move()
  except rospy.ROSInterruptException: 
    pass 
           
  
  

    
