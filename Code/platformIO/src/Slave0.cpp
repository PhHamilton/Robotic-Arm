#include <Arduino.h>
#include "Class/axisClass.h"
#include <Wire.h>

#define SLAVE_ADRESS 0x08
#define BAUD_RATE 9600

#define WAIT_FOR_INPUT 0
#define HOME_MOTORS 1
#define MOVE_MOTORS 2 


// Motor parameters [Controller 0]
// Axis 0
uint8_t motorPins_0[3] = {5,4,6};
uint16_t stepsPerRev_0 = 2*200;
uint16_t frequencyRange_0[2] = {350, 2000};
uint16_t angleRange_0[2] = {0, 1080};
uint8_t limitSwitchPin_0 = 16;

axisClass axis0(motorPins_0, stepsPerRev_0, frequencyRange_0, angleRange_0, limitSwitchPin_0);


int testArray[9] = {};

int positonArray[4] = {0, 0, 0, 0};
int timeArray[4] = {-1, -1, -1, -1};

int TASK = 0; 

bool taskCompleted = true;

void recieveEvent(int howMany);
void requestEvent();
void parseData(String array);
void updateArray(int arr[]);
void printArray();


void homeMotors();
void moveMotors(int positions[4], int times[4]);

void setup()
{
    Serial.begin(BAUD_RATE);
    Wire.begin(SLAVE_ADRESS);
    Wire.onReceive(recieveEvent);
    Wire.onRequest(requestEvent);

}

void loop()
{

    switch(TASK)
    {
        case WAIT_FOR_INPUT:

        break;

        case HOME_MOTORS:
            homeMotors();

        break;

        case MOVE_MOTORS:
            moveMotors(positonArray, timeArray);
        break;

        default: 
            TASK = 0; 
        break;
    }

    if(taskCompleted)
        TASK = 0; 

}

void requestEvent()
{
    // Get values
    for(int i = 0; i < 3; i++)
    {
        Wire.write(i + '0');
    }
}

void recieveEvent(int howMany)
{
    char c;
    String dataString = "";

    for(int i = 0; i < howMany; i++)
    {
        c = Wire.read();
        dataString = dataString + c; 
    }

    parseData(dataString);
    printArray();
    dataString = "";
}

void updateArray(int arr[])
{
    TASK = arr[0]; 
    for(int i = 0; i < 4; i++)
    {
        positonArray[i] = arr[1+i];
        timeArray[i] = arr[5+i];
    }
}

void parseData(String array)
{
    
    int negativeNumber = 1; 
    uint8_t counter = 0; 

    // Starts at 1 to ignore the first 0
    // Convert to array of ints
    for(int i = 1; array[i] != '\0'; i++)
    {
        
        if(array[i] == '-')
        {
            negativeNumber = -1; 
            continue;
        }
        else if(array[i] == ',')
        {
            continue;
        }
        testArray[counter] = negativeNumber*(array[i] - '0');
        negativeNumber = 1; 

        counter++; 
    }

    updateArray(testArray);
}

void printArray()
{
    Serial.print("Task:");
    Serial.print("\t");
    Serial.println(TASK);

    Serial.print("Position:");
    Serial.print("\t");
    Serial.print(positonArray[0]);
    Serial.print(",");
    Serial.print(positonArray[1]);
    Serial.print(",");
    Serial.print(positonArray[2]);
    Serial.print(",");
    Serial.println(positonArray[3]);
    
    Serial.print("Time:");
    Serial.print("\t");
    Serial.print(timeArray[0]);
    Serial.print(",");
    Serial.print(timeArray[1]);
    Serial.print(",");
    Serial.print(timeArray[2]);
    Serial.print(",");
    Serial.println(timeArray[3]);

}

void homeMotors(void)
{
  static int state = 0; 

  switch(state)
  {
    case 0: 
      axis0.home();
      if(axis0.isHomed())
      {
        state++;
      }
    break; 

    case 1: 
      axis0.rotate(axis0.limitSwitchOffset);
      if(axis0.ready())
      {
        taskCompleted = true; 
        state = 0; 
        Serial.println("Motors Homed");
      }
    break;
  //   case 1: 
  //     axis1.home();
  //     if(axis1.isHomed())
  //     {
  //       axis1.rotate(axis1.limitSwitchOffset);
  //       if(axis1.ready())
  //         state++;
  //     }
  //   break;

  //   case 2: 
  //     axis2.home();
  //     if(axis2.isHomed())
  //     {
  //       axis2.rotate(axis2.limitSwitchOffset);
  //       if(axis2.ready())
  //         state++;
  //     }
  //   break;

  // case 3: 
  //     axis3.home();
  //     if(axis3.isHomed())
  //     {
  //       axis3.rotate(axis3.limitSwitchOffset);
  //       if(axis3.ready())
  //       {
  //         taskCompleted = true; 
  //         state = 0;
  //       }
  //     } 
  //   break;

    default: 
      state = 0;
    break; 
  }
}

void moveMotors(int positions[4], int times[4])
{
  axis0.rotate((float)positions[0]);
  if(axis0.ready())
    taskCompleted = true;
//   axis1.rotate(positions[1], times[1])
//   axis2.rotate(positions[2], times[2])
//   axis3.rotate(positions[3], times[3])
  
//   if(axis0.ready() && axis1.ready() && axis2.ready() && axis3.ready())
//     taskCompleted = true; 
// }
}