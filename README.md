# ros_smart_grasping_pkgs
packages to use into shadow robotics sandbox simultation

This repository contains two ROS packages that were build to be used with the [Shadow Robotics Smart Grasping Sandbox Simulation](https://www.shadowrobot.com/we-built-an-open-sandbox-for-training-robotic-hands-to-grasp-things/) (10.08.2018).This simulation is available as a Docker container and uses Cloud 9 by AWS as an built-in IDE and Gazebo as the simulation software. 

## Development groundwork

The ROS packages were build using the Shadow Robotic's sandbox simulation:

https://github.com/shadow-robot/smart_grasping_sandbox.git 

from 29.06.2018.

## Get the Docker container 

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



## Start the container 

## Use the simulation 
