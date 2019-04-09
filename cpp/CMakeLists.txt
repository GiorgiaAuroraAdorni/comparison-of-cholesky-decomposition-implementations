cmake_minimum_required(VERSION 3.13)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

find_package(Eigen3  3.3 REQUIRED NO_MODULE)
find_package(Boost  1.68 REQUIRED COMPONENTS iostreams)

add_executable(cpp main.cpp)
target_include_directories(cpp SYSTEM PRIVATE ${Boost_INCLUDE_DIRS})
target_link_libraries(cpp Eigen3::Eigen ${Boost_LIBRARIES})
