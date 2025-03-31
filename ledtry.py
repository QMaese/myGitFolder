import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

red_led=17
green_led=27
blue_led=22

GPIO.setmode(GPIO.BCM)

GPIO.setup(red_led,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(green_led,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(blue_led,GPIO.OUT,initial=GPIO.LOW)

time.sleep(1)

GPIO.output(red_led,GPIO.LOW)
GPIO.output(green_led,GPIO.LOW)
GPIO.output(blue_led,GPIO.LOW)

soil_moisture=input("Enter the status of soil: ")

if soil_moisture=="dry":
    print("Soil is dry!! It needs water. Turning on Red LED")
    GPIO.output(red_led,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(red_led,GPIO.LOW)

elif soil_moisture=="wet":
    print("Soil is wet!! It has enough water. Turning on Green LED")
    GPIO.output(green_led,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(green_led,GPIO.LOW)


elif soil_moisture=="watering":
    print("The system is watering the plant!! Turning on the Blue LED")
    GPIO.output(blue_led,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(blue_led,GPIO.LOW)

else:
    print("invalid vocabs")


GPIO.cleanup()