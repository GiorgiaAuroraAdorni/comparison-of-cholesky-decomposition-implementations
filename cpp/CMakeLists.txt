cmake_minimum_required(VERSION 3.13)
project(cholesky)

set(CMAKE_CXX_STANDARD 14)

set(Boost_COMPONENTS filesystem iostreams)

if(WIN32)
	set(Boost_USE_STATIC_LIBS ON)
	
	list(APPEND Boost_COMPONENTS zlib)
endif()

find_package(Eigen3  3.3 REQUIRED NO_MODULE)
find_package(Boost  1.68 REQUIRED COMPONENTS ${Boost_COMPONENTS})

add_executable(cholesky-cpp main.cpp)
target_include_directories(cholesky-cpp SYSTEM PRIVATE ${Boost_INCLUDE_DIRS})
target_link_libraries(cholesky-cpp Eigen3::Eigen ${Boost_LIBRARIES})
