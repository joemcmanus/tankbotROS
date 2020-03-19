#!/bin/bash
#A really simple script to start roscore and it's associated parts 
#for the tankbot on boot
#the right way to do this is with a systemd startup script, but... 

HOME=/home/joe

cd $HOME

#Setup.sh is a misleading name, it should be something like rosenv
source /opt/ros/melodic/setup.bash

#Start roscore and give it a few seconds to finish starting
nohup roscore &> $HOME/roscore.log &
sleep 5

#cd in to the tankbot ros directory and get it to start. 
cd tankbot_ros_ws
source devel/setup.bash 
nohup rosrun tankbot_ros driver_node &> $HOME/rosrun.log & 

#Start the flask web server
cd $HOME/tankbotROS/ROS/
nohup ./server.py &> $HOME/server.log &

