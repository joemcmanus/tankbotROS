#!/bin/bash

sudo snap connect wifi-ap:network-manager network-manager:service


cd /home/joe
source /opt/ros/melodic/setup.bash

nohup roscore &> roscore.log &
sleep 5
cd tankbot_ros_ws
source devel/setup.bash 
nohup rosrun tankbot_ros ping_node &>>/home/joe/rosrun.log & 
nohup rosrun tankbot_ros driver_node &>>/home/joe/rosrun.log & 

cd /home/joe/tankbotROS/ROS/
nohup ./server.py &>/home/joe/server.log &

sleep 30
sudo wifi-ap.status restart-ap

