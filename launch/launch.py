import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():

    gen3n7_description_dir = get_package_share_directory("gen3n7_description")

    model_arg = DeclareLaunchArgument(
        name="model", 
        default_value=os.path.join(gen3n7_description_dir, "urdf", "gen3n7.urdf"), 
        description="Absolute path to the robot URDF file"
    )

    with open(os.path.join(gen3n7_description_dir, "urdf", "gen3n7.urdf"), "r") as urdf_file:
        robot_description_content = urdf_file.read()

    robot_description = ParameterValue(
        robot_description_content, 
        value_type=str
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}]
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz_node = Node(
        package="rviz2", 
        executable="rviz2", 
        name="rviz2", 
        output="screen",
        arguments=["-d", os.path.join(get_package_share_directory("gen3n7_description"), "rviz", "config.rviz")]
    )

    return LaunchDescription([
        model_arg, 
        robot_state_publisher,
        joint_state_publisher_gui, 
        rviz_node
    ])