import math
import time
from datetime import datetime
from ExamQ1 import ExamQ1
from matplotlib import pyplot as p

length = 4
alpha = math.pi / 6
vel = 20
duration = 10


radiusPath = length / math.tan(alpha)
print("radius: ", radiusPath)
pathCircumf = 2 * radiusPath * math.pi
print("path Circumfrence: ", pathCircumf)
oneRevSec = pathCircumf / vel
print("time for one revolution: ", oneRevSec)
totalRev = duration / oneRevSec
print("total revolutions", totalRev)
oneRevDist = (vel * duration) / totalRev
print("distance for one revolution: ", oneRevDist)
print("total Distance traveled: ", pathCircumf * totalRev)
print("total Distance traveled: ", oneRevDist * totalRev)

endPosition = (totalRev - 4) * oneRevDist
print("end distance into 5th revolution (arc length) ", endPosition)
thetaEndPosition = (endPosition * 360) / (2 * math.pi * radiusPath)
print("theta of end position", thetaEndPosition)
radiansEndPos = math.radians(thetaEndPosition)
gutCheck = math.radians(180) # this gives end location being (-r, 0) YAY
bestEndX = radiusPath * math.cos(radiansEndPos)
bestEndY = radiusPath * math.sin(radiansEndPos)
print("theoretical end position", "( " + str(bestEndX) + ", " + str(bestEndY) + ")")
truePoint = [bestEndX, bestEndY]

robotExam = ExamQ1(vel, duration, radiusPath)
robotExam1 = ExamQ1(vel, duration, radiusPath)
robotExam2 = ExamQ1(vel, duration, radiusPath)
robotExamGut = ExamQ1(vel, duration, radiusPath)

def xandyPos(visitedPoints):
    xlist = []
    ylist = []

    for point in visitedPoints:
        xlist.append(point[0])
        ylist.append(point[1])
    return xlist, ylist

timeInit = time.time()
print(timeInit)
visitedExam1 = robotExam.driveCommands(1)
timeFinal = time.time()
print(timeFinal)
cTime = timeFinal - timeInit

xPositions1sec, yPositions = xandyPos(visitedExam1)
# print("\n\n (xLoc, yLoc): " , robotExam.visitedList)
print("\ntotal points on graph: ", len(robotExam.visitedList))
print("last point position 1 dt", "(" + str(xPositions1sec[len(xPositions1sec) - 1]) + ", " + str(yPositions[len(yPositions) - 1]) + ")" )
print("theoretical end position", "(" + str(bestEndX) + ", " + str(bestEndY) + ")")
dt1Point = [xPositions1sec[len(xPositions1sec) - 1], yPositions[len(yPositions) - 1]]

timeInit = time.time()
visitedExam2 = robotExam1.driveCommands(0.1)
timeFinal = time.time()
cTime1 = timeFinal - timeInit

xPositions01, yPositions1 = xandyPos(visitedExam2)
# print("\n\n (xLoc, yLoc): " , robotExam1.visitedList)
print("\ntotal points on graph: ", len(robotExam1.visitedList))
print("last point position 0.1 dt", "(" + str(xPositions01[len(xPositions01) - 1]) + ", " + str(yPositions1[len(yPositions1) - 1]) + ")" )
print("theoretical end position", "(" + str(bestEndX) + ", " + str(bestEndY) + ")")
dt01Point = [xPositions01[len(xPositions01) - 1], yPositions1[len(yPositions1) - 1]]

timeInit = time.time()
visitedExam3 = robotExam2.driveCommands(0.01)
xPositions001, yPositions2 = xandyPos(visitedExam3)
timeFinal = time.time()
cTime2 = timeFinal - timeInit

# print("\n\n (xLoc, yLoc): " , robotExam2.visitedList)
print("\ntotal points on graph: ", len(robotExam2.visitedList))
print("last point position 0.01 dt", "(" + str(xPositions001[len(xPositions001) - 1]) + ", " + str(yPositions2[len(yPositions2) - 1]) + ")" )
print("theoretical end position", "(" + str(bestEndX) + ", " + str(bestEndY) + ")")
dt001point = [xPositions001[len(xPositions001) - 1], yPositions2[len(yPositions2) - 1]]

# this is a gutcheck taking a really small time step
# timeInit = time.time()
# visitedExamSmall = robotExamGut.driveCommands(0.00001)
# timeFinal = time.time()
# cTime3 = timeFinal - timeInit
#
# xPositionsSmall, yPositionsSmall = xandyPos(visitedExamSmall)
# # print("\n\n (xLoc, yLoc): " , robotExamGut.visitedList)
# print("\n (xLoc, yLoc): ", len(robotExamGut.visitedList))
# print("last point position 0.01 dt", "( " + str(xPositionsSmall[len(xPositionsSmall) - 1]) + ", " + str(yPositionsSmall[len(yPositionsSmall) - 1]) + ")" )
# print("theoretical end position", "( " + str(bestEndX) + ", " + str(bestEndY) + ")")

# to plot the resulting path of each robot with different timesteps
# p.plot(xPositions1sec, yPositions, lw="2.5")
# p.title("dt 1")
# p.show()
#
# p.plot(xPositions01, yPositions1, marker='o', color="orange")
# p.title("dt 0.1")
# p.show()
#
# p.plot(xPositions001, yPositions2, marker='o', color="black")
# p.title("dt 0.01")
# p.show()

# distance formula
def distance(point1, point2):
    dis = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    return dis

# distance between final point of each different robot with different time steps
error = distance(truePoint,dt1Point)
error1 = distance(truePoint,dt01Point)
error2 = distance(truePoint,dt001point)

# plotting errors
fig = p.figure()
langs = ['dt-1', 'dt-0.1', 'dt-0.01']
metersOff = [error, error1, error2]
p.bar(langs,metersOff)
p.xlabel("time steps in seconds")
p.ylabel("error in meters")
p.title("error in different time steps")
p.show()

print(cTime, cTime1, cTime2)
fig = p.figure()
langs = ['dt-1', 'dt-0.1', 'dt-0.01']
metersOff = [cTime, cTime1, cTime2]
p.bar(langs,metersOff)
p.xlabel("time steps in seconds")
p.ylabel("compute time")
p.title("compute time in different time steps")
p.show()

