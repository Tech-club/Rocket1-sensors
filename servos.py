# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# Set up pin 11 for PWM
GPIO.setup(11,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(11, 50)     # Sets up pin 11 as a PWM pin
p.start(0)               # Starts running PWM on the pin and sets it to 0

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(11, True)
	p.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(11, False)
	p.ChangeDutyCycle(0)

SetAngle(90)
# Clean up everything
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup() 