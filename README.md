# tankbotRos

An intro to ROS using a tank kit
![alt_tag](https://github.com/joemcmanus/tankbotROS/blob/master/img/tankbotStand.jpg)

# Setup
----

1. clone the repo

```
git clone git@github.com:joemcmanus/tankbotROS.git
```


1b. If you have not installed ROS yet do the following

```
joe@tankbot:~$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
joe@tankbot:~$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
joe@tankbot:~$ sudo apt install ros-melodic-ros-base
joe@tankbot:~$ sudo rosdep init 
joe@tankbot:~$ rosdep update 
joe@tankbot:~$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
joe@tankbot:~$ source ~/.bashrc
joe@tankbot:~$ sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

2. Setup workspace

```
joe@tankbot:~$ mkdir -p tankbot_ros_ws/src
joe@tankbot:~$ cd tankbot_ros_ws/src
joe@tankbot:~/tankbot_ros_ws/src$ catkin_init_workspace 
joe@tankbot:~/tankbot_ros_ws/src$ catkin_create_pkg tankbot_ros rospy std_msgs 
```

3. Create Package 

```
joe@tankbot:~/tankbot_ros_ws/src$ cp ~/tankbotROS/ROS/* tankbot_ros/src/. 
joe@tankbot:~/tankbot_ros_ws/src$ cd ~/tankbot_ros_ws/
joe@tankbot:~/tankbot_ros_ws$ catkin_make 
```

4. Enable i2c without running as root

```
sudo usermod -aG i2c joe

```
5. Test

You will need 3 terminals to make this work. 
 - Log in and run roscore 
```
joe@tankbot:~$ roscore 
... logging to /home/joe/.ros/log/2c987dd4-5f52-11ea-b4f2-b827eb2ffb14/roslaunch-tankbot-7884.log
Checking log directory for disk usage. This may take awhile.
```

 - Log in and launch the driver_node

```
joe@tankbot:~/tankbot_ros_ws$ cd ~/tankbot_ros_ws/
joe@tankbot:~/tankbot_ros_ws$ source devel/setup.bash 
joe@tankbot:~/tankbot_ros_ws$ rosrun tankbot_ros driver_node 

```
 - Log in to terminal 3 and test the app, not it is a #1 not a lowercase L. 

```
joe@tankbot:~$ rostopic pub -1 /command std_msgs/String "Forward"
joe@tankbot:~$ rostopic pub -1 /command std_msgs/String "Backward"
```

# Flask
----
![alt_tag](https://github.com/joemcmanus/tankbotROS/blob/master/img/tankbotFlask.jpg)

A flask app to drive the robot can be run by starting the 2 steps above and for step three running python server.py 


# Parts
----

![alt_tag](https://github.com/joemcmanus/tankbotROS/blob/master/img/tankbotParts.jpg)

This kit was built using the following off the shelf parts:
 - RaspberryPi 3B
 - OSEPP Tank kit 
 - 7.4v RC Car Battery 
 - Robot Hat Cntroller
