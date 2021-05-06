#include <Arduino.h>
#include "MotorDriverClass.h"

#define CLOCKWISE 1 
#define COUNTERCLOCKWISE 0 


MotorDriver::MotorDriver(uint8_t stepPin, uint8_t dirPin, uint8_t enablePin)
{
    _stepPin = stepPin; 
    _dirPin = dirPin;
    _enablePin = enablePin;
}

void MotorDriver::initialize(void)
{
    pinMode(_stepPin, OUTPUT);
    pinMode(_dirPin, OUTPUT);
    pinMode(_enablePin, OUTPUT);
    _direction(COUNTERCLOCKWISE);
    _enableMotor(false);
}

void MotorDriver::goTo(float deg, float time = NULL)
{
    deg = _withinLimis(deg);

    if(time == NULL)
    {  
        t_off = (uint16_t)(1000000/maxFrequency) - t_on;  
    }
    else
    {
        //Do something
    }

    float relativeMovement = deg - _currentPosition; 
    relativeMovement > 0 ? _direction(CLOCKWISE) : _direction(COUNTERCLOCKWISE);

    rotateDegrees(relativeMovement);

    if(finished)
    {
        _currentPosition += relativeMovement;
    }
    
}

void MotorDriver::rotateDegrees(float deg)
{
    static float _currentDeg = 0;  
    
    if(deg != _currentDeg) // New entry!
    {   
        finished = 0;         
        deg > 0 ? _direction(CLOCKWISE) : _direction(COUNTERCLOCKWISE);

        regularStep(_degToSteps(abs(deg)));
    }

    if(finished)
    {
        _currentDeg = deg; 
    }
}

void MotorDriver::regularStep(uint16_t nSteps)
{
    if(abs(_stepCounter) != nSteps)
    {
        _enableMotor(true); 
        _step();
    }
    else
    {
        finished = 1; 
        _stepCounter = 0;
        _enableMotor(false);
    }
}


// void MotorDriver::smoothStep(uint16_t smoothStep)
// {

//     _fStepFactor = ((maxFrequency-minFrequency)/_stepsToAccelerate(smoothStep));

//     if(_stepCounter != smoothStep)
//     {
//         _enableMotor(true);    
//         if(_stepCounter < _stepsToAccelerate(smoothStep)) //Acceleration
//         {
//             _step(minFrequency + _fStepFactor*(_stepCounter+1));
//         }
        
//         else if(_stepCounter >= smoothStep - _stepsToAccelerate(smoothStep)) //Deacceleration
//         {
//             _step(maxFrequency - _fStepFactor*(_stepCounter - (smoothStep - _stepsToAccelerate(smoothStep))));
//         }
        
//         else // Constant speed phase
//             _step(maxFrequency);

//         //_dir > 0 ? _stepCounter++ : _stepCounter--;
//     }
//     else
//     {
//         _enableMotor(false);
//         finished = 1; 
//     }
    
// }

bool MotorDriver::ready(void)
{
    if(finished == 1)
        return true; 
    else
        return false;
}

void MotorDriver::continousRotation(bool deg)
{
    deg > 0 ? _direction(CLOCKWISE) : _direction(COUNTERCLOCKWISE); 
    _step();  
}
float MotorDriver::info(void)
{
    return _currentPosition;
}

void MotorDriver::_step(void)
{
    _currentMicros = micros(); 

    switch(_state)
    {
        case 0:
            digitalWrite(_stepPin, HIGH);
            delayMicroseconds(t_on);
            digitalWrite(_stepPin, LOW);
            _state = 1;
        break;
        case 1: 
            if(_currentMicros - _previousMicros >= t_off)
            {
                _previousMicros = _currentMicros;
                _dir > 0 ? _stepCounter++ : _stepCounter--;
                _state = 0; 
            }
        break; 

        default:

        break; 

    }

}

// void MotorDriver::_step(uint16_t frequency)
// { 
    
//     //t_off = (uint16_t)(1000000/frequency) - t_on;
//     _currentMicros = micros(); 

//     switch(_state)
//     {
//         case 0: 
//             t_off = (uint16_t)(1000000/frequency) - t_on;
            
//         case 1:     
//             digitalWrite(_stepPin, HIGH);
//             delayMicroseconds(t_on);
//             digitalWrite(_stepPin, LOW);
//             _state = 2;
//         break;
//         case 2: 
//             if(_currentMicros - _previousMicros >= t_off)
//             {
//                 _previousMicros = _currentMicros;
//                 _dir > 0 ? _stepCounter++ : _stepCounter--;
//                 _state = 0; 
//             }
//         break;
//     }
    
// }

// float MotorDriver::_stepsToAccelerate(uint16_t nSteps)
// {
//     if(accelerationPercent > 50) accelerationPercent = 50; 
//     if(accelerationPercent < 0) accelerationPercent = 0;

//     return (nSteps*accelerationPercent/100);
// }

float MotorDriver::_withinLimis(float deg)
{
    if(deg > maxAngle)
        return maxAngle; 
    else if(deg < minAngle)
        return minAngle;
    else
        return deg;     
}

uint16_t MotorDriver::_degToSteps(float deg)
{
    return (uint16_t)(stepsPerRev*((float)abs(deg)/360));
}

void MotorDriver::_enableMotor(bool state)
{
    state == true ? digitalWrite(_enablePin, HIGH) : digitalWrite(_enablePin, LOW);
}

void MotorDriver::_direction(bool dir)
{
    if(dir == CLOCKWISE)
    {
        digitalWrite(_dirPin, HIGH); 
        _dir = 1; 
    }
    else
    {
        digitalWrite(_dirPin, LOW);  
        _dir = 0; 
    }
}
