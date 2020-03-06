# tankbotRos

An intro to ROS using a tank kit

#Setup

1. clone the repot 

    git clone git@github.com:joemcmanus/tankbotROS.git

2. Setup workspace

    joe@tankbot:~$ mkdir -p tankbot_ros_ws/src
    joe@tankbot:~$ cd tankbot_ros_ws/src
    joe@tankbot:~/tankbot_ros_ws/src$ catkin_init_workspace 
    joe@tankbot:~/tankbot_ros_ws/src$ catkin_create_pkg tankbot_ros rospy std_msgs 

3. Create Package 

    joe@tankbot:~/tankbot_ros_ws/src$ cp ~/tankbotROS/ROS/* tankbot_ros/src/. 
    joe@tankbot:~/tankbot_ros_ws/src$ cd ~/tankbot_ros_ws/
    joe@tankbot:~/tankbot_ros_ws$ catkin_make 

4. Enable i2c without running as root

    sudo usermod -aG i2c joe

5. Test

You will need 3 terminals to make this work. 
 - Log in and run roscore 
 - Log in and launch the driver_node

    joe@tankbot:~/tankbot_ros_ws$ cd ~/tankbot_ros_ws/
    joe@tankbot:~/tankbot_ros_ws$ source devel/setup.bash 
    joe@tankbot:~/tankbot_ros_ws$ rosrun tankbot_ros driver_node 

 - Log in to terminal 3 and test the app, not it is a #1 not a lowercase L. 

    rostopic pub -1 /command std_msgs/String "Forward"
    rostopic pub -1 /command std_msgs/String "Backward"

