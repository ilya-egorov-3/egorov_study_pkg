import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ilya3/ros2_ws/src/study_pkg/install/study_pkg'
