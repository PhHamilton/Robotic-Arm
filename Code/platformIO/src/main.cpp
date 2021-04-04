#include <Arduino.h>
#include "Class/MotorDriverClass.h"

MotorDriver motor1(9,8,10);
MotorDriver motor2(3,4,14);
MotorDriver motor3(5,6,15);
MotorDriver motor4(7,11,16);
int deg = 0; 
char inputBuffer[16];
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  motor1.initialize();
  motor2.initialize();
  motor3.initialize();
  motor4.initialize();
  
}

void loop() 
{

  motor1.rotateDegrees(5*360);
  motor2.rotateDegrees(5*360);
  motor3.rotateDegrees(5*360);
  motor4.rotateDegrees(5*360);
}