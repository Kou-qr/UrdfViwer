# UrdfViwer
show the urdf with meshes in rviz by ros2

## install gui
```bash
sudo apt install ros-humble-joint-state-publisher-gui
```

## Use colcon build
```bash
mkdir UrdfViwer
cd ~/UrdfViwer
git clone git@github.com:Sher1ockFan/UrdfViwer.git
mv UrdfViwer/ src/
colcon build
```
## Before run the rviz
replace the meshes path with
package://urdf_rviz/meshes

## Use roslaunch to run rviz with model
```bash
. install/setup.bash
ros2 launch urdf_viewer display.launch.py
```