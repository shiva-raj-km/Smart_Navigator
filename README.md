# Smart_Navigator
An Opensource Platform for Autonomous Navigation systems.

## Prerequisites
Install the ROS Kinetic framework for Ubuntu 16.04. [Follow this](http://wiki.ros.org/kinetic/Installation/Ubuntu)

## Setup
``` bash
cd ~/ros_workspace/src
git clone https://github.com/shiva-raj-km/Smart_Navigator.git
```
Cut and copy two folders inside Smart_navigator into src folder

``` bash
cd ..
# Run 
catkin build
# If no errors after running catkin build the packages are installed and build properly
# Run 
source devel/setup.bash
# To source the terminal
```

## Usage
### Mapping
``` bash 
cd ~/ros_workspace
source devel/setup.bash
# Make four terminals source
# Terminal -1
roslaunch navigator_bringup robot_standalone.launch
# Terminal -2
roslaunch navigator_bringup gmapping.launch
# Terminal -3
roslaunch navigator_bringup keyboard_teleop.launch
# Terminal -4
roslaunch navigator_bringup view_navigation.launch
# Using teleoperation run the robot to explore the environment, and map building can be vizuliazed in Rviz. After bulding the map save it using map server.
rosrun map_server map_saver -f ~/<path>
```
### Autonomous Navigation
``` bash
# Terminal -1
roslaunch navigator_bringup robot_standalone.launch
# Terminal -2
roslaunch navigator_bringup amcl_demo.launch map_file:=~/<path of saved map>
# Terminal -3
roslaunch navigator_bringup move_base.launch
# Terminal -4
roslaunch navigator_bringup view_navigation.launch
