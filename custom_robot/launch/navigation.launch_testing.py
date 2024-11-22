import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Directories for map and config files
    config_dir = os.path.join(get_package_share_directory('custom_robot'), 'config')
    map_dir = os.path.join(get_package_share_directory('custom_robot'), 'maps')
    
    # Files for map and parameters
    map_file = os.path.join(map_dir, 'turtlebothoue.yaml') 
    param_file = os.path.join(config_dir, 'nav2_params.yaml')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'navigation_launch.py')]
            ),
            launch_arguments={
                'map': map_file,
                'params_file': param_file,
                'use_sim_time': 'true' 
            }.items(),
        ),
    ])
