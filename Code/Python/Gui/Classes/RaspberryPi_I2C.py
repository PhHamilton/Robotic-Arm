from smbus import SMBus
import time

SLAVE_ADRESS = 0x08

class raspberryI2C():
    def __init__(self, ):
        self.bus = SMBus(1)

    def sendMessage(self, msg, slave_adress):
        msgInBytes = self.convertToBytes(msg)
        self.bus.write_i2c_block_data(slave_adress, 0x00, msgInBytes)

    def readMessage(self):
        pass

    def convertToBytes(self, msg):
        inBytes = []
        msgInBytes = bytes(msg, 'utf-8')
        for byte in msgInBytes: 
            inBytes.append(byte)
        
        print(inBytes)    

        return inBytes



a = raspberryI2C()
msg = "0,1,2,3,4,5,6,7,8"



while(1):
    
    a.sendMessage(msg, SLAVE_ADRESS)
    time.sleep(1)
    
  
