# description
This is a package that combines darknet_ros and iai_kinect2 in order to get the 3D location of the object.
It will automatically send the tf transform between the kinect2_link and the objects detected.

![a](/imgs/a.jpeg)
![b](/imgs/b.jpeg)

# system requirement
only tested on
* Ubuntu 20.04 (ROS Noetic)
* remember to downgrade your gcc and g++ version of your system to 7(my Ubuntu 20.04 default 8)

# dependencies
[libfreenect2](https://github.com/OpenKinect/libfreenect2)

python3-pcl
```sh
pip3 install python3-pcl
```
ros_numpy
```sh
sudo apt-get install ros-noetic-ros-numpy
```
cuda(optional but recommended)

[darknet_ros](https://github.com/0nhc/darknet_ros.git)

[iai_kinect2](https://github.com/0nhc/iai_kinect2.git)

# how to use

```sh
cd <your_ws>/src
git clone --recursive https://github.com/0nhc/darknet_ros.git
git clone https://github.com/0nhc/iai_kinect2.git
git clone https://github.com/0nhc/depth_yolo.git
cd ..
catkin_make -DCMAKE_BUILD_TYPE="Release"
source devel/setup.bash
roslaunch depth_yolo depth_yolo.launch
```
