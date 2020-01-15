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

<p align="center"> ROS Installation
</p>


## 📝 Table of Contents
+ [1. ROS Installation](#rosinstall)
+ [2. Notes](#notes)


## 🏁 1. ROS Installation <a name = "rosinstall"></a>
**Please watch this 7 min video before you move on to installation**
https://www.youtube.com/watch?v=YHFzr-akOas

---

do follow steps to update your system first regardless which version of Ubuntu you are using
```
sudo apt update
sudo apt upgrade
```
### 1.1 Ubuntu 16 & ROS Kinetic
here is the more detail explanation of how to [install ROS on ubuntu 16](http://wiki.ros.org/kinetic/Installation/Ubuntu)

here is simplify version if you are having trouble following the tutorial link:
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt-get update

sudo apt-get install ros-kinetic-desktop-full

sudo rosdep init

rosdep update

echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

source ~/.bashrc

sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```
### 1.2 Ubuntu 18 & ROS Melodic
here is the more detail explanation of how to [install ROS on ubuntu 18](http://wiki.ros.org/melodic/Installation/Ubuntu)

here is simplify version if you are having trouble following the tutorial link:
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt update

sudo apt install ros-melodic-desktop-full

sudo rosdep init

rosdep update

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

source ~/.bashrc

sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```


## ✍️ 2. Notes <a name = "notes"></a>

- **CTRL + ALT + T** to open up a **terminal**
---
- **CTRL + ALT + C** to Copy stuff **Inside** terminal
- **CTRL + ALT + Y** to Paste stuff **Inside** terminal
---
- **CTRL + C** to Copy stuff **Outside** terminal
- **CTRL + Y** to Paste stuff **Outside** terminal