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

Since it will be wireless driving around, I would lunch the above commands in screen sessions in case your terminal drops. 

# Parts
----

![alt_tag](https://github.com/joemcmanus/tankbotROS/blob/master/img/tankbotParts.jpg)

This kit was built using the following off the shelf parts:
 - RaspberryPi  https://www.raspberrypi.org/products/raspberry-pi-3-model-b/
 - OSEPP Tank kit  https://www.osepp.com/robotic-kits/4-tank-mechanical-kit
 - 7.4v RC Car Battery https://www.amazon.com/gp/product/B07RBTVBY3/
 - Battery Charger https://www.amazon.com/gp/product/B07QRQT3LC/
 - Robot Hat Cntroller https://geekworm.com/collections/raspberry-pi-4/products/new-updated-raspberry-pi-motor-hat-full-function-robot-expansion-board
 - Random USB battery for pi https://www.amazon.com/gp/product/B07RSH9NP7/
 - Random "deans connector" for battery https://www.amazon.com/gp/product/B07WHPD4KD/

# Standalone
----
If you want to make the robot standalone you will want to make it a WiFi AP and then you can go beyond WiFi range. 

Install wifi-ap snap. 

    sudo snap install wifi-ap 

Then you may want to start up the above processes on boot. 

    crontab -e
    @reboot /home/you/yourScript.sh 

Create a script that will start roscore, source the env file, start up the tankbot topic and then start flask. An exmaple of on I use is attached here as rosStart.sh . 


