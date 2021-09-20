import math
import numpy as n

class ExamQ1:


    def __init__(self, vel, duration):
        self.velocity = vel
        self.length = 4
        self.psi = 0
        self.xPos = 0
        self.yPos = 0
        self.visitedList = [[0, 0]]
        self.duration = duration

    def driveCommands(self, dt):
        self.visitedList = [[0, 0]]
        self.xPos = 0
        self.yPos = 0
        xVel = self.velocity * math.sin(math.pi / 6)
        yVel = self.velocity * math.cos(math.pi / 6)
        for t in n.arange(0, self.duration, dt):
            self.psi = self.psi + 30 * dt
            self.xPos = self.xPos + xVel * dt
            self.yPos = self.yPos + yVel * dt
            self.visitedList.append([self.xPos, self.yPos])

        return self.visitedList
