# ros_smart_grasping_pkgs

The repository was build as part of the MSc. Master Project course for the MSc. Software Development program of the University of Glasgow in summer 2018. It contains two ROS packages that were build to be used with the [Shadow Robotics Smart Grasping Sandbox Simulation](https://www.shadowrobot.com/we-built-an-open-sandbox-for-training-robotic-hands-to-grasp-things/) (10.08.2018).This simulation is available as a Docker container and uses Cloud 9 by AWS as an built-in IDE and Gazebo as the simulation software. The packages enable users to gather camera data and use these data to execute grasps in the simulation. 

## Development Groundwork

The ROS packages were build using the Shadow Robotic's sandbox simulation:

https://github.com/shadow-robot/smart_grasping_sandbox.git 

from 29.06.2018.

## Packages Architecture 

IMAGE OF THE SYSTEM ARCHITECTURE MODEL 
  
 As shown in the model above the the system was divided into two parts. Gathering camera data and object grasping. The data gathering nodes subscribe to ROS topics published by hardware devices. The object grasping nodes publish and subscribe to data they provide on their own. Both packages are descirbed in more detail below. 

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

2. Run the latest Docker Hub image

```
docker run -it --name sgs -p 8080:8080 -p 8888:8888 -p 8181:8181 -p 7681:7681 rebor94/robotic_grip_grab_shadow_robotics
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

Otherwise you might need to restart the simulation. The files saved by the nodes in the camera_data package can be found in the following directory: 

```
/workspace/src/ros_smart_grasping_pkgs/camera_data/imgs/
```

In the case of this package images are saved as .png files and information are saved as .txt files. 

SCREENSHOT OF COLOR IMAGE
  
SCREENSHOT OF DEPTH IMAGE
  
SCREENSHOT OF CAMERA INFO 

## Run the object_grasping package 

The grasping package contains two nodes. One node calls a neural network to gather information about pose estimations about objects in the scene the Kinect camera captures. It then publishes there estimation as Pose objects. The other node subscribes to these published pose estimations and uses these grasp the objects in the scene. It therefore uses the SmartGrasper library provided by Shadow Roboitcs. 

To run one of the nodes use: 

```
rosrun object_grasping <node_name> 
```

If you run the object_grasper node, you need to change tabs to the Gazebo simulation to be able to see the movement of the robotic arm. 

## nn_connector node (in further detail) 

To enable smart grasping without the need to train robots on specific objects this project was aimed to provide the groundwork to combine the use of neural networks with grasp enabled robots. The nn_connector node was build to gather the needed information from a neural network and provide these to other node the execute grasps. In that context the neural network uses the data gathered by the camera_data nodes and provides pose estimations. 

The neural network itself is not yet specified and can be chosen freely. The only constraints would be to use neural networks that use color images and depth images as input and provide positional vectors as an output. 

## Run the unit tests 

## Run the integration tests 
