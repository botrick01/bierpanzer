import RPi.GPIO as GPIO
import time
import moveRobot
from gpiozero import Button

PIN_TRIGGER = 5
PIN_ECHO = 6
DESK_LENGTH = 100

def shoot():
    print("shoot")
    startButtonClick()

def move():
    print("move")
    moveRobot.moveRobot()

def checkIfShoot(distance):
    if(distance < DESK_LENGTH):
        shoot()
    else:
        move()

def pinSetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    global button
    button = Button(21)

def checkDistance():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)

    print("Distanz: %.1f" % distance, "cm")
    checkIfShoot(distance)

def startButtonClick():
    print("Push button to start")
    button.wait_for_press()
    startDistanceSensor()

def startDistanceSensor():
    try:
        while True:
            checkDistance()
    finally:
        GPIO.cleanup()

def main():
    pinSetup()
    moveRobot.setupMovement()
    startButtonClick()

if __name__ == "__main__":
    main()
