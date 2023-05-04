#!/bin/bash

cp -r /home/ws/src/CustomRobots/tello_phy/tello_ros/ /home/ws/src
cp -r /home/ws/src/CustomRobots/tello_phy/ros2_shared/ /home/ws/src
cd /home/ws/src/tello_ros
rm -rf tello_description tello_gazebo
cd /home/ws
colcon build --symlink-install
source install/setup.bash
cp -r install /
cp -r install /src/manager/launcher/
cd /


root="cd /"
ros_setup="source /.env && source ~/.bashrc && source /home/ws/install/setup.bash"
runserver="python3 RoboticsAcademy/manage.py runserver 0.0.0.0:8000"
runram="python3 /manager.py 0.0.0.0 7163"

eval ${ros_setup} && echo 'environment set'
$root && $runram