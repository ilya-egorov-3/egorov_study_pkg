#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='normal',
        description='Режим: normal (8 Гц, 80, /even_numbers), fast (20 Гц, 50, /even_numbers_fast), slow (5 Гц, 150, /even_numbers_slow)'
    )

    mode = LaunchConfiguration('mode')

    frequency = PythonExpression([
        "20.0 if '", mode, "' == 'fast' else "
        "8.0 if '", mode, "' == 'normal' else "
        "5.0"
    ])

    threshold = PythonExpression([
        "50 if '", mode, "' == 'fast' else "
        "80 if '", mode, "' == 'normal' else "
        "150"
    ])

    topic = PythonExpression([
        "'/even_numbers_fast' if '", mode, "' == 'fast' else "
        "'/even_numbers' if '", mode, "' == 'normal' else "
        "'/even_numbers_slow'"
    ])

    publisher_node = Node(
        package='study_pkg',
        executable='even_number_publisher',
        name='even_pub',
        parameters=[{
            'frequency': frequency,
            'overflow_threshold': threshold,
            'topic_name': topic
        }],
        output='screen'
    )

    listener_node = Node(
        package='study_pkg',
        executable='overflow_listener',
        name='overflow_listener',
        parameters=[{
            'topic_name': '/overflow'
        }],
        output='screen'
    )

    return LaunchDescription([
        mode_arg,
        publisher_node,
        listener_node
    ])
