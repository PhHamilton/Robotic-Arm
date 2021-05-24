// #include <Arduino.h>
// // #include "Class/MotorDriverClass.h"
// #include "Class/axisClass.h"
// #include <Wire.h>

// #define WAIT_FOR_INPUT 0
// #define HOME_MOTORS 1
// #define MOVE_MOTORS 2 
// #define SLAVE_ADRESS 0x08

// // Motor parameters [Controller 0]
// // Axis 0
// uint8_t motorPins_0[3] = {5,4,6};
// uint16_t stepsPerRev_0 = 2*200;
// uint16_t frequencyRange_0[2] = {350, 2000};
// uint16_t angleRange_0[2] = {0, 1080};
// uint8_t limitSwitchPin_0 = 16;

// axisClass axis0(motorPins_0, stepsPerRev_0, frequencyRange_0, angleRange_0, limitSwitchPin_0);

// // Axis 1 
// uint8_t motorPins_1[3] = {6,5,7};
// uint16_t stepsPerRev_1 = 2*200;
// uint16_t frequencyRange_1[2] = {350, 2000};
// uint16_t angleRange_1[2] = {0, 1080};
// uint8_t limitSwitchPin_1 = 17;

// axisClass axis1(motorPins_1, stepsPerRev_1, frequencyRange_1, angleRange_1, limitSwitchPin_1);

// // Axis 2 

// uint8_t motorPins_2[3] = {15,14,16};
// uint16_t stepsPerRev_2 = 2*200;
// uint16_t frequencyRange_2[2] = {350, 2000};
// uint16_t angleRange_2[2] = {0, 1080};
// uint8_t limitSwitchPin_2 = 15;

// axisClass axis2(motorPins_2, stepsPerRev_2, frequencyRange_2, angleRange_2, limitSwitchPin_2);

// // Axis 3 
// uint8_t motorPins_3[3] = {18,17,19};
// uint16_t stepsPerRev_3 = 2*200;
// uint16_t frequencyRange_3[2] = {350, 2000};
// uint16_t angleRange_3[2] = {0, 1080};
// uint8_t limitSwitchPin_3 = 14;

// axisClass axis3(motorPins_3, stepsPerRev_3, frequencyRange_3, angleRange_3, limitSwitchPin_3);


// float goToPos = 0; 
// bool runFlag = 0;
// char inputBuffer[16];

// bool taskCompleted = false; 
// uint8_t task = 0;
// float positionArray[4] = {360, 0, 0, 0}; 
// float timeArray[4] = {0, 0, 0, 0}; 





// int deg = 0; 

// void homeMotors(void);
// void moveMotors(float positions[4], float times[4]);

// void setup() 
// {
//   // put your setup code here, to run once:
//   Serial.begin(9600);
//   axis0.initialize();
//   axis1.initialize();
//   axis2.initialize();
//   axis3.initialize();
// }

// void loop() 
// {
//   if(Serial.available() > 0)
//   {
//     Serial.readBytes(inputBuffer, sizeof(inputBuffer));
//     goToPos = atoi(inputBuffer);
//     Serial.print("Target Position: ");
//     Serial.print("\t");
//     Serial.println(goToPos);
//     delay(1000);
//     runFlag = 1; 
//   }

//   if(runFlag == 1)
//   {
//     if(goToPos == -1)
//     {
//       axis0.home();
//       if(axis0.isHomed())
//         runFlag = 0;
//     }
//     else
//     {
//       axis0.rotate(goToPos);
//       if(axis0.ready())
//         runFlag = 0;
//     }
//   }

  

// } 

// void initializeSlave(void)
// {
//   Wire.begin(SLAVE_ADRESS);
  
// }

// void recieveEvent()
// {

// }

// void requestEvent()
// {

// }

// void parseMessage()
// {
  

// }

// void homeMotors(void)
// {
//   static int state = 0; 

//   switch(state)
//   {
//     case 0: 
//       axis0.home();
//       if(axis0.isHomed())
//       {
//         state++;
//         axis0.info();
//       }
//     break; 

//     case 1: 
//       axis0.rotate(axis0.limitSwitchOffset);
//       if(axis0.ready())
//       {
//         taskCompleted = true; 
//         state = 0; 
//         Serial.println("Motors Homed");
//       }
//     break;
//   //   case 1: 
//   //     axis1.home();
//   //     if(axis1.isHomed())
//   //     {
//   //       axis1.rotate(axis1.limitSwitchOffset);
//   //       if(axis1.ready())
//   //         state++;
//   //     }
//   //   break;

//   //   case 2: 
//   //     axis2.home();
//   //     if(axis2.isHomed())
//   //     {
//   //       axis2.rotate(axis2.limitSwitchOffset);
//   //       if(axis2.ready())
//   //         state++;
//   //     }
//   //   break;

//   // case 3: 
//   //     axis3.home();
//   //     if(axis3.isHomed())
//   //     {
//   //       axis3.rotate(axis3.limitSwitchOffset);
//   //       if(axis3.ready())
//   //       {
//   //         taskCompleted = true; 
//   //         state = 0;
//   //       }
//   //     } 
//   //   break;

//     default: 
//       state = 0;
//     break; 
//   }
// }

// void moveMotors(float positions[4], float times[4])
// {
//   axis0.rotate(positions[0]);
//   if(axis0.ready())
//     taskCompleted = true;
// //   axis1.rotate(positions[1], times[1])
// //   axis2.rotate(positions[2], times[2])
// //   axis3.rotate(positions[3], times[3])
  
// //   if(axis0.ready() && axis1.ready() && axis2.ready() && axis3.ready())
// //     taskCompleted = true; 
// // }
// }
