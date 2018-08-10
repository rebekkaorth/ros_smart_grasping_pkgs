# ros_smart_grasping_pkgs
packages to use into shadow robotics sandbox simultation

This repository contains two ROS packages that were build to be used with the [Shadow Robotics Smart Grasping Sandbox Simulation](https://www.shadowrobot.com/we-built-an-open-sandbox-for-training-robotic-hands-to-grasp-things/) (10.08.2018).This simulation is available as a Docker container and uses Cloud 9 by AWS as an built-in IDE and Gazebo as the simulation software. 

## Development groundwork

The ROS packages were build using the Shadow Robotic's sandbox simulation:

https://github.com/shadow-robot/smart_grasping_sandbox.git 

from 29.06.2018.

## Get and run the Docker container 

To use these packages, you first need to ensure that you have installed [Docker]() on the machine, you want to use. 

Then you have two ways to run them: 

1. Run the simulation using the Sahdow Robotic's Docker Hub repository and clone these packages into the IDE 

Start the Shadow Robotic's simulation

```
docker run -it --name sgs -p 8080:8080 -p 8888:8888 -p 8181:8181 -p 7681:7681 shadowrobot/smart_grasping_sandbox
```

Open your favorite browser and open: 

```
localhost:8080/ 
```

to see the simulation in Gazebo' 

Open a new tab with 

```
localhost:8181/
```

to see the Cloud 9 IDE. 

When you have opened the Cloud 9 tab, the terminal should have been opened already. Ensure that your an in the: 

```
/workspace/src
```

directory. And clone this directory with: 

```
git clone https://github.com/rebekkaorth/ros_smart_grasping_pkgs.git
```

## Run the camera_data package

The camera_data package contains files to save different information provided by the Kinect camera in separate files in the img-folder. For each of the different information that can be saved, different nodes can be ran to get the information. 

To run the nodes ensure that you are still in the 

```
/workspace/src
```

directory. To ensure that the needed topics are available, you should check all currently available topics by calling: 

```
rostopic list
```
Then ensure that you find '/kinect/' topics in that list.  
If that is the case run: 

```
rosrun camera_data <node_name>
```

Otherwise you might need to restart the simulation. 

## Run the object_grasping package 

## Run the unit tests 

## Run the integration tests 
