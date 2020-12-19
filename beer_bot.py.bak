import numpy as np
import random
import matplotlib.pyplot as p
import time
from picamera import PiCamera
import cv2
from easygopigo3 import EasyGoPiGo3 # importing the EasyGoPiGo3 class


gpg = EasyGoPiGo3() # instantiating a EasyGoPiGo3 object
gpg3_obj = EasyGoPiGo3() #making a second gopigo object
gpg3_obj2 = EasyGoPiGo3() #making a second gopigo object


imagePath = "picture1.jpg"
cascPath = "haarcascade_frontalface_default.xml"


servo = gpg3_obj.init_servo() # defines servo
servo2 = gpg3_obj2.init_servo(port = "SERVO2")

my_distance_sensor = gpg.init_distance_sensor() #defines distance sensor


#functions

def grab_can(servo2):
	servo2.rotate_servo(170)
	time.sleep(1)
	servo2.rotate_servo(0)
	time.sleep(1)


def startup(servo, gpg):
	servo.reset_servo()
	servo.rotate_servo(90)
	gpg.forward()

def l_turn(servo, gpg):
        print("biger than 550. turning left.")
        gpg.turn_degrees(90)
        gpg.forward()
        servo.disable_servo()

def r_turn(servo, gpg):
	print("biger than 550. turning right")
	gpg.turn_degrees(-90)
	gpg.forward()
	servo.disable_servo()

def check_right(servo, gpg):
        servo.rotate_servo(140)
        time.sleep(1)
        r_distance = my_distance_sensor.read_mm()
        servo.rotate_servo(90)
        return r_distance


def check_left (servo, gpg):
        servo.rotate_servo(25)
        time.sleep(1)
        l_distance = my_distance_sensor.read_mm()
        servo.rotate_servo(90)
        return l_distance



grab_can(servo2)
startup(servo, gpg)
#grab_can(servo2)
time.sleep(1)


# main loop of program
while True:
	gpg.forward()
	distance = my_distance_sensor.read_mm()
	print("Distance Sensor Reading (mm): " + str(my_distance_sensor.read_mm()))

	if (distance <= 450): # 450 mm away from object
		gpg.stop()
		print("less than 450, trying to check left side....")

		l_distance = check_left(servo, gpg)

		if (l_distance > 550):
			l_turn(servo, gpg)
			continue

		print("left bad. checking right")

		r_distance = check_right(servo, gpg)

		if (r_distance > 550):
			r_turn(servo, gpg)
			continue
		else:
			gpg.stop()
			gpg.backward()
			time.sleep(3)
			gpg.stop()
			l_distance = check_left(servo, gpg)
			r_distance = check_right(servo, gpg)
			if l_distance >450:
				l_turn(servo, gpg)
			elif r_distance > 450:
				r_turn(servo, gpg)
			else:
				print("cant move, stopping")
				gpg.stop()
				break


	#DONE WITH MOVEMENT, CHECK FOR FACES AND TAKE PICTURE.

