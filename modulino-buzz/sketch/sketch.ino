#include <Modulino.h>

ModulinoBuzzer buzzer;

int frequency = 440;  // Frequency of the tone in Hz
int duration = 1000;  // Duration of the tone in milliseconds

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