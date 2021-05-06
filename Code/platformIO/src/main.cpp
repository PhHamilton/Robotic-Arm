#include <Arduino.h>
// #include "Class/MotorDriverClass.h"
#include "Class/axisClass.h"

struct motorData
{
    uint8_t stepPin = 8;
    uint8_t dirPin = 9; 
    uint8_t enablePin = 10;
    uint16_t stepsPerRev = 200; 
    uint16_t minFrequency = 350;
    uint16_t maxFrequency = 2000;

    uint16_t maxAngle = 1080;
    uint16_t minAngle = 0;
};

axisClass axis0(&motorData, 14);

// MotorDriver motor1(8,9,10);
// MotorDriver motor2(11,12,13);



float goToPos = 0; 
bool runFlag = 0;
char inputBuffer[16];


int deg = 0; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // motor1.stepsPerRev = 200*2;
  // motor1.maxFrequency = 500;
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
  }

  if(runFlag == 1)
  {
    // motor1.rotateDegrees(goTo);
    // motor1.goTo(goToPos);
  

    // if(motor1.ready())
    // {
    //   runFlag = 0;
    //   motor1.info();
    // }
  }


  // if(motor1.ready())

  // motor2.rotateDegrees(5*360);
}