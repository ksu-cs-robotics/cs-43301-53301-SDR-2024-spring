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
+ [1. PC Setup](#pc_setup)
+ [2. ROS Installation](#rosinstall)
+ [3. Notes](#notes)

## 💾 1. PC Setup <a name = "pc_setup"></a>
#### 1.1 Personal PC Setup
During this class, we are going to use [Ubuntu 18.04](https://ubuntu.com/download/desktop) as our main operating system. 

- If you already have **Ubuntu 16.04** insteaded, it is *preferable* to upgrade to 18.04 but *not necessary* to do so. 
- If you have a windows operating system, please follow [this link](https://www.youtube.com/watch?v=sB_5fqiysi4) to install **virtual box + ubuntu** on your system.(replace ubuntu *16.04* with *18.04*)
- **\[optional\]** If you have a windows 10 on your system. You call try out [Windows 10 Bash & Linux Subsystem](https://www.youtube.com/watch?v=Cvrqmq9A3tA&t=243s). it is a command line bash based system on windows, it has most function of Ubuntu, but it doesnt provide a GUI interface.(you can use **X Servers** to bypass it, but it is bugyy to use)

#### 1.2 Raspberry PI Setup
Since its not really a good idea to put your laptop/desktop on a *0.2m^3* robot, we are going to use *Raspberry Pi* as our ob board PC. 

- Raspberry Pi 3: Please follow [this video]() link to setup your raspberry pi
- Raspberry Pi 4: Since the offical Ubuntu support for raspberry pi 4 havent come out yet. You can install [Raspbian Buster with desktop](https://www.raspberrypi.org/downloads/raspbian/), the setup process would be the similar as above.
- **DVI type monitor Setup:** 
  ```
  sudo nano /boot/config.txt
  ```
  ```
  ### edit these lines ###
  hdmi_force_hotplug=1
  hdmi_drive=1
  hdmi_group=2
  hdmi_mode=82
  ```

## 🏁 2. ROS Installation <a name = "rosinstall"></a>

ROS(Robot Operating System) is a popular framework for building the software for robot now adays, which we will also use it to build our Robot.

**Please watch this 7 min video before you move on to installation**
https://www.youtube.com/watch?v=YHFzr-akOas

---

do follow steps to update your system first regardless which version of Ubuntu you are using
```
sudo apt update
sudo apt upgrade
```
### 2.1 Ubuntu 16 & ROS Kinetic
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
### 2.2 Ubuntu 18 & ROS Melodic
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


## ✍️ 3. Notes <a name = "notes"></a>

- when using **catkin_make** on raspberry pi:
Use `catkin_make -j2` instead of `catkin_make`
  - *"-j2" means using 2 cores for computing.*
  - *Raspberry pi has 4 core process by default, if didn't use "-j2", it will use all 4 core process to compute, which may result in crash or froze.*

- **CTRL + ALT + T** to open up a **terminal**
---
- **CTRL + ALT + C** to Copy stuff **Inside** terminal
- **CTRL + ALT + Y** to Paste stuff **Inside** terminal
---
- **CTRL + C** to Copy stuff **Outside** terminal
- **CTRL + Y** to Paste stuff **Outside** terminal