### Robot description 
After addiing xacro files and plugins of gazebo, run robot state publiher that publisher robot_desciption topic and run rviz2 in a seperate terminal to visualize it.


### Install gazebo_classsic

```bash
sudo apt install ros-humble-gazebo-ros-pkgs
```

### Run Robot state publisher
```bash
ros2 launch custom_robot rps.launch.py
```

### Run Joint state publisher GUI 
```ros2 run joint_state_publisher_gui joint_state_publisher_gui ```

### Launch Gazebo with a custom world
```bash
ros2 launch custom_robot launch_sim.launch.py world:=src/custom_robot/worlds/custom_world.world 
```

### Install SLAM toolbox
```bash
sudo apt install ros-humble-slam-toolbox
```

### Create map using slam toolbox, copy mapper_params file to config directory 
```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/custom_robot/config/mapper_params_online_async.yaml use_sim_time:=true
```

### Run rviz
```bash
ros2 run rviz2 rviz2 
```

### Teleoperate Robot
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

