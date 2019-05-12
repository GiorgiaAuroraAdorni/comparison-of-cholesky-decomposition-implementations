cmake_minimum_required(VERSION 3.10)
include(CheckCXXCompilerFlag)

project(cholesky)

set(CMAKE_CXX_STANDARD 14)

option(OPTIMIZE_FOR_NATIVE "Build with -march=native" OFF)
option(OPTIMIZE_FOR_AVX2 "Build for AVX2" OFF)

if(OPTIMIZE_FOR_NATIVE)
    CHECK_CXX_COMPILER_FLAG("-march=native" COMPILER_SUPPORTS_MARCH_NATIVE)

    if(COMPILER_SUPPORTS_MARCH_NATIVE)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")
    else()
        message(SEND_ERROR "Requested building with -march=native but compiler doesn't support it")
    endif()
endif()

if(OPTIMIZE_FOR_AVX2)
    CHECK_CXX_COMPILER_FLAG("/arch:AVX2 /EHsc" COMPILER_SUPPORTS_AVX2_MSVC)

    if(COMPILER_SUPPORTS_AVX2_MSVC)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /arch:AVX2 /EHsc")
    else()
        message(SEND_ERROR "Requested building for AVX2 but compiler doesn't support it")
    endif()
endif()

if(WIN32)
	# Since building for Windows requires Visual Studio, we want to build once and just copy the executable
	# on the test systems. Statically linking Boost makes it easier.
	set(Boost_USE_STATIC_LIBS ON)
endif()

find_package(Eigen3  3.3 REQUIRED NO_MODULE)
find_package(Boost  1.65 REQUIRED COMPONENTS filesystem iostreams)

link_directories(${Boost_LIBRARY_DIRS})

add_executable(cholesky-cpp main.cpp)
target_include_directories(cholesky-cpp SYSTEM PRIVATE ${Boost_INCLUDE_DIRS})
target_link_libraries(cholesky-cpp Eigen3::Eigen ${Boost_LIBRARIES})
