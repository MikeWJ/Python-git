# First GPIO example
#   * Read button input
#   * Drive LEDs (Blink & PWM)

import RPi.GPIO as GPIO
import time

# Pin Definitions
pwmPin = 18
ledPin = 23
butPin = 17

duty = 75

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setup(butPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(pwmPin, 200) # Set PWM freq = 200Hz
GPIO.output(ledPin, GPIO.LOW)
pwm.start(duty)

# Infinite Loop
try:
    while 1:
        if  GPIO.input(butPin):             # Not Pressed ========
            pwm.ChangeDutyCycle(duty)
            GPIO.output(ledPin, GPIO.LOW)

        else:                               # Pressed ============
            GPIO.output(ledPin, GPIO.HIGH)
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.5)
            GPIO.output(ledPin, GPIO.LOW)
            pwm.ChangeDutyCycle(100-duty)
            time.sleep(0.5)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()