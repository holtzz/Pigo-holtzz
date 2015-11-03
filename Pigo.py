from gopigo import *
import time

__author__ = 'holtzz'

class Pigo:

    ######
    ###### BASIC STATUS AND METHODS
    ######

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175, 'rightspeed': 175}

    def __init__(self):
        print "Hello!"

    def stop(self):
        self.isMoving = False
        while stop() != 1
            time.sleep(.1)
            print "Oops! I'm sorry! I just can't stop!"

    def fwd(self):
        self.isMoving = True
        while fwd() != 1
            time.sleep(.1)
            print "I tried to vroom...but I couldn't."

    ######
    ###### COMPLEX METHODS
    ######

    ######
    ###### MAIN APP STARTS HERE
    ######

piggy = Pigo()
tina.fwd()
time.sleep(2)
tina.stop()
