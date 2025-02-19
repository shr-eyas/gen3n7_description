cmake_minimum_required(VERSION 3.8)
project(gen3n7_description)

find_package(ament_cmake REQUIRED)
find_package(rviz_default_plugins REQUIRED)

install(
  DIRECTORY urdf launch meshes rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()