#ifndef axisClass_h
#define axisClass_h

#include "Arduino.h"
#include "MotorDriverClass.h"
#include "limitSwitchClass.h"

struct motorData;
{
    uint8_t stepPin;
    uint8_t dirPin; 
    uint8_t enablePin;
    uint16_t stepsPerRev; 
    uint16_t minFrequency;
    uint16_t maxFrequency;
    uint16_t maxAngle;
    uint16_t minAngle;
};

class axisClass
{
    public:
        axisClass(const motorData &data, uint8_t limitSwitchPin);
        void initialize(void);

        void rotate(float deg, float time = NULL);
        void home(void); 
        void info(void);

    private:    

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