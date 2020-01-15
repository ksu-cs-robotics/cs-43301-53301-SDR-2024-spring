<p align="center">
  <a href="" rel="noopener">
 <img src="resources/images/ATR-logo.gif" alt="ATR"></a>
</p>

<h3 align="center">Software Development for Robotics</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![build](https://img.shields.io/badge/build-melodic-green)]()
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> this repo contains the steps for setup your environment and necessary source code for the class
</p>


## 📝 Table of Contents
+ [1. Course Overview](#overview)
+ [2. PC Setup](#pc_setup)
+ [3. ROS Setup](#ros_setup)
+ [4. Notes](#notes)
+ [5. Assignments](#assignments)
+ [6. Projects](#projects)


## 🏁 1. Course Overview <a name = "overview"></a>
&emsp;This course will teach the students fundamentals of robotics along with various software, hardware for robot developments based on the Robot Operating System (ROS) which is a flexible framework for writing robot software. It is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robotic platforms.

&emsp;This course will provide hands-on experience with lab activities and practical knowledge from semester-long projects. During the semester, the students will build a Battle Bot based on a customized TurtleBot with ROS. And the class will host a battle bot competition at the end of the semester as a part of the class. This is a [demo video](https://youtu.be/F-Cr1E8kr7c ) 


## 💾 2. Environment Setup <a name = "pc_setup"></a>
### 2.1 PC Setup
#### 2.1.1 Personal PC Setup
During this class, we are going to use [Ubuntu 18.04](https://ubuntu.com/download/desktop) as our main operating system. 

- If you already have **Ubuntu 16.04** insteaded, it is *preferable* to upgrade to 18.04 but *not necessary* to do so. 
- If you have a windows operating system, please follow [this link](https://www.youtube.com/watch?v=sB_5fqiysi4) to install **virtual box + ubuntu** on your system.(replace ubuntu *16.04* with *18.04*)
- **\[optional\]** If you have a windows 10 on your system. You call try out [Windows 10 Bash & Linux Subsystem](https://www.youtube.com/watch?v=Cvrqmq9A3tA&t=243s). it is a command line bash based system on windows, it has most function of Ubuntu, but it doesnt provide a GUI interface.(you can use **X Servers** to bypass it, but it is bugyy to use)

#### 2.1.2 Raspberry PI Setup
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
## 🚀 3. ROS Setup <a name = "ros_setup"></a>
ROS(Robot Operating System) is a popular framework for building the software for robot now adays, which we will also use it to build our Robot.
- if you are installing ROS on **Ubuntu 16.04** (Personal PC or Raspberry pi). you can follow [this link](doc/ROSinstall.md) to install
- if you are installing ROS on **Ubuntu 18.04** (Personal PC or Raspberry pi). you can follow [this link](doc/ROSinstall.md) to install
- if you are installing ROS on **Raspbian** (Raspberry pi). you can follow [this link](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi) to install

## ✍️ 4. Notes <a name = "notes"></a>
1. when using **catkin_make** on raspberry pi:
Use `catkin_make -j2` instead of `catkin_make`
```
"-j2" means using 2 cores for computing.
Raspberry pi has 4 core process by default, if didn't use "-j2", it will use all 4 core process to compute, which may result in crash or froze.
```