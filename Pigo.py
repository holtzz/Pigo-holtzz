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
        self.status["ismoving"] = False
        print "Hey, hold on a second!"
        for x in range(3):
            stop()


    def fwd(self):
        self.status["ismoving"] = False
        print "Ready to go!"
        for x in range(3):
           fwd()

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
