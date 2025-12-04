#include "Arduino_RouterBridge.h"

void setup() {
  Monitor.begin();
}

void loop() {
  Monitor.println("Hello UNO Q!");
  delay(1000);
}