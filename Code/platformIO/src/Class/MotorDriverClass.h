#ifndef MotorDriverClass_h
#define MotorDriverClass_h

#include "Arduino.h"

class MotorDriver
{ 
    public:
        MotorDriver(uint8_t stepPin, uint8_t dirPin, uint8_t enablePin);
        void initialize(void);
        void goTo(float deg, float time = NULL);
        void rotateDegrees(float deg); 
        void regularStep(uint16_t nSteps);
        void continousRotation(bool dir);
        float info(void);
        bool ready(void);
        uint16_t t_on = 1; //us
        
        uint16_t stepsPerRev = 200; 
        uint16_t minFrequency = 350;
        uint16_t maxFrequency = 2000;
        
        uint8_t accelerationPercent = 30; 

        uint16_t maxAngle = 1080;
        uint16_t minAngle = 0;
    private:
    
    unsigned long _previousMicros = 0; 
    unsigned long _currentMicros;
    
    float _withinLimis(float deg); 

    uint8_t _stepPin;
    uint8_t _dirPin;
    uint8_t _enablePin;

    uint16_t t_off = (uint16_t)(1000000/maxFrequency) - t_on;  
    uint8_t _state = 0;
    bool _dir = 1;
    bool finished = 0; 

    void _step(void);
    float _stepsToAccelerate(uint16_t nSteps);
    uint16_t _degToSteps(float deg);
    int _stepCounter = 0; 
    uint16_t _aSteps = 0;

    float _fStepFactor = 0; 


    float _currentPosition = 0;

    void _enableMotor(bool state); 
     
    void _direction(bool dir);


};

#endif