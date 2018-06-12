import math

def sgn(value):
    return math.fabs(value) / value if value != 0 else 0

# Cart-pole equations
#
# Taken from https://coneural.org/florian/papers/05_cart_pole.pdf
class BartoCartPole:
    def __init__(self, g = 9.81, F = 0, mp = 1, mc = 1, l = 1, muc = 0.2, mup = 0.1):
        self._g = g
        self._F = F
        self._mp = mp
        self._mc = mc
        self._l = l
        self._muc = muc
        self._mup = mup

    # y" = theta" = g(t, x, y, x', y')
    def yFunc(self, t, x, theta, xd, thetaD):
        num = -self._F - self._mp * self._l * thetaD ** 2 * math.sin(theta) + self._muc * sgn(xd)
        num /= self._mc + self._mp
        num *= math.cos(theta)
        num += self._g * math.sin(theta)
        num -= (self._mup * thetaD) / (self._mp * self._l)

        den = -(self._mp * math.cos(theta) ** 2) / (self._mc + self._mp)
        den += 4 / 3
        den *= self._l

        return num / den

    # x" = f(t, x, y, x', y', y")
    def xFunc(self, t, x, theta, xd, thetaD, thetaDD):
        num = self._F + self._mp * self._l * (thetaD ** 2 * math.sin(theta) - thetaDD * math.cos(theta)) - self._muc * sgn(xd)
        den = self._mc + self._mp
        return num / den
