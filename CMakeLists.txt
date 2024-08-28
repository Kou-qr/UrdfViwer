cmake_minimum_required(VERSION 3.5)
project(urdf_viewer)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(rviz2 REQUIRED)

install(
  DIRECTORY urdfModel/launch urdfModel/urdf urdfModel/meshes
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
