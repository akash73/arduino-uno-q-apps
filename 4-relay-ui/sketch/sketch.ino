#include "Arduino_RouterBridge.h"

int relay_1 = 4;
int relay_2 = 7;
int relay_3 = 8;
int relay_4 = 12;

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

