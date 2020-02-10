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

<p align="center"> Class Notes
</p>

## 📝 Table of Contents
+ [1. Important Notes](#important)
+ [2. Aditional Notes](#additional)

## ✒️ Important Notes: <a name = "important"></a>

1. **Addition link:**
    - ROS offical Tutorial: http://wiki.ros.org/ROS/Tutorials

1. **Important Command for Working with Ubuntu**
    - **CTRL + ALT + T** to open up a **terminal**
    - **CTRL + ALT + C** to Copy stuff **Inside** terminal
    - **CTRL + ALT + Y** to Paste stuff **Inside** terminal
    - **CTRL + C** to Copy stuff **Outside** terminal
    - **CTRL + Y** to Paste stuff **Outside** terminal

1. **Notes on working with Raspberry pi**

    1. if raspberry pi freeze or something suppose to work but doesn't work, try **unplug and plug back in**, if that doesn't solve the problem, try **google**

    2. when you do ```catkin_make``` on raspberry pi, use ```catkin_make -j2``` instead, **-j2** is gonna force raspberry pi only to use two core of CPU to compile. because raspberry dont have enough computing power, it will easily freeze if you dont use **-j2**

1. **command for check IP address:**

    the IP address of your PC may change when you in a different network. even when you in the same network, IP may also change from time to time
    - **ifconfig**    (linux)
    - **ipconfig**    (windows)

1. **Setup your connection with ROS Master:**
    - gedit ~/.bashrc **OR** nano ~/.bashrc
        - Enter these at the Bottom of your ~/.bashrc script:
            ```
                export ROS_IP=your.ip.address.here
                export ROS_MASTER_URI=http://master.ip.address.here:11311
                export ROS_HOSTNAME=your.ip.address.here
            ```

## 🖊️ Aditional Notes: <a name = "additional"></a>

1. **communicate your VirtualBox with ROS Master on other PC:**
<img src = "../resources/images/random/network_virtualbox.png">

1. **Turtlebot3 Test and Play:**

    official manual page: http://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#turtlebot3-simulation-using-fake-node
    1. install: 
    ```sudo apt install ros-melodic-turtlebot3* ros-melodic-teleop-twist-keyboard ```

    2. Run Simulation: (you can run both on your PC when you test on your own)
        - **one PC:**
        ```
        export TURTLEBOT3_MODEL=waffle_pi
        roslaunch turtlebot3_gazebo multi_turtlebot3.launch
        ```
        - **another PC:**
        ```
        rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=tb3_2/cmd_vel
        ## check the instruction show up on terminal when you run this code and try to control the robot.
        ```

1. **face detection:**
    check out [this library](https://pypi.org/project/face_recognition/)