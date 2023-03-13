# Multi-robot in ROS2

This is a fundamental repository used when multiple system robots (ROS2) have the same architecture (also the same topics, nodes, ...) within the same network. It can recognize itself and others without conflict. Each robot has a unique name `ROBOT_NAME`. For instance, in this repo, the robot has the name `robot1`.

You can run two robots by cloning this repository in two devices, ensuring both are connected to the same network and changing the different name `ROBOT_NAME` for each robot.

## Usage

To change the different name for each robot, change the `ROBOT_NAME` variable at line 12 in the launch file `multi_machine/launch/multi_launch.py`:
```
ROBOT_NAME = 'robot1'
```

To run launch file:
```
ros2 launch multi_machine multi_launch.py
```

> Note: Make sure you downloaded the repo in your workspace and built it successfully

To check all topics:
```
ros2 topic list
```
Giving:
```
/parameter_events
/robot1/my_topic
/rosout
```

The name topic will be `/robot1/my_topic` where `robot1` is the `ROBOT_NAME` variable you have set in launch file, `my_topic` is your topic name.

To check data the node is received:
```
ros2 topic echo /robot1/my_topic
```