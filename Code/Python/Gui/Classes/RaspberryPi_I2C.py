from smbus import SMBus
import time

SLAVE_ADRESS = 0x08
SLAVE_ADRESS2 = 0x09
HOME_MOTORS = 1
MOVE_MOTORS = 2 


class raspberryI2C():
    def __init__(self):
        self.bus = SMBus(1)
        self.pos = "0,0,0,0"
        self.time = "0,0,0,0"

    def sendMessage(self, msg, slave_adress):
        msgInBytes = self.convertToBytes(msg)
        self.bus.write_i2c_block_data(slave_adress, 0x30, msgInBytes)
        
    def updatePosition(self, x0, x1, x2, x3):
        self.pos = "{},{},{},{}".format(x0,x1,x2,x3)

    def updateTime(self, t0, t1, t2, t3):
        self.time = "{},{},{},{}".format(t0,t1,t2,t3)

    def homeMotors(self):
        TASK = HOME_MOTORS
        msg = "{},{},{}".format(TASK, self.pos, self.time)
        self.sendMessage(msg, SLAVE_ADRESS)
        self.sendMessage(msg, SLAVE_ADRESS2)

    def moveMotors(self):
        TASK = MOVE_MOTORS
        msg = "{},{},{}".format(TASK, self.pos, self.time)
        self.sendMessage(msg, SLAVE_ADRESS)
        self.sendMessage(msg, SLAVE_ADRESS2)

    def readMessage(self):
        pass

    def convertToBytes(self, msg):
        inBytes = []
        msgInBytes = bytes(msg, 'utf-8')
        for byte in msgInBytes: 
            inBytes.append(byte)
        
        print(inBytes)

        return inBytes



msg = "0,-5,-3,-2,4,-1,-1,-1,-1"
a = raspberryI2C()

b = "1,1,1,1"
c = "2,2,2,2"

d = "{},{}".format(b,c)

print(d)

while(1):
    x0 = input()
    a.updatePosition(x0,0,0,0)
    a.moveMotors()
    # a.sendMessage(msg, SLAVE_ADRESS)
    time.sleep(1)
    
  
# from smbus import SMBus
# import time

# SLAVE_ADRESS = 0x08

# class raspberryI2C():
#     def __init__(self, ):
#         self.bus = SMBus(1)

#     def sendMessage(self, msg, slave_adress):
#         self.bus.write_i2c_block_data(SLAVE_ADRESS, 0, msg)
#         # for byte in msg: 
#         #     self.bus.write_byte(slave_adress, byte)

#     def readMessage(self):
#         pass


# a = raspberryI2C()

# # msg = [(startBit), (Position), (sign), ()]

# array = [-1, 1, -1, 1]

# while(1):
#     a.sendMessage(array, SLAVE_ADRESS)
#     print(array)
#     time.sleep(5)
    
