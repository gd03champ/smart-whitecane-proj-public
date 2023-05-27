import serial
import codecs
import time
import playsound
import os



def beep(gap):

        for i in range(3):
               #playsound.playsound('assets/buk.mp3', True)
                playsound.playsound('assets/buk.mp3', True)
                time.sleep(gap)


usbport = '/dev/ttyACM0' #usb from arduino
arduino = serial.Serial(usbport, 9600, timeout=0)
numbers=list("1234567890")
while (True):
    if (arduino.inWaiting()>0):
        myData = arduino.readlines()
        myDist = myData[len(myData)-1]
        list_byt = list(str(myDist))
        list_num = []
        for _ in list_byt:
                if _ in numbers:
                        list_num.append(_)
                else:
                        pass
       #print(list_num)
        s = [str(integer) for integer in list_num]
        a_string = "".join(s)
        print(a_string)
        res = int(a_string)
        print(res)
        time.sleep(0.5)



        if res < 10:
                beep(0.1)
        elif res < 30:
                beep(0.4)
        elif res < 50:
                beep(0.6)
        else:
                pass
       # print(type(res))
