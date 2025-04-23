
#imporing necessary libraries
import RPi.GPIO as GPIO  #controls the GPIO pins on Rpi
import time    #for delays...like turning on pump for 5 seconds (example)
import threading   #allows runnning multiple tasks at once....GUI+sensor check for example
import tkinter as tk  #builds the GUI 
import board  #sets up I2C communication
import busio ####
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn  #reading analog data from sensor


#Setting up GPIO
GPIO.setwarnings(False)   #disable GPIO warnings
GPIO.setmode(GPIO.BCM)    #use BCM pin numbering

#defining GPIO pin numbers
RED_LED = 17                        # Red LED pin (dry soil)
GREEN_LED = 27                      # Green LED pin (wet soil)
BLUE_LED = 22                       # Blue LED pin (watering)
RELAY_PIN = 23                      # Relay module pin (controls water pump)
BUTTON_PIN = 24                     # Physical manual water button pin

#setting up GPIO pins as input/ output
GPIO.setup(RED_LED, GPIO.OUT, initial=GPIO.LOW)     # Red LED output, initially off
GPIO.setup(GREEN_LED, GPIO.OUT, initial=GPIO.LOW)   # Green LED output, initially off
GPIO.setup(BLUE_LED, GPIO.OUT, initial=GPIO.LOW)    # Blue LED output, initially off
GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.LOW)   # Relay output, initially off
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button input, pulled up

#soil moisture sensor setup
i2c = busio.I2C(board.SCL, board.SDA)               # Set up I2C communication
ads = ADS.ADS1115(i2c)                              # Initialize the ADS1115 ADC
chan = AnalogIn(ads, ADS.P0)                        # Read from channel 0 of the ADC (where sensor is connected)

#Global Variables
timesWatered = 0          # Tracks number of times the plant has been watered
AUTO_MODE = True          # If True, system will water plant automatically when soil is dry

#watering function of the system
def water_plant():
    """Function to water the plant"""
    global timesWatered
    print("Watering plant...")
    GPIO.output(RELAY_PIN, GPIO.HIGH)    # Turn ON the water pump
    GPIO.output(BLUE_LED, GPIO.HIGH)     # Turn ON the blue LED (watering)
    time.sleep(5)                        # Water for 5 seconds
    GPIO.output(RELAY_PIN, GPIO.LOW)     # Turn OFF the water pump
    GPIO.output(BLUE_LED, GPIO.LOW)      # Turn OFF the blue LED
    timesWatered += 1                    # Increment watering count
    update_times_label()                 # Update GUI label

#updating the GUI watering count
def update_times_label():
    """Update the GUI with the number of times watered"""
    if 'timesLabel' in globals():       # Check if label exists (only inside GUI)
        timesLabel.config(text=f"Times Watered: {timesWatered}")  # Update text

#soil mositure monitor
def check_soil_moisture():
    """Function to continuously check soil moisture and auto-water"""
    while True:
        moisture_value = chan.value     # Read analog value from sensor
        print(f"Soil Moisture Value: {moisture_value}")  # Print for debugging

        if moisture_value < 15000:      # Threshold: less than 15000 = dry soil
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

#Physical Button Action (optional)

def button_callback(channel):
    """Callback function when physical button is pressed"""
    print("Manual physical button pressed!")
    threading.Thread(target=water_plant).start()   # Run watering in separate thread

#GUI
def start_gui():
    """Function to start the GUI"""
    global timesLabel  # Make label accessible globally

    root = tk.Tk()                          # Create GUI window
    root.title("Smart Plantation System")   # Title of the window
    root.geometry("300x200")                # Set window size
    root.configure(bg="light green")        # Set background color

    titleLabel = tk.Label(root, text="Plant Watering System", font=("Arial", 16), bg="light green")
    titleLabel.pack(pady=20)                # Title label

    waterButton = tk.Button(root, text="Water Plant", 
                            command=lambda: threading.Thread(target=water_plant).start(),
                            font=("Arial", 14), bg="#ffffff", fg="#444444", padx=20, pady=10)
    waterButton.pack(pady=20)               # Manual watering button

    timesLabel = tk.Label(root, text=f"Times Watered: {timesWatered}", font=("Arial"), bg="light green")
    timesLabel.pack(pady=5)                 # Label to show number of times watered

    root.mainloop()

#program start point
try:
    # Set up event detection for physical button (falling edge = press)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=300)

    # Start background thread to monitor soil moisture
    threading.Thread(target=check_soil_moisture, daemon=True).start()

    # Start the GUI (blocking call)
    start_gui()

except KeyboardInterrupt:
    # Graceful exit if program is manually stopped
    print("Exiting program...")

finally:
    # Clean up GPIO to reset all pins safely
    GPIO.cleanup()



