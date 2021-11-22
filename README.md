```sh
cd <your_ws>/src
git clone --recursive https://github.com/0nhc/depth_yolo.git
cd ..
catkin_make -DCMAKE_BUILD_TYPE="Release"
source devel/setup.bash
roslaunch depth_yolo depth_yolo.launch
```
