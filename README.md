# UrdfViwer
show the urdf with meshes in rviz

## Use catkin build
```bash
mkdir UrdfViwer
cd ~/UrdfViwer
git clone git@github.com:Sher1ockFan/UrdfViwer.git
catkin build
```

## Use roslaunch to run rviz with model
```bash
. devel/setup.bash
roslaunch urdf_tutorial display.launch model:./src/urdf_model/inspire_hands.urdf