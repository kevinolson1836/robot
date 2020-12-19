import time
from easygopigo3 import EasyGoPiGo3 # importing the EasyGoPiGo3 class


gpg = EasyGoPiGo3() # instantiating a EasyGoPiGo3 object
gpg3_obj = EasyGoPiGo3() #making a second gopigo object
gpg3_obj2 = EasyGoPiGo3() #making a second gopigo object


servo = gpg3_obj.init_servo() # defines servo
servo2 = gpg3_obj2.init_servo(port = "SERVO2") # defines servo


my_distance_sensor = gpg.init_distance_sensor() #defines distance sensor


#functions

def startup(servo, gpg):
	servo.reset_servo()
	servo.rotate_servo(90)
	gpg.stop()

startup(servo, gpg)
startup(servo2, gpg)


