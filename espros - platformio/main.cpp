/*
 * rosserial Publisher Example
 * Prints "hello world!"
 * This intend to connect to a Wifi Access Point
 * and a rosserial socket server.
 * You can launch the rosserial socket server with
 * roslaunch rosserial_server socket.launch
 * The default port is 11411
 *
 */
#include <Servo.h>
#include <ESP8266WiFi.h>
#include <ros.h>
#include <std_msgs/String.h> //allow to work with str msg with ros (eg. publish a string message)
#include <std_msgs/Int16.h> //allow to work with int msg with ros (eg. move a servo with an int message)
#include <string>

Servo servo;

const char* ssid = "PULV_DVIC";
const char* password = "5UKAPIp!dvic";
// Set the rosserial socket server IP address
IPAddress server(172,21,72,140);
// Set the rosserial socket server port
const uint16_t serverPort = 11411;

#define message "servo moved"
#define LED D0
#define DEBUG 0
int i;

////  All subscriber messages callbacks here
void angleCallback(const std_msgs::Int16& msg) {
  Serial.print("sucess");
  servo.attach(D1);
  servo.write(abs(msg.data));
}

ros::NodeHandle nh;
// Make a chatter publisher
std_msgs::String str_msg;
//ros::Publisher chatter("chatter", &str_msg);
ros::Subscriber<std_msgs::Int16> sub("led", &angleCallback);

// Be polite and say hello
char hello[13] = "hello world!";

void setup()
{
  if(DEBUG)
  {
  // Use ESP8266 serial to monitor the process
  Serial.begin(115200);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  }

  // Connect the ESP8266 the the wifi AP
  WiFi.begin(ssid, password);
  if(DEBUG){
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  }

  // Set the connection to rosserial socket server
  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();
  nh.subscribe(sub);
  // Start to be polite
  //nh.advertise(sub);
  if(DEBUG){
    // Another way to get IP
    Serial.print("IP = ");
    Serial.println(nh.getHardware()->getLocalIP());

    while (nh.connected()) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("ROS connected");
  }
}

void loop()
{
  nh.spinOnce();
  // Loop exproximativly at 1Hz
  delay(100);
}