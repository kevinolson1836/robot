from flask import Flask, redirect, url_for, render_template, request

import RPi.GPIO as GPIO
import numpy as np
import random
import matplotlib.pyplot as p
import time
#from picamera import PiCamera
import cv2
from easygopigo3 import EasyGoPiGo3 # importing the EasyGoPiGo3 class


gpg = EasyGoPiGo3() # instantiating a EasyGoPiGo3 object
gpg3_obj = EasyGoPiGo3() #making a second gopigo object
gpg3_obj2 = EasyGoPiGo3() #making a second gopigo object

servo = gpg3_obj.init_servo() # defines servo
servo2 = gpg3_obj2.init_servo(port = "SERVO2")

global DEGREE
DEGREE = 0

laser = 2

#functions
def grab_can(servo2):
	servo2.rotate_servo(170)
	time.sleep(1)
	servo2.rotate_servo(0)
	time.sleep(1)


def startup(servo, gpg):
	servo.reset_servo()
	servo.rotate_servo(90)

def l_turn(servo, gpg):
        DEGREE = DEGREE -90
        gpg.turn_degrees(DEGREE)
        servo.disable_servo()

def r_turn(servo, gpg):
	gpg.turn_degrees(90)
	servo.disable_servo()


app = Flask(__name__)

@app.route('/')
def test():
	req = str(request)
	req = req[33:36]

	if req == "For":
		print("Forward")
		gpg.forward()
	elif req == "Sto":
		print("Stop")
		gpg.stop()
	elif req == "Lef":
		print("Left")
		gpg.left()
	elif req == "Rig":
		print("Right")
		gpg.right()
	elif req == "Rev":
		print("Reverse")
		gpg.backward()
	elif req == "Ope":
		print("Open")
		servo2.rotate_servo(170)
	elif req == "Clo":
		print("Close")
		servo2.rotate_servo(10)
#	elif req == "On":
#                print("laser on")
#                GPIO.output(laser, GPIO.HIGH)
#	elif req == "Off":
##                print("Laser off")
#                GPIO.output(laser, GPIO.LOW)


	return render_template('index.html')

startup(servo, gpg)
app.run(debug=True, host='0.0.0.0', port=4242)

# main loop of program
