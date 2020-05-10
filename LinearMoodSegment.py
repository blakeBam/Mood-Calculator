from BaseMoodSegment import BaseMoodSegment


class LinearMoodSegment(BaseMoodSegment):
    """Line segment for a period of time in mood"""

    def __init__(self, start, end):
        super().__init__(start, end)
        self.slope = (end[1] - start[1]) / (end[0] - start[0])
