<p align="center">
  <a href="" rel="noopener">
 <img src="resources/images/ATR-logo.gif" alt="ATR"></a>
</p>

<h3 align="center">CS 43301/53301: Software Development for Robotics</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![build](https://img.shields.io/badge/build-melodic-green)]()
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Monday and Wednesday from : 11:00 AM to 12:15 PM - MSB 104 Lab room
</p>


## 📝 Project Guide

### Image Detection (YOLO):

in order to use yolo with ROS, we need to modify the `detect.py` with ROS subscriber to make it listen to ROS image instead of webcam on your PC, I made two new file call `yolo_ros.py` and `yolo_ros_connector.py` to replace the original `detect.py`. Everything else is excatly the same.

#### steps on how to use yolo with ROS:

**following steps are just highlight of the difference between `normal yolo` and `ROS yolo`.** the rest of steps are excatly the same the normal yolo

1. clone this repo
1. move all your yolo file into `project_tools/scripts` folder
1. record training video:
    1. install recording software: `sudo apt install vokoscreen`
    1. check out the `training.mp4` video at Slack chanel on how to do it
1. runing detection:
    1. ```
        # terminal 1 
        cd YOUR_PATH_TO_project_ws
        source devel/setup.bash
        roslaunch project_gazebo turtlebot_house_playground.launch
        ```
    1. ```
        # terminal 2
        cd YOUR_PATH_TO_project_ws
        source devel/setup.bash
        rosrun project_tools yolo_ros_connector.py
        ```
    1. ```
        # terminal 3
        cd YOUR_PATH_TO_project_ws
        source devel/setup.bash # you need to do this before you go into sub-folder
        cd src/project_tools/scripts/
        # command below only change the `detect.py` to `yolo_ros.py`. the rest is the same as yolo document
        python3 yolo_ros.py --data datafile.data --cfg yolov3-tiny-1cls.cfg --weights best.pt --source 0
        ```


