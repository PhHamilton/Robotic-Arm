from smbus import SMBus
import time

SLAVE_ADRESS = 0x08

class raspberryI2C():
    def __init__(self, ):
        self.bus = SMBus(1)

    def sendMessage(self, msg, slave_adress):
        for byte in msg: 
            self.bus.write_byte(slave_adress, byte)

    def readMessage(self):
        pass


a = raspberryI2C()

while(1):
    a.sendMessage("1,2,3,4", SLAVE_ADRESS)
    time.sleep(1)
    
