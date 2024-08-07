# UrdfViwer
show the urdf with meshes in rviz

## Use catkin build
```bash
cd ~/UrdfViwer
catkin build
```

## Use roslaunch to run rviz with model
```bash
. devel/setup.bash
roslaunch urdf_tutorial display.launch model:./src/urdf_model/inspire_hands.urdf