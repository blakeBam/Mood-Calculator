from LinearMoodSegment import LinearMoodSegment
from CubicMoodSegment import CubicMoodSegment
import os
import matplotlib.pyplot as plt
import numpy as np


def readFile(fileName):
    with open(fileName, 'r') as f:
        return f.read()


def getListOfSegments(segmentStringCSV):
    segmentList = []
    segmentLines = segmentStringCSV.splitlines()
    for i in range(len(segmentLines) - 1):
        startPoint = tuple(map(float, segmentLines[i].split(',')))
        endPoint = tuple(map(float, segmentLines[i + 1].split(',')))
        newSegment = LinearMoodSegment(startPoint, endPoint)
        segmentList.append(newSegment)
    return segmentList


def test():
    x = CubicMoodSegment((1, 3), (2, 4), 0, 0)
    print(x.cubicCoefficients)
    xRange = np.linspace(1, 2, 100)
    y = 0
    size = len(x.cubicCoefficients)
    for i in range(size):
        y += x.cubicCoefficients[i] * (xRange ** (size - 1 - i))
    plt.plot(xRange, y, 'b-')
    plt.plot([2, 3], [4, 4], 'b-')
    plt.plot([0, 1], [3, 3], 'b-')
    plt.show()


def main():
    segmentPointsFile = os.getcwd() + "\\MoodData.csv"
    segmentList = getListOfSegments(readFile(segmentPointsFile))
    xList = []
    yList = []
    for segment in segmentList:
        xList.append(segment.startPoint[0])
        yList.append(segment.startPoint[1])
    xList.append(segmentList[-1].startPoint[0])
    yList.append(segmentList[-1].startPoint[1])
    plt.plot(xList, yList)
    plt.show()


if __name__ == "__main__":
    test()
