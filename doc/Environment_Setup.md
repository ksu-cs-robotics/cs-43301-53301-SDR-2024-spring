<p align="center">
  <a href="" rel="noopener">
 <img src="../resources/images/ATR-logo.gif" alt="ATR"></a>
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
+ [0. Tools](#tools)
+ [1. PC Setup](#pc_setup)
+ [2. ROS Installation](#rosinstall)
+ [3. Notes](#notes)

## 💬 0. Tools <a name = "tools"/>
#### We will use "Github" for homework submision and "Slack" for communication 

#### 0.1 Github: 
GitHub is a global company that provides hosting for software development version control using Git.

Instruction Link: [basic use](https://www.youtube.com/watch?v=SWYqp7iY_Tc)

#### 0.2 Slack
Slack is a cloud-based proprietary instant messaging platform developed by Slack Technologies.

Instruction Link: [basic use](https://www.youtube.com/watch?v=dJmdHowChWk)

### Chanels: 
- **Github:** Please Fork this Repo into your account. if you do not know how to do that, please watch [this video](https://www.youtube.com/watch?v=HbSjyU2vf6Y)

- **Slack:** Please send an emial to Instructor (xlin10@kent.edu) about your Slack handle and email 

## 💾 1. PC Setup <a name = "pc_setup"></a>
#### 1.1 Personal PC Setup
During this class, we are going to use [Ubuntu 18.04](https://ubuntu.com/download/desktop) as our main operating system. 

# BACK UP ALL YOUR IMPORTENT FILES BEFORE YOU CONTINUE

##### 1.1.1. You Already Have Ubuntu 16 or You Want to Wipe Entire PC:

- **CASE 0 - BLANK INSTALL:** 
  check out 1.1.2. CASE 0. do the same thing but skip the first part where you particition on Windows

- **CASE 1 - UPGRADE:** 
  If you already have **Ubuntu 16.04** insteaded, it is *preferable* to upgrade to 18.04.
  ```
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install update-manager-core
  sudo do-release-upgrade
  ``` 

##### 1.1.2. You Already Have Windows and You Dont Want To Wipe Anything:

- **CASE 0 - WINDOWS + UBUNTU (DUAL BOOT):** 
  Dual Booting installs both system. You can run one or the other full speed with full and full features, but only run one at a time.

  Instruction Link: [Dual boot Windows and Ubuntu](https://www.youtube.com/watch?v=u5QyjHIYwTQ) (Choose Option#1 - install ubuntu alongside windows boot manager) 

- **CASE 1 - WINDOWS + VIRTUAL MACHINE (VM):** 
  Running a VM allows running both system at the same time with full features, but slows down the VM (and potentially also the host).

  Instruction Link: [Virtual Box on Windows 10](https://www.youtube.com/watch?v=sB_5fqiysi4) (replace ubuntu *16.04* with *18.04*)

- **CASE 2 - WINDOWS + UBUNTU BASH (WSL):** 
  WSL is APIs and libraries to enable binary compatibility, but you aren't actually running Linux, and some programs are incompatible. Full speed, limited features.

  Instruction Link: [Windows 10 Bash & Linux Subsystem](https://www.youtube.com/watch?v=Cvrqmq9A3tA&t=243s). it does not provide a GUI interface.(you can use **X Servers** to bypass it, but it is bugyy to use)

##### 1.1.3. Install OS on Raspberry pi

- **CASE 0 Raspberry Pi 3:** Please follow [this video]() link to setup your raspberry pi

- **CASE 1 Raspberry Pi 4:** Since the offical Ubuntu support for raspberry pi 4 havent come out yet. You can install [Raspbian Buster with desktop](https://www.raspberrypi.org/downloads/raspbian/), the setup process would be the similar as above.

- **!!->> DVI type monitor Setup: <<-!! (NOTES)** 
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

**Simple But Important Linux Conept and Command Line Tutorial Video (7min)**
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