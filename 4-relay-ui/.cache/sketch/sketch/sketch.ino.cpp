#include <Arduino.h>
#line 1 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
#include "Arduino_RouterBridge.h"

int relay_1 = LED3_R;
int relay_2 = 7;
int relay_3 = 8;
int relay_4 = 12;

#line 8 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
void setup();
#line 22 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
void loop();
#line 26 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
void set_relay_1(bool state);
#line 31 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
void set_relay_2(bool state);
#line 36 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
void set_relay_3(bool state);
#line 41 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
void set_relay_4(bool state);
#line 8 "/home/arduino/ArduinoApps/4-relay-ui/sketch/sketch.ino"
void setup() {
  pinMode(relay_1, OUTPUT);
  pinMode(relay_2, OUTPUT);
  pinMode(relay_3, OUTPUT);
  pinMode(relay_4, OUTPUT);

  Bridge.begin();
  Bridge.provide("set_relay_1", set_relay_1);
  Bridge.provide("set_relay_2", set_relay_2);
  Bridge.provide("set_relay_3", set_relay_3);
  Bridge.provide("set_relay_4", set_relay_4);  

}

void loop() {
  
}

void set_relay_1 (bool state)
{
  digitalWrite(relay_1, state ? HIGH : LOW );
}

void set_relay_2 (bool state)
{
  digitalWrite(relay_2, state ? HIGH : LOW );
}

void set_relay_3 (bool state)
{
  digitalWrite(relay_3, state ? HIGH : LOW );
}

void set_relay_4 (bool state)
{
  digitalWrite(relay_4, state ? HIGH : LOW );
}


