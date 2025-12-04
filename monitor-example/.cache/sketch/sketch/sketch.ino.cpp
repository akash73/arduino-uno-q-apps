#include <Arduino.h>
#line 1 "/home/arduino/ArduinoApps/ciao/sketch/sketch.ino"
#include "Arduino_RouterBridge.h"

#line 3 "/home/arduino/ArduinoApps/ciao/sketch/sketch.ino"
void setup();
#line 7 "/home/arduino/ArduinoApps/ciao/sketch/sketch.ino"
void loop();
#line 3 "/home/arduino/ArduinoApps/ciao/sketch/sketch.ino"
void setup() {
  Monitor.begin();
}

void loop() {
  Monitor.println("Hello UNO Q!");
  delay(1000);
}
