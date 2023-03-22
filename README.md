![ROS1 VERSION](https://img.shields.io/badge/ROS-ROS%201%20Noetic-brightgreen)
&nbsp;
[![Ubuntu VERSION](https://img.shields.io/badge/Tested-Ubuntu%2020.04-green)](https://ubuntu.com/)
&nbsp;
![LICENSE](https://img.shields.io/badge/license-GPL%203-informational)
&nbsp;

# Description
This is a package combining darknet_ros and iai_kinect2 in order to get the 3D location of the objects detected.

It will automatically send tf transforms between the objects detected and kinect2_link.

![b](imgs/b.jpeg)
  


# Installation
## step1 Install dependencies
1. Remember to downgrade the gcc and g++ version of your system to 7 (my Ubuntu 20.04 is default 8)
2. [libfreenect2](https://github.com/OpenKinect/libfreenect2.git) (follow the official steps to install libfreenect2)
3. python3-pcl (if you are using Ubuntu 18.04 with ROS Melodic, pip install python-pcl)
```bash
pip install python3-pcl
```

4. ros_numpy (if you are using Ubuntu 18.04 with ROS Melodic, sudo apt-get install ros-melodic-ros-numpy)
```bash
sudo apt-get install ros-noetic-ros-numpy
```
5. [darknet_ros](https://github.com/0nhc/darknet_ros) (This links to my forked repo. I modified it for supporting my RTX 30 laptop)
6. [iai_kinect2](https://github.com/0nhc/iai_kinect2) (This links to my forked repo. I modified it for supporting Ubuntu 20.04)
## step2 Clone the dependencies packages
If you haven't cloned the dependencies packages yet, clone them in your workspace first.

```bash
cd <your_ws>/src
git clone --recursive https://github.com/0nhc/darknet_ros.git
git clone https://github.com/0nhc/iai_kinect2.git
```
## step3 install depth_yolo
Then, you can continue installing depth_yolo
```bash
git clone https://github.com/0nhc/depth_yolo.git
cd ..
catkin_make -DCMAKE_BUILD_TYPE=Release
source devel/setup.bash
```
# Usage

It will automatically launch darknet_ros node(yolo v3) and kinect2_bridge.
```bash
roslaunch depth_yolo depth_yolo.launch
```
# Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.



# License
This project is licensed under the GPL 3 License. See [LICENSE](LICENSE) for more information.
```
    Copyright (C) 2023  0nhc

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.If not, see <https://www.gnu.org/licenses/>.                               
```

# Acknowledgments 
I would like to thank the following people for their contributions to this project:

- **Herman Ye**  

  I would like to take a moment to express my sincere gratitude to Herman Ye for his invaluable contribution to this project's README. His attention to detail and clear communication have greatly improved the overall quality of the documentation, making it easier for others to understand and contribute to the project.  
  Herman Ye's dedication and hard work have not gone unnoticed, and I am truly grateful for his efforts. Thank you, Herman Ye, for your outstanding work and for being an integral part of this project's success.for implementing the search functionality.


