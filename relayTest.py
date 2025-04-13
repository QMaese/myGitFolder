import RPi.GPIO as GPIO
import time

# Define GPIO pin for relay
RELAY_PIN = 17  # Use the GPIO pin number connected to relay IN

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(RELAY_PIN, GPIO.OUT)  # Set the relay pin as an output

try:
    while True:
        print("Relay ON")
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Activate relay (NO connects to COM)
        time.sleep(2)  # Wait 2 seconds

        print("Relay OFF")
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Deactivate relay (NO disconnects from COM)
        time.sleep(2)  # Wait 2 seconds

except KeyboardInterrupt:
    print("Exiting test.")
    GPIO.cleanup()  # Reset GPIO settings before exiting
