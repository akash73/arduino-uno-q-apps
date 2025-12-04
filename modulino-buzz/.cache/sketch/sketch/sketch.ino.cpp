#include <Arduino.h>
#line 1 "/home/arduino/ArduinoApps/modulino-buzz/sketch/sketch.ino"
#include <Modulino.h>

ModulinoBuzzer buzzer;

int frequency = 440;  // Frequency of the tone in Hz
int duration = 1000;  // Duration of the tone in milliseconds

#line 8 "/home/arduino/ArduinoApps/modulino-buzz/sketch/sketch.ino"
void setup();
#line 13 "/home/arduino/ArduinoApps/modulino-buzz/sketch/sketch.ino"
void loop();
#line 8 "/home/arduino/ArduinoApps/modulino-buzz/sketch/sketch.ino"
void setup(){
  Modulino.begin(Wire1);
  buzzer.begin();
}

void loop(){
  buzzer.tone(frequency, duration);  // Generate the tone
  delay(1000);  // Wait for 1 second
  buzzer.tone(0, duration);  // Stop the tone
  delay(1000);  // Wait for 1 second
}
