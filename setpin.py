import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin = 33

GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin, 0)

exit()
