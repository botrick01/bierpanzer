import wiringpi
import time

wiringpi.wiringPiSetup()
wiringpi.pinMode(7,1)
wiringpi.digitalWrite(7, 1)
time.sleep(1)
wiringpi.digitalWrite(7, 0)
