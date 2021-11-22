# Description
This is a package combining darknet_ros and iai_kinect2 in order to get the 3D location of the objects detected.

It will automatically send tf transforms between the objects detected and kinect2_link.

![b](imgs/b.jpeg)

# System Requirements
* I only tested it on Ubuntu 20.04
* Remember to downgrade the gcc and g++ version of your system to 7 (my Ubuntu 20.04 is default 8)

# Dependencies
* [libfreenect2](https://github.com/OpenKinect/libfreenect2.git) (follow the official steps to install libfreenect2)
* python3-pcl
```sh
pip install python3-pcl
```

* ros_numpy
```sh
sudo apt-get install ros-noetic-ros-numpy
```

* [darknet_ros](https://github.com/0nhc/darknet_ros) (This links to my forked repo. I modified it for supporting my RTX 30 laptop)
* [iai_kinect2](https://github.com/0nhc/iai_kinect2) (This links to my forked repo. I modified it for supporting Ubuntu 20.04)

# Installation
```sh
cd <your_ws>/src
```

If you haven't cloned the dependencies packages yet, clone them first.
```sh
git clone --recursive https://github.com/0nhc/darknet_ros.git
git clone https://github.com/0nhc/iai_kinect2.git
```

Then, you can continue installing depth_yolo
```sh
git clone https://github.com/0nhc/depth_yolo.git
cd ..
catkin_make -DCMAKE_BUILD_TYPE=Release
source devel/setup.bash
```

# Launch it
It will automatically launch darknet_ros node(yolo v3) and kinect2_bridge.
You can see the pointclouds and tf transforms in rviz manually.
```sh
roslaunch depth_yolo depth_yolo.launch
```
