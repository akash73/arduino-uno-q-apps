#include <Arduino.h>
#line 1 "/home/arduino/ArduinoApps/detect-objects-to-sketch/sketch/sketch.ino"
// SPDX-FileCopyrightText: Copyright (C) 2025 ARDUINO SA <http://www.arduino.cc>
//
// SPDX-License-Identifier: MPL-2.0

#include "Arduino_RouterBridge.h"


constexpr auto keepAliveInterval { 1000ul };
auto keepAliveNow { keepAliveInterval };

#line 11 "/home/arduino/ArduinoApps/detect-objects-to-sketch/sketch/sketch.ino"
void setup();
#line 24 "/home/arduino/ArduinoApps/detect-objects-to-sketch/sketch/sketch.ino"
void loop();
#line 35 "/home/arduino/ArduinoApps/detect-objects-to-sketch/sketch/sketch.ino"
void detection(String key);
#line 11 "/home/arduino/ArduinoApps/detect-objects-to-sketch/sketch/sketch.ino"
void setup() {
    pinMode(LED3_G, OUTPUT);
    pinMode(LED4_B, OUTPUT);
    pinMode(LED4_R, OUTPUT);
    digitalWrite(LED3_G, HIGH);
    digitalWrite(LED4_B, HIGH);
    digitalWrite(LED4_R, HIGH);
    // Monitor.begin(9600);
    // Monitor.print("Hello: U5!");
    Bridge.begin();
    Bridge.provide("detection", detection);
}

void loop() {
  if (millis() > keepAliveNow) {
    // Monitor.print(millis());
    digitalWrite(LED3_G, LOW);
    delay(50);
    digitalWrite(LED3_G, HIGH);
    delay(50);
    keepAliveNow = millis() + keepAliveInterval;
  }
}

void detection(String key) {
    // LOW state means LED is ON
    Monitor.print(key);
    if (key == "keyboard") {
      digitalWrite(LED4_R, LOW);
      delay(50);
      digitalWrite(LED4_R, HIGH);
      delay(50);
    } else {
      digitalWrite(LED4_B, LOW);
      delay(50);
      digitalWrite(LED4_B, HIGH);
      delay(50);
    }

}

