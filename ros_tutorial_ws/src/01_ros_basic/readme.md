# 01_ros_basic

## How to run

```
# navigate to ros_tutorial_ws
cd ros_tutorial_ws
# builds the '01_ros_basic' package and its dependencies in the 'ros_tutorial_ws' directory
catkin_make --only-pkg-with-deps 01_ros_basic
# setup environment
source devel/setup.bash
# run ros script
rosrun 01_ros_basic hello_node.py
```

You should be able to see:

```
hello ros python
hello ros python
hello ros python
hello ros python
```

## Debugging

If you see the following errors: 

```
Command 'pip' not found, but there are 18 similar ones.
```

Or:

```
ImportError: No module named yaml
```

Or:

```
No module named 'rospkg'
```

Try the following commands:

```
pip install rospkg
sudo apt install python-is-python3
```

