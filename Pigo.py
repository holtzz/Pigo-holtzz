from gopigo import *
import time

__author__ = 'holtzz'

STOP_DIST = 50

class Pigo:

    ######
    ###### BASIC STATUS AND METHODS
    ######

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175, 'rightspeed': 175, 'dist': 100}

    def __init__(self):
        print "Hello!"
        self.status['dist'] = us_dist(15)

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

    #Check if the conditions are safe for the Pigo to continue.
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle within stop distance"
            return False
        elif volt() > 14 or volt() < 6:
            print "Voltage outside of safe range: " + str(volt())
            return False
        else:
            return True

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "There is something " + str(self.status['dist']) + "mm away from me!"

    ######
    ###### COMPLEX METHODS
    ######

    def dance(self):
        self.spin()
        self.shuffle()
        self.shakeServo()
        self.rturn()
        self.lturn()
        self.blink()
    ######
    ###### MAIN APP STARTS HERE
    ######
piggy = Pigo()

while piggy.keepGoing():
    piggy.checkDist()
    piggy.fwd()
    time.sleep(2)
    piggy.stop()

piggy.stop()