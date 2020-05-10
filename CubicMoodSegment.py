from BaseMoodSegment import BaseMoodSegment
import numpy as np


class CubicMoodSegment(BaseMoodSegment):
    """Cubic segment for a period of time in mood"""

    def __init__(self, start, end, startSlope, endSlope):
        super().__init__(start, end)
        self.startSlope = startSlope
        self.endSlope = endSlope
        self.cubicCoefficients = self.calculateCubicEquation()

    def calculateCubicEquation(self):
        startX = self.startPoint[0]
        startY = self.startPoint[1]
        endX = self.endPoint[0]
        endY = self.endPoint[1]
        coefficientMatrix = np.array([
            [startX ** 3, startX ** 2, startX, 1],
            [endX ** 3, endX ** 2, endX, 1],
            [3 * (startX ** 2), 2 * startX, 1, 0],
            [3 * (endX ** 2), 2 * endX, 1, 0]
        ])
        bVector = np.array(
            [startY, endY, self.startSlope, self.endSlope]
        )

        try:
            return np.linalg.solve(coefficientMatrix, bVector)
        except np.linalg.LinAlgError:
            return None
