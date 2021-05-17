#include <Arduino.h>
#include "axisClass.h"

#define CLOCKWISE 1 
#define COUNTERCLOCKWISE 0 

axisClass::axisClass(uint8_t motorPins[3], uint16_t stepsPerRev, uint16_t frequencyRange[2], uint16_t angleRange[2], uint8_t limitSwitchPin)
:_motorDriver(motorPins[0], motorPins[1], motorPins[2]), _limitSwitch(limitSwitchPin)
{
    _motorDriver.stepsPerRev = stepsPerRev; 
    _motorDriver.minFrequency = frequencyRange[0];
    _motorDriver.maxFrequency = frequencyRange[1];
    _motorDriver.minAngle = angleRange[0];
    _motorDriver.maxAngle = angleRange[1];

}

void axisClass::initialize(void)
{
    _motorDriver.initialize();
    _limitSwitch.initialize();
}

void axisClass::rotate(float deg, float time = NULL)
{
    _motorDriver.goTo(deg, time);
}

void axisClass::home(void)
{
    if(!_limitSwitch.isPressed())
        _motorDriver.continousRotation(COUNTERCLOCKWISE);
    
}

bool axisClass::ready(void)
{
    return _motorDriver.ready();
}

void axisClass::info(void)
{
    Serial.print("Motor position");
    Serial.print("\t");
    Serial.println(_motorDriver.info()); 
    Serial.print("Limitswitch status");
    Serial.print("\t");
    Serial.println(_limitSwitch.info());
}