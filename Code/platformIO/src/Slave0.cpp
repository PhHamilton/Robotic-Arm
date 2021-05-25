#include <Arduino.h>
#include <Wire.h>

#define SLAVE_ADRESS 0x08
#define BAUD_RATE 9600

byte recievedValues[9] = {};

byte positionArray[6];
byte timeArray[6];

byte TASK = 0; 


void recieveEvent(int msgSize);
void setup()
{
    Serial.begin(BAUD_RATE);
    Wire.begin(SLAVE_ADRESS);
    Wire.onReceive(recieveEvent);

}

void loop()
{

}

void recieveEvent(int howMany)
{
    int counter = 0; 
    for(int i = 0; i < howMany; i++)
    {
        if(i == 1)
            TASK = Wire.read();
        else if(i > 2 && i <=7)

        else if(i > 8 && i <= 17)    
    }
    //     if( i%2 == 0)
    //     {
    //         recievedValues[counter] = Wire.read();
    //         counter++;
    //     }
    // }
    // for(int i = 0; i < counter; i++)
    // {
    //     Serial.print(recievedValues[i]);
    // }
    // Serial.println(" ");
}

