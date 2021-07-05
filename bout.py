from boxer import Boxer
from math import sqrt, atan2,pi, degrees
import numpy as np

class Bout:
    def __init__(self, boxer1, boxer2):
        self.boxer1 = boxer1
        self.boxer2 = boxer2

    def xDistanceBetweenFighters(self, xLocationBoxer1, xLocationBoxer2):
        return(abs(xLocationBoxer1 - xLocationBoxer2))
    def yDistanceBetweenFighters(self, yLocationBoxer1, yLocationBoxer2):
        return(abs(yLocationBoxer1 - yLocationBoxer2))
    def pythagDistance(self, xLocationBoxer1, xLocationBoxer2, yLocationBoxer1, yLocationBoxer2):
        return(sqrt(self.xDistanceBetweenFighters(xLocationBoxer1, xLocationBoxer2)**2 + self.yDistanceBetweenFighters(yLocationBoxer1, yLocationBoxer2)**2))
    def basicReachInRangeAssessment(self, xLocationBoxer1, xLocationBoxer2, yLocationBoxer1, yLocationBoxer2):
        if self.pythagDistance(xLocationBoxer1, xLocationBoxer2, yLocationBoxer1, yLocationBoxer2) < self.boxer1.reach:
            print(self.boxer1.name, "in range")
        else:
            print(self.boxer1.name, "out of range")
        if self.pythagDistance(xLocationBoxer1, xLocationBoxer2, yLocationBoxer1, yLocationBoxer2) < self.boxer2.reach:
            print(self.boxer2.name, "in range")
        else:
            print(self.boxer2.name, "out of range")

    def getAngleOfLineBetweenTwoPoints(self,p1, p2):
        xDiff = p2.xLocation - p1.xLocation
        yDiff = p2.yLocation - p1.yLocation
        angle = 90+degrees(atan2(yDiff, xDiff))
        return(angle)
        #sentence = print('Angle from', p1.name, 'to', p2.name,"{:.0f}".format(angle), 'degrees')

    def ringSetup(self):
        for y in range(11):
            for x in range(11):
                if y == self.boxer1.yLocation and x == self.boxer1.xLocation and y == self.boxer2.yLocation and x == self.boxer2.xLocation:
                    print("*",end= ' ')
                elif y == self.boxer1.yLocation and x == self.boxer1.xLocation:
                    print(self.boxer1.name[0],end= ' ')
                elif y == self.boxer2.yLocation and x == self.boxer2.xLocation:
                    print(self.boxer2.name[0],end= ' ')
                elif x == 0:
                    print('.', end= ' ')
                elif y == 0 or y == 10:
                    print('.', end= ' ')
                else:
                    print(' ', end= ' ')
            print('.')

    def determineLongerReach(self):
        if self.boxer1.reach > self.boxer2.reach:
            print(self.boxer1.name,'has the longer reach')
        elif self.boxer1.reach < self.boxer2.reach:
            print(self.boxer1.name,'has the longer reach')
        else:
            print('Both fights have the same reach')

    def determineStrongerChin(self):
        if self.boxer1.chin > self.boxer2.chin:
            print(self.boxer1.name,'has the stronger chin')
        elif self.boxer1.chin < self.boxer2.chin:
            print(self.boxer1.name,'has the stronger chin')
        else:
            print('Both fights have the same chin')
