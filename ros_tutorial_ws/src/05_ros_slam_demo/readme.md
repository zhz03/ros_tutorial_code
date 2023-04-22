# SLAM Simulation

In this demo, you can try the SLAM algorithm by yourself using the [TurtleBot](https://www.turtlebot.com/) simulation.

## 1 Install TurtleBot3

```
sudo apt-get install ros-melodic-turtlebot3-*
# 安装地图算法依赖
apt-get install ros-melodic-gmapping 
# 安装dwa路径规划算法
apt-get install ros-melodic-dwa-local-planner 


sudo apt-get install ros-melodic-turtlebot3-*
# Install mapping algorithm dependency
apt-get install ros-melodic-gmapping 
# Install dwa path planning algorithm 
apt-get install ros-melodic-dwa-local-planner 
```

## 2 Control TurtleBot

You need to install some dependency first:

```
sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control
sudo apt-get install ros-melodic-teleop-twist-keyboard 
```

Then we need to activate turtleBot in the simulation environment:

```
export TURTLEBOT3_MODEL=waffle_pi
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

Next, execute the following command to control the little car:

```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

## 3 Construct SLAM

