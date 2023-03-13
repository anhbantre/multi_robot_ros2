import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command, PythonExpression

ROBOT_NAME = 'robot1'

def generate_launch_description():

    launch = LaunchDescription()

    node_1 = Node(
        package = "multi_machine",
        executable = "node_1",
        name = f"node_1_{ROBOT_NAME}",
        parameters = [
            {'robot_name': ROBOT_NAME},
            {'my_param': "param1"}
        ],
    )

    launch.add_action(node_1)

    return launch