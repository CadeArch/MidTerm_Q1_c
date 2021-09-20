from ExamQ1 import ExamQ1
from matplotlib import pyplot as p

vel= 20
duration = 10
robotExam = ExamQ1(vel, duration)

def xandyPos(visitedPoints):
    xPositions1 = []
    yPositions1 = []

    for x in visitedPoints:
        xPositions1.append(x[0])
        yPositions1.append(x[1])
    return xPositions1, yPositions1


visitedExam1 = robotExam.driveCommands(1)
xPositions1sec, yPositions1sec = xandyPos(visitedExam1)
print("\n\n (xLoc, yLoc): " , robotExam.visitedList)
print("\n (xLoc, yLoc): ", len(robotExam.visitedList))

visitedExam2 = robotExam.driveCommands(0.1)
xPositions01, yPositions01 = xandyPos(visitedExam2)
print("\n\n (xLoc, yLoc): " , robotExam.visitedList)
print("\n (xLoc, yLoc): ", len(robotExam.visitedList))

visitedExam3 = robotExam.driveCommands(0.01)
xPositions001, yPositions001 = xandyPos(visitedExam3)
print("\n\n (xLoc, yLoc): " , robotExam.visitedList)
print("\n (xLoc, yLoc): ", len(robotExam.visitedList))


p.plot(xPositions1sec, yPositions1sec, marker='o', color="green")
p.title("error - diff d/t 1, 0.1, 0.01")
p.ylabel("yPos (meters)")
p.xlabel("xPos (meters)")
p.show()

p.plot(xPositions01, yPositions01, marker='o', color="orange")
p.title("error - diff d/t 1, 0.1, 0.01")
p.ylabel("yPos (meters)")
p.xlabel("xPos (meters)")
p.show()

p.plot(xPositions001, yPositions001, marker='o', color="black")
p.title("error - diff d/t 1, 0.1, 0.01")
p.ylabel("yPos (meters)")
p.xlabel("xPos (meters)")
p.show()

