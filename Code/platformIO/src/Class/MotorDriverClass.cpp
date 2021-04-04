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
    _direction(CLOCKWISE);
    _enableMotor(false);
    Serial.println(round(1000000/minFrequency));
}

void MotorDriver::oneRevolution(void)
{
    smoothStep(stepsPerRev);
}

void MotorDriver::rotateDegrees(float deg)
{
    static float _currentDeg = 0;    
    
    if(deg != _currentDeg) // New entry!
    {   
        finished = 0; 
        float relativeMovement = deg - _currentDeg; 
        relativeMovement < 0 ? _direction(COUNTERCLOCKWISE) : _direction(CLOCKWISE);

        //smoothStep(_degToSteps(abs(relativeMovement)));
        regularStep(_degToSteps(abs(relativeMovement)));
    }

    if(finished)
    {
        _currentDeg = deg; 
    }

    
}

void MotorDriver::regularStep(uint16_t nSteps)
{
    if(_stepCounter != nSteps)
    {
        _enableMotor(true); 
        _step(1000);
    }
    else
    {
        finished = 1; 
        _enableMotor(false);
    }
}

void MotorDriver::rotateRadians(float rad)
{
    smoothStep(_radToSteps(rad));
}

void MotorDriver::smoothStep(uint16_t smoothStep)
{

    _fStepFactor = ((maxFrequency-minFrequency)/_stepsToAccelerate(smoothStep));

    if(_stepCounter != smoothStep)
    {
        _enableMotor(true);    
        if(_stepCounter < _stepsToAccelerate(smoothStep)) //Acceleration
        {
            _step(minFrequency + _fStepFactor*(_stepCounter+1));
        }
        
        else if(_stepCounter >= smoothStep - _stepsToAccelerate(smoothStep)) //Deacceleration
        {
            _step(maxFrequency - _fStepFactor*(_stepCounter - (smoothStep - _stepsToAccelerate(smoothStep))));
        }
        
        else // Constant speed phase
            _step(maxFrequency);

        //_dir > 0 ? _stepCounter++ : _stepCounter--;
    }
    else
    {
        _enableMotor(false);
        finished = 1; 
    }
    
}

bool MotorDriver::ready(void)
{
    if(finished == 1)
        return true; 
    else
        return false;
}

void MotorDriver::_step(uint16_t frequency)
{
    
    //t_off = (uint16_t)(1000000/frequency) - t_on;
    _currentMicros = micros(); 
    switch(_state)
    {
        case 0: 
            t_off = (uint16_t)(1000000/frequency) - t_on;
            
        case 1:     
            digitalWrite(_stepPin, HIGH);
            delayMicroseconds(t_on);
            digitalWrite(_stepPin, LOW);
            _state = 2;
        break;
        case 2: 
            if(_currentMicros - _previousMicros >= t_off)
            {
                _previousMicros = _currentMicros;
                _dir > 0 ? _stepCounter++ : _stepCounter--;
                _state = 0; 
            }
        break;
    }
    
}

float MotorDriver::_stepsToAccelerate(uint16_t nSteps)
{
    if(accelerationPercent > 50) accelerationPercent = 50; 
    if(accelerationPercent < 0) accelerationPercent = 0;

    return (nSteps*accelerationPercent/100);
}

uint16_t MotorDriver::_degToSteps(float deg)
{
    deg < 0 ? _direction(COUNTERCLOCKWISE) : _direction(CLOCKWISE);
    return (uint16_t)(stepsPerRev*((float)abs(deg)/360));
}

uint16_t MotorDriver::_radToSteps(float rad)
{
    rad < 0 ? _direction(COUNTERCLOCKWISE) : _direction(CLOCKWISE);
    return (uint16_t)(stepsPerRev*((float)abs(rad)/(2*PI)));
}

void MotorDriver::_enableMotor(bool state)
{
    state == true ? digitalWrite(_enablePin, LOW) : digitalWrite(_enablePin, HIGH);
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
