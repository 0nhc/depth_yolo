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

# how to use
remember to downgrade your gcc and g++ version of your system to 7(Ubuntu 20.04 default 8)
```sh
cd <your_ws>/src
git clone --recursive https://github.com/0nhc/depth_yolo.git
cd ..
catkin_make -DCMAKE_BUILD_TYPE="Release"
source devel/setup.bash
roslaunch depth_yolo depth_yolo.launch
```
