#include <Arduino.h>
// #include "Class/MotorDriverClass.h"
#include "Class/axisClass.h"

uint8_t motorPins[3] = {8,9,10};
uint16_t stepsPerRev = 2*200;
uint16_t frequencyRange[2] = {350, 2000};
uint16_t angleRange[2] = {0, 1080};
uint8_t limitSwitchPin = 2;

axisClass axis0(motorPins, stepsPerRev, frequencyRange, angleRange, limitSwitchPin);

// MotorDriver motor1(8,9,10);
// MotorDriver motor2(11,12,13);



float goToPos = 0; 
bool runFlag = 0;
char inputBuffer[16];

unsigned long currentTime;
unsigned long finishedTime;


int deg = 0; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  axis0.initialize();
  // motor1.stepsPerRev = 200*2;
  // motor1.maxFrequency = 2000;
  // motor1.initialize();

  // motor2.stepsPerRev = 200*2;
  // motor2.initialize();
}

void loop() 
{
  if(Serial.available() > 0)
  {
    Serial.readBytes(inputBuffer, sizeof(inputBuffer));
    goToPos = atoi(inputBuffer);
    Serial.print("Target Position: ");
    Serial.print("\t");
    Serial.println(goToPos);
    delay(1000);
    runFlag = 1; 
    currentTime = millis();
  }

  if(runFlag == 1)
  {
    axis0.rotate(goToPos);
    
    if(axis0.ready())
    {
      runFlag = 0;
      axis0.info();
    }

    // motor1.rotateDegrees(goTo);


    // motor1.goTo(goToPos,3);
    
  

    // if(motor1.ready())
    // {
    //   finishedTime = millis();
    //   runFlag = 0;
    //   motor1.info();
    //   Serial.println(finishedTime - currentTime);
    // }
  }


  // if(motor1.ready())

  // motor2.rotateDegrees(5*360);
}