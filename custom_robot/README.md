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


### Slam toolbox
```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/custom_robot/config/mapper_params_online_async.yaml use_sim_time:=true
```
If needed map can be reloaded from the last saved state and expand the map by modifying mapper_params_onine_asyc.yaml file 
and give an existing path of the saved map. and localize within the new map


### Run rviz
```bash
ros2 run rviz2 rviz2 
```

### Teleoperate Robot
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

use turtlebot teleop command as this gives more control over speec
```bash
ros2 run turtlebot3_teleop teleop_keyboard 
```

### save the map
```bash
ros2 run nav2_map_server map_saver_cli -f <map_name>
```

---------------------------------------------------------------------------
                                  RUN AMCL For LOCALIZATION
---------------------------------------------------------------------------

### install nav2
```bash
sudo apt install ros-humble-navigation
sudo apt install ros-humble-nav2-bringup
```


### RUN a map server

THis is load saved map file and publish init on /map topic

```bash
ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=<map_path> 
```

In a seperate terminal activate map_server using
```bash
ros2 run nav2_util lifecycle_bringup map_server
```
The map is now available on /map topic, run launch file and rviz2 and set frame_id to map and map topic to /map
Change setting to transient_local if map is not appearning 


```bash
ros2 run nav2_amcl amcl -p use_sim_time:=true
```