# Turtlebot Controller

### Prerequisite
* bHaptics Player has to be installed (Windows)
   * The app can be found in
   bHaptics webpage: [http://www.bhaptics.com](http://bhaptics.com/)

### Dependencies
* websocket-client
* roslibpy

### roslibpy
Python ROS Bridge library allows to use Python and IronPython to interact with ROS, the open-source robotic middleware. It uses WebSockets to connect to rosbridge 2.0 and provides publishing, subscribing, service calls, actionlib, TF, and other essential ROS functionality.

#### roslibpy Installation
`pip install roslibpy`

#### ros setup
The ubuntu system needs to setup ros to run rosbridge

First install the rosbridge suite with the following commands:

`sudo apt-get install -y ros-kinetic-rosbridge-server`
`sudo apt-get install -y ros-kinetic-tf2-web-republisher`

And before starting a connection, make sure you launch all services:
`roslaunch rosbridge_server rosbridge_websocket.launch`
`rosrun tf2_web_republisher tf2_web_republisher`


#### roslibpy documentation
https://roslibpy.readthedocs.io/en/latest/index.html