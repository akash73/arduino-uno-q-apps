#include <Arduino.h>
#line 1 "/home/arduino/ArduinoApps/minimal-rpc-call/sketch/sketch.ino"
// SPDX-FileCopyrightText: Copyright (C) 2025 ARDUINO SA <http://www.arduino.cc>
//
// SPDX-License-Identifier: MPL-2.0
#include <Modulino.h>
#include <Arduino_RouterBridge.h>

ModulinoBuzzer buzzer;

//frequecy and duration
int frequency = 440;  // Frequency of the tone in Hz
int duration = 1000;  // Duration of the tone in milliseconds


#line 14 "/home/arduino/ArduinoApps/minimal-rpc-call/sketch/sketch.ino"
void setup();
#line 29 "/home/arduino/ArduinoApps/minimal-rpc-call/sketch/sketch.ino"
void loop();
#line 34 "/home/arduino/ArduinoApps/minimal-rpc-call/sketch/sketch.ino"
void detection(String key);
#line 14 "/home/arduino/ArduinoApps/minimal-rpc-call/sketch/sketch.ino"
void setup() {
  //Bridge.begin();
  Monitor.begin(9600);
  delay(1000);
  
  Monitor.print("Hello from MCU");
  
  // Initialize Modulino I2C communication
  Modulino.begin(Wire1);
  buzzer.begin();
  Bridge.provide("detection", detection);
  Monitor.print("__LINE__ from MCU");

  }

void loop() {

        delay(10);  // Wait    
    }

void detection (String key)
{
  
   
  if (key == "person") {
   Monitor.print(key);
   buzzer.tone(frequency, duration);  // Generate the tone
   //buzzer.tone(0, duration);  
  } 

  
}

