def inter():

    try:

        i = 0

        while True:
            import os
            os.system("python3 setpin.py")

            import RPi.GPIO as GPIO
            import time
            import os

            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)
            buttonPin = 33

            GPIO.setup(buttonPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

            while True:

                state = GPIO.input(buttonPin)
                if state == False:
                    pass
                else:
                    print("Pushed")
                    os.system("python3 setpin.py")
                    i+=1
                    #print(i)
                    f=open('itf.txt','w+')
                    f.write(str(i))
                    f.close()
                    if i==4:
                        exit()
                    time.sleep(0.1)
                    break
    except KeyboardInterrupt:
        print("Button action terminated: Ctrl C pressed 🙂")
        exit()

if __name__ == "__main__":
    inter()
