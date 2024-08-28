from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # 获取当前脚本所在的目录
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # 拼接出 URDF 文件的完整路径
    urdf_file = os.path.join(current_dir, '../urdf/inspire_hands.urdf')
    rviz_config_file = os.path.join(current_dir, 'robot.rviz')

    # 检查 URDF 文件是否存在
    if not os.path.exists(urdf_file):
        raise FileNotFoundError(f"URDF file not found: {urdf_file}")

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        )
    ])
