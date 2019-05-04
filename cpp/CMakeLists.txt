cmake_minimum_required(VERSION 3.13)
include(CheckCXXCompilerFlag)

project(cholesky)

set(CMAKE_CXX_STANDARD 14)

if(WIN32)
	#set(Boost_DEBUG ON)
	set(Boost_COMPILER -vc142)
	set(Boost_USE_STATIC_LIBS        ON)

	set(BOOST_LIBRARYDIR "D:/Programmi/boost_1_70_0/lib64-msvc-14.2")

	add_definitions(-DBOOST_ALL_NO_LIB)
endif()

option(OPTIMIZE_FOR_NATIVE "Build with -march=native" OFF)

if(OPTIMIZE_FOR_NATIVE)
    CHECK_CXX_COMPILER_FLAG("-march=native" COMPILER_SUPPORTS_MARCH_NATIVE)

    if(COMPILER_SUPPORTS_MARCH_NATIVE)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
    else()
        message(SEND_ERROR "Requested building with -march=native but compiler doesn't support it" )
    endif()
endif()

find_package(Eigen3  3.3 REQUIRED NO_MODULE)
find_package(Boost  1.68 REQUIRED COMPONENTS filesystem iostreams zlib)

add_executable(cholesky-cpp main.cpp)
target_include_directories(cholesky-cpp SYSTEM PRIVATE ${Boost_INCLUDE_DIRS})
target_link_libraries(cholesky-cpp Eigen3::Eigen ${Boost_LIBRARIES})
