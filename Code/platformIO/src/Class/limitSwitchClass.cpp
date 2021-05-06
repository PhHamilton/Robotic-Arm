#include <Arduino.h>
#include "limitSwitchClass.h"


limitSwitch::limitSwitch(uint8_t limitSwitchPin)
{
    _limitSwitchPin = limitSwitchPin;
}

void limitSwitch::initialize(void)
{
    pinMode(_limitSwitchPin, INPUT);
}

bool limitSwitch::isPressed(void)
{
    return !digitalRead(_limitSwitchPin);
}

bool limitSwitch::info(void)
{
    return digitalRead(_limitSwitchPin);
}