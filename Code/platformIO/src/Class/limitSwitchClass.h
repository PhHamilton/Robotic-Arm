#ifndef limitSwitchClass_h
#define limitSwitchClass_h

#include "Arduino.h"
// Add software debounce
class limitSwitch
{
    public:
        limitSwitch(uint8_t limitSwitchPin);
        void initialize(void);
        bool info(void);
        bool isPressed(void);

    
    private:
        uint8_t _limitSwitchPin; 
        
};

#endif