import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins
TRIG = 23
ECHO = 24

# Set GPIO direction
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Set TRIG to LOW
    GPIO.output(TRIG, False)
    time.sleep(0.2)

    # Send 10µs pulse to TRIG
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Start time
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Stop time
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Time difference
    time_elapsed = stop_time - start_time

    # Distance calculation (cm)
    distance = (time_elapsed * 34300) / 2
    return round(distance, 2)

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
