<p align="center">
  <a href="" rel="noopener">
 <img src="https://raw.githubusercontent.com/ksu-cs-robotics/Software-Development-for-Robotics/master/resources/images/ATR-logo.gif" alt="ATR"></a>
</p>

<h3 align="center">Software Development for Robotics</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![build](https://img.shields.io/badge/build-melodic-green)]()
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Final Projects
</p>

## 🏁 Individual Project

### Simulation:

### The project folder is locate at [HERE](https://github.com/ksu-cs-robotics/Software-Development-for-Robotics/tree/master/src/project_ws)

#### install missing package
```
sudo apt install ros-melodic-turtlebot3*
sudo apt install ros-melodic-dwa-local-planner
sudo apt install ros-melodic-gmapping
```

#### commands for launch individual project playground

##### Personal PC:
launch the gazebo environment with single robot inside
```
export TURTLEBOT3_MODEL=waffle_pi
roslaunch project_gazebo single_robot.launch
```
launch autonomous driving package
```
export TURTLEBOT3_MODEL=waffle_pi
roslaunch project_navigation single_AmclStack.launch
```

##### Raspberry pi:
launch rviz for autonomous driving and visualize
```
roslaunch project_navigation rviz_single_robot.launch
```
launch teleop to control the robot
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=tb3_0/cmd_vel
```

### Goal:

1. change all topic name from **/tb3_0/TOPIC_NAME** to **/YOUR_NAME/TOPIC_NAME** (for example: /tb3_0/odom to /shawn/odom)

    (hint: look into how **group** tag work and how **prefix** work in ROS)

1. make sure the autonomous driving function still works after you are done with the first one.

1. detecting different color in Gazebo environment then modify original image and publish result to new topics: "YOUR_NAME/color_detected" (for colors detected, such as "red", "yellow", "green"); "YOUR_NAME/modified_image" (for the new modified image).

    you only need to detect whatever colors in the middle of your screen

    (hint: subscribe to original image topic, and publish modified image to a new topic)


when there is no color in the middle of your screen
<img src="https://raw.githubusercontent.com/ksu-cs-robotics/Software-Development-for-Robotics/master/resources/images/not_found.png" alt="not_found">

when there are colors in the middle of your screen
<img src="https://raw.githubusercontent.com/ksu-cs-robotics/Software-Development-for-Robotics/master/resources/images/found.png" alt="found">

### Physcial Robot:
make sure you are able to use teleop to control robot, see document [**HERE**](https://github.com/ksu-cs-robotics/Software-Development-for-Robotics/blob/master/doc/ATR_Bot.md)

## ✍️ Group Project
1. randomly spawn robot from location (1-3)
2. autonomous moving robot from location start to end
3. detecting color on the way
4. stop at "STOP" and detect the real size of selected color (ex: 10*20 cm)

<img src="https://raw.githubusercontent.com/ksu-cs-robotics/Software-Development-for-Robotics/master/resources/images/group_project.jpg" alt="group_project">