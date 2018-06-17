# Agent that simply stores a force
class UserAgent:
    def __init__(self):
        self._force = 0
        pass

    def getAction(self, env):
        old = self._force
        # self._force = 0
        return old