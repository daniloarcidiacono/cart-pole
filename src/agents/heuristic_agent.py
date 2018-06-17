import math

def sgn(value):
    return math.fabs(value) / value if value != 0 else 0

# Agent that counters the angle
class HeuristicAgent:
    def __init__(self):
        pass

    def getAction(self, env):
        return -10 if env._angle < 0 else 10

