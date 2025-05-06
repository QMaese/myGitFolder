import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0)
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

RED_LED=17
GREEN_LED=27
RELAY_PIN=23

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_LED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(GREEN_LED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(RELAY_PIN, GPIO.OUT, initial = GPIO.LOW)
time.sleep(1)

GPIO.output(RED_LED,GPIO.LOW)
GPIO.output(GREEN_LED,GPIO.LOW)
#soil moisture sensor setup                      # Read from channel 0 of the ADC (where sensor is connected)

#Global Variables
timesWatered = 0          # Tracks number of times the plant has been watered
AUTO_MODE = True          # If True, system will water plant automatically when soil is dry

#watering function of the system
def water_plant():
    """Function to water the plant"""
    global timesWatered
    print("Watering plant...")
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(RELAY_PIN, GPIO.LOW)
    timesWatered += 1                    # Increment watering count
           # Update GUI label

#soil mositure monitor
def check():
    """Function to continuously check soil moisture and auto-water"""
    while True:
        moisture_value = chan.value     # Read analog value from sensor
        print(f"Soil Moisture Value: {moisture_value}")  # Print for debugging

        if moisture_value > 15000:      # Threshold: less than 15000 = dry soil
            print("Soil is dry. Turning on Red LED.")
            GPIO.output(RED_LED, GPIO.HIGH)    # Red LED ON
            GPIO.output(GREEN_LED, GPIO.LOW)   # Green LED OFF

            if AUTO_MODE:              # If auto mode is enabled
                water_plant()          # Water the plant

        else:
            print("Soil is wet. Turning on Green LED.")
            GPIO.output(GREEN_LED, GPIO.HIGH)   # Green LED ON
            GPIO.output(RED_LED, GPIO.LOW)      # Red LED OFF

        time.sleep(10)                # Wait 10 seconds before next reading


GPIO.cleanup()
