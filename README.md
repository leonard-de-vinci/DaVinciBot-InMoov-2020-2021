
# DaVinciBot InMoov 2020-2021
**ROS serial for ESP8266 through WiFi integrated on InMoov**
```
2021 Flavien Deseure & Wim Poignon (https://github.com/leonard-de-vinci/DaVinciBot-InMoov-2020-2021) 
```
This is an adaptation of ROS-serial-arduino to run on the ESP8266, a small and efficient chip, with WiFi instead of wired USB UART cable, based on http://answers.ros.org/users/1034/ahendrix/ proposed solution for Arduino with WiFi shield.

**ESP8266 NodeMCU board**
There are multiple reasons to use the ESP8266 (or ESP32) chip instead of a standard Arduino. It begins with the size and the memory.
The ESP8266 is a cost-effective and highly integrated Wi-Fi MCU for IoT applications, with a better flash memory compared to Arduino Uno (4MB vs. 32 KB). Moreover, you can load new firmware to the board using a Wi-Fi connection rather than serial communication.
**Platformio**
For this projet, we are using PlatformIO IDE on Visual Studio Code for coding the Wifi microchip. PlatformIO is a professional tool for embedded systems engineers, where we can have a lot of Freedom. 
**Connection between ESP and ROS**

This Esp8266 sketch creates a Car (similar to turtlebot) with all basic ROS objects, that connect via "WiFi" with rosserial in the server. 
This is an innovative way of connecting rosserial using tcp thanks to http://answers.ros.org/users/1034/ahendrix/ example program.

**Examples**

Folows, a list of progressive codes created during the research and development of Ros compatibility with ESP8266. They are convenient
to be used during learning, as Ros has an step learning curve.

**esproswifi**

Example program taken from http://answers.ros.org/users/1034/ahendrix/ for Arduino and
adapted to ESP8266, NodeMCU dev module. Please, modify ssid/password of your Wifi and 
IP of your roscore server. Your ESP8266 will try to connect to 11411 port at that server IP
To allow the connection, run roscore of course, and later:
```
            $ rosrun rosserial_python serial_node.py tcp
```

**chatter**

The standard ros tutorial client, working via Serial cable adapted for ESP8266
This example is particulary suitable for Witty ESP8266 dev platform and allow
to toggle all its leds by publishing to /led topic with stdmsg/Int16 that 
correspond to its gpio pin ESP12E number, (i.e. 2,12,13,15)

**CarEspRos**

NodeMCU with motor shield and 2 DC motors plus infrared encoders wheels (DoIt car) implementation in ROS WiFi
with esproswifi approach. Encoder counters are pusblished and basic movement with time length as subscriptions.
Car is moved with messages like: 
```
$ rostopic pub -1 /car/forward std_msgs/Int16 1000 // to move foward 1000 ms, use backward, right or left
```
Car encoders can be read with:
```
$ rostopic echo /car/leftencoder
```

**CarEspRosServo**

This is a version of CarEspRos above with addition of Servo in D7 nodeMCU pin (GPIO13 of ESP12). This Servo
ROS subscription can be used, to rotate a Steering Wheel, or other usages. See later. Message to publish is:
```
$ rostopic pub -1 /car/angle std_msgs/Int16 120  // to adjust to Servo center angle (min:0, max:255)
````

This code is part of a student project to build an open source ROS Robot. 

Have fun,

Flavien & Wim
