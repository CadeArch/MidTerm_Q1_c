import math
import numpy as n

class ExamQ1:


    def __init__(self, vel, duration, startX):
        self.velocity = vel
        self.length = 4
        self.theta = math.pi / 6 # 30 degrees
        self.duration = duration
        self.psi = 0
        self.visitedList = [[startX, 0]]

        # if i wont use polar x location it can start at the beginning of unit circle
        self.xloc = startX
        self.yloc = 0

    def driveCommands(self, dt):

        for t in n.arange(0, self.duration, dt):
            # multiply in dt?
            self.psi = self.psi + (self.velocity / self.length) * (math.tan(self.theta) * dt)
            self.xloc = self.xloc - (self.velocity * math.sin(self.psi) * dt)
            self.yloc = self.yloc + (self.velocity * math.cos(self.psi) * dt)

            # converting to radians
            self.radians = math.radians(self.psi)

            self.visitedList.append([self.xloc, self.yloc])

        return self.visitedList

