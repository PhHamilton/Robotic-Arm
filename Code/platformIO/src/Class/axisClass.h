#ifndef axisClass_h
#define axisClass_h

#include "Arduino.h"
#include "MotorDriverClass.h"
#include "limitSwitchClass.h"



class axisClass
{
    public:
        axisClass(uint8_t motorPins[3], uint16_t stepsPerRev, uint16_t frequencyRange[2], uint16_t angleRange[2], uint8_t limitSwitchPin);
        void initialize(void);
        void rotate(float deg, float time = NULL);
        bool ready();
        void home(void);
        bool isHomed(void); 
        float positionInfo(void);
        bool limitSwitchInfo(void);

        float limitSwitchOffset = 180; 

    private:    

        bool _homed = 0;     
        limitSwitch _limitSwitch;
        MotorDriver _motorDriver;

};


// struct motorData
// {
//     uint8_t stepPin = 1;
//     uint8_t dirPin = 2; 
//     uint8_t enablePin = 3;
//     uint16_t stepsPerRev = 200; 
//     uint16_t minFrequency = 350;
//     uint16_t maxFrequency = 2000;
//     uint16_t maxAngle = 1080;
//     uint16_t minAngle = 0;
// };

#endif