#include <Arduino.h>
#include "axisClass.h"

#define CLOCKWISE 1 
#define COUNTERCLOCKWISE 0 

axisClass::axisClass(const motorData data, uint8_t limitSwitchPin):_motorDriver(data->stepPin, data->dirPin, data->enablePin), _limitSwitch(limitSwitchPin)
{
    _motorDriver.stepsPerRev = data->stepsPerRev;
    _motorDriver.minFrequency = data->minFrequency;
    _motorDriver.maxFrequency = data->maxFrequency; 
    _motorDriver.maxAngle = data->maxAngle; 
    _motorDriver.minAngle = data->minAngle; 
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

void axisClass::info(void)
{
    Serial.print("Motor position");
    Serial.print("\t");
    Serial.println(_motorDriver.info()); 
    Serial.print("Limitswitch status");
    Serial.print("\t");
    Serial.println(_limitSwitch.info());
}