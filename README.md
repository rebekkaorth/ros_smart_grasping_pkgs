# ROS Smart Grasping Packages

The repository was build as part of the MSc. Master Project course for the MSc. Software Development program of the University of Glasgow in summer 2018. It contains two ROS packages that were build to be used with the [Shadow Robotics Smart Grasping Sandbox Simulation](https://www.shadowrobot.com/we-built-an-open-sandbox-for-training-robotic-hands-to-grasp-things/) (10.08.2018).This simulation is available as a Docker container and uses Cloud 9 by AWS as an built-in IDE and Gazebo as the simulation software. The packages enable users to gather camera data and use these data to execute grasps in the simulation. 

## Development Groundwork

The ROS packages were build using the Shadow Robotic's sandbox simulation:

https://github.com/shadow-robot/smart_grasping_sandbox.git 

from 29.06.2018.

## Project 

### Package Architecture 

Path overview: 

![alt tag](https://github.com/rebekkaorth/ros_smart_grasping_pkgs/blob/master/screenshots/path_overview.png "pather overview")

In addition to the path overview a package architecture model has been created to give a detailed overview: 

![alt tag](https://github.com/rebekkaorth/ros_smart_grasping_pkgs/blob/master/screenshots/package_overview.png "package overview")
  
As shown in the model above the the system was divided into two parts. Gathering camera data and object grasping. The data gathering nodes subscribe to ROS topics published by hardware devices. The object grasping nodes publish and subscribe to data they provide on their own. Both packages are descirbed in more detail below. 

### Requirements 

During a meeting with the project's supervisor the following clients and users could be defined: 

Client: CVAS group (Univeristy of Glasgow)

User: research students (School of Computer Science - University of Glasgow) 

The requirements for the developed system were gathered in consultation with the project supervisor as well as during a conducted research regarding the needed specifications of such a system. With the client and future user in mind, the following requirements could be worked out: 

Prioritisation: 

Must-Have:
- saving color images
- saving depth images
- saving camera information
- move robotic arm to a certain position

Should-Have:
- connector between sandbox and neural network
    
Could_Have:
- creator of datasets
- move robotic arm around the object
    
Would-Like-To-Have:
- mount camera on robotic arm 
- implementation of neural network 
  
### User Stories 

Must-Have: 
  
Title: "Color Image Saver"

Story: "As a user I want to run a node that saves color images as png from the object at hand in a separate directory."
  
Title: "Depth Image Saver"

Story: "As a user I want to run a node that saves depth images as png from the object at hand in separate directory."
  
Title: "Camera Info Saver"

Story: "As a user I want to run a node that saves camera information as txt in a separate directory"
  
Title: "Object grasper"

Story: "As a user I wantto run a node that moves the robotic arm to the position of the object and grasps it. The arm should
         then carry the object to a specific position"


Should-Have:

Title: "Neural Network Connector"

Story: "As a user I want to run a node that uses saved images to call a neural network and publish pose predictions"

Could-Have:

Title: "Dataset Maker"

Story: "As a user I want to run a node that takes several color and depth images as well as camera information in a
          separate directory"
          
Title: "Move Around Object"

Story: "As a user I want to run a node that moves a robotic arm around an object"

Would-Like-To-Have:

Title: "Camera On Robotic Arm"

Story: "As a user I want to use a camera that is connected to a robotic arm, so it can be moved around"
  
Title: "Neural Network implemnetation"

Story: "As a user I want to have a neural network, that is able to predict object poses, within the sandbox"

### System Architecture

UML Diagram: 
![alt tag](https://github.com/rebekkaorth/ros_smart_grasping_pkgs/blob/master/screenshots/UML_Ros_SmartGraspingPkgs.png "pather overview")

## Project Plan

A detail project plan with details about what part of the project was developed when, can be found here : https://github.com/rebekkaorth/robitics_pick_n_place_masterproject/projects/1


## Get and run the Docker container 

To use these packages, you first need to ensure that you have installed [Docker](https://www.docker.com) on the machine, you want to use. 

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
docker run -it --name sgs -p 8080:8080 -p 8888:8888 -p 8181:8181 -p 7681:7681 rebor94/robotic_grip_grab_shadow_robotics:latest
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

VIDEO OF OBJECT GRASPING 

## nn_connector node (in further detail) 

To enable smart grasping without the need to train robots on specific objects this project was aimed to provide the groundwork to combine the use of neural networks with grasp enabled robots. The nn_connector node was build to gather the needed information from a neural network and provide these to other node the execute grasps. In that context the neural network uses the data gathered by the camera_data nodes and provides pose estimations. 

The neural network itself is not yet specified and can be chosen freely. The only constraints would be to use neural networks that use color images and depth images as input and provide positional vectors as an output. 

## dataset_creator + camera_mover nodes (in further detail) 

Both nodes fulfill the requirement of developing nodes that enable the creation of datasets of different objects. To save images and move the robotic arm at the same time, the functionality was split into two nodes. One node moves the camera around the object and the other node saves color- and depth-images. The nodes were developed under the assumptions that objects are placed on the table (provided by the sandbox) on the right lower corner. That enables the robotic arm to move around the corner and therefore makes it possible to take pictures of objects. Images in a ca. 90 degree angle can be taken.
All images are saved in a separate directory in '/camera_data/imgs/dataset_images/'. 

VIDEO OF CAMERA_MOVER 

The assumption of the placement of objects on the table was made in order to be able to move the robotic arm at the same hieght as the object is. Would objects be placed on the floor, for example, the camera could not capture the whole object. Moreover, the robotic arm does not move around the entire table due to the length of the robotic arm. 

Problem encountered: 
The camera has to move according to the movement of the robotic arm in order to be able to take pictures of the object at every angle. Due to the scope of the project, this issue has not been resolved. 

## Run the unit tests 

The developed unit tests can be run separately as follows, when you are in the "/workspace/src/" direcotry: 

```
$ nosetests -v ros_smart_grasping_pkgs/<pkg_name>/test/<file_name>
```

More detail on how to run unit tests in ROS can be found here: https://personalrobotics.ri.cmu.edu/software/unit-testing

## Author

Rebekka Orth - 2312288O - 2312288O@student.gla.ac.uk

## Acknowledgments 

The code of the simulation and the robot comes from: 
https://github.com/shadow-robot/smart_grasping_sandbox

Shadow robotics website can be found here: 
https://www.shadowrobot.com 

