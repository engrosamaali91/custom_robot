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

Now the map is loaded in rviz2, move a robot using teleop, the robot will be displaced in gazebo but not is rviz2 

In seperate terminal 
```bash
ros2 run nav2_amcl amcl -p use_sim_time:=true
```
Run amcl node to activate amcl 
```bash
ros2 run nav2_util lifecycle_bringup amcl
```

Now give 2d pose in rviz2 to localize it. Now the robot is localized and map is loaded.


---------------------------------------------------------------------------
                                  NAV2 stack
---------------------------------------------------------------------------

```bash
sudo apt install ros-humble-twist-mux
```
Remap command velocity output to the controller command velocity topic. red param file how it joy command velocity topic is prioritized 
this will give control to joy controller even during autonomous navigation 
```bash
ros2 run twist_mux twist_mux  --ros-args --params-file ./src/custom_robot/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped 
```
Later on I changed output velocities to cmd_vel becuase robot expectes the velocities on /cmd_vel topic

Run gazebo and rviz2 and run slam toolbox similarly

```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/custom_robot/config/mapper_params_online_async.yaml use_sim_time:=true
```

And now run navigation stack launch file 
```bash
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true
```
Add another map and change the topic to global_costmap



### My own launch file for navigation 
```bash
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true
```
Ensure before running the above file slamtool box is running which provides the /map topic.
To run my launch file i provided map file and param file for navigation



### teleop remapping 
I have prioritized cmd_vel_topic using teleop above cmd_vel topic on which nav2 is publishing velocities
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=cmd_vel_teleop
```
### run localliztion without SLAM 
```bash
ros2 launch nav2_bringup localization_launch.py map:=./src/custom_robot/maps/turtlebothoue.yaml use_sim_time:=true
```

Better way to do this is to copy localization lanch file to the workspace and then run from workspace 


But for testing run navigation launch file with 
```bash
 ros2 launch custom_robot navigation.launch_testing.py use_sim_time:=true map_subscribe_transient_local:=true 
```

or directly from root
```bash
 ros2 launch nav2_bring navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true 
```