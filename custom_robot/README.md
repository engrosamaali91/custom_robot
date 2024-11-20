## Robot Package
- Step 1: Make robot_core.xacro file: define links and joints
- ```ros2 run joint_state_publisher_gui joint_state_publisher_gui ``` Run this in seperate terminal becuase wheel wont publish the transforms
- ```ros2 launch gazebo_ros gazebo.launch.py``` Launch gazebo empty world
Note if gzebo is not installed run:
``` sudo apt install ros-humble-gazebo-ros-pkgs```