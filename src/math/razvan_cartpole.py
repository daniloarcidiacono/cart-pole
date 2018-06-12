import math

def sgn(value):
    return math.fabs(value) / value if value != 0 else 0

# Cart-pole equations without friction
#
# Taken from https://coneural.org/florian/papers/05_cart_pole.pdf
class RazvanFrictionlessCartPole:
    def __init__(self, g = 9.81, F = 0, mp = 1, mc = 1, l = 1):
        self._g = g
        self._F = F
        self._mp = mp
        self._mc = mc
        self._l = l

    # y" = theta" = g(t, x, y, x', y')
    def yFunc(self, t, x, theta, xd, thetaD):
        num = -self._F - self._mp * self._l * thetaD ** 2 * math.sin(theta)
        den = self._mc + self._mp
        expr2 = self._l * (4 / 3 - (self._mp * math.cos(theta) ** 2) / (self._mc + self._mp))
        return (self._g * math.sin(theta) + math.cos(theta) * num / den) / expr2

    # x" = f(t, x, y, x', y', y")
    def xFunc(self, t, x, theta, xd, thetaD, thetaDD):
        num = self._F + self._mp * self._l * (thetaD ** 2 * math.sin(theta) - thetaDD * math.cos(theta))
        den = self._mc + self._mp
        return num / den

# Cart-pole equations with friction
#
# Taken from https://coneural.org/florian/papers/05_cart_pole.pdf
class RazvanCartPole:
    def __init__(self, g = 9.81, F = 0, mp = 1, mc = 1, l = 1, muc = 0.2, mup = 0.1):
        self._g = g
        self._F = F
        self._mp = mp
        self._mc = mc
        self._l = l
        self._muc = muc
        self._mup = mup

    def nc(self, theta, thetaD, thetaDD):
        result = thetaDD * math.sin(theta) + thetaD ** 2 * math.cos(theta)
        result *= -self._mp * self._l
        result += (self._mc + self._mp) * self._g

        return result

    # Computes the thetaDD function with friction assuming a value for sgn(nC * xD)
    def yFunc_signed(self, t, x, theta, xd, thetaD, signNcxD):
        num = math.sin(theta) + self._muc * signNcxD * math.cos(theta)
        num *= -self._mp * self._l * thetaD ** 2
        num += -self._F
        num /= self._mc + self._mp
        num += self._muc * self._g * signNcxD
        num *= math.cos(theta)
        num += self._g * math.sin(theta)
        num -= (self._mup * thetaD) / (self._mp * self._l)

        den = math.cos(theta) - self._muc * signNcxD
        den *= -(self._mp * math.cos(theta)) / (self._mc + self._mp)
        den += 4 / 3
        den *= self._l

        return num / den

    # y" = theta" = g(t, x, y, x', y')
    def yFunc(self, t, x, theta, xd, thetaD):
        thetaDD_pos = self.yFunc_signed(t, x, theta, xd, thetaD, sgn(xd))
        return thetaDD_pos

        # sgnNc = sgn(nc(theta, thetaD, thetaDD_pos))
        #
        # if sgnNc > 0:
        #     return thetaDD_pos
        #
        # if sgnNc < 0:
        #     return thetaDD_friction_func_signed(t, x, theta, xd, thetaD, sgn(-xd))
        #
        # return thetaDD_friction_func_signed(t, x, theta, xd, thetaD, 0)

        # Compute thetaDD for both values of sgn(Nc * xD)
        # posValue = thetaDD_friction_func_signed(t, x, theta, xd, thetaD, sgn(xd))
        # zeroValue = thetaDD_friction_func_signed(t, x, theta, xd, thetaD, 0)
        # negValue = thetaDD_friction_func_signed(t, x, theta, xd, thetaD, sgn(-xd))
        #
        # # Recompute sgn(nC * xD) based on the assumed thetaDD values
        # posNcxD = nc(theta, thetaD, posValue)
        # zeroNcxD = nc(theta, thetaD, zeroValue)
        # negNcxD = nc(theta, thetaD, negValue)
        #
        # # Choose the value of thetaDD that agrees with the recomputed sgn(Nc * xD) values
        # if posNcxD > 0 and zeroNcxD != 0 and negNcxD >= 0:
        #     return posValue
        #
        # if zeroNcxD == 0 and posNcxD <= 0 and negNcxD >= 0:
        #     return zeroValue
        #
        # if negNcxD < 0 and posNcxD <= 0 and zeroNcxD != 0:
        #     return negValue

        # raise Exception("Should never reach here [pos = " + posNcxD + ", neg = " + negNcxD + ", zero = " + zeroNcxD + "]")

    # x" = f(t, x, y, x', y', y")
    def xFunc(self, t, x, theta, xd, thetaD, thetaDD):
        ncValue = self.nc(theta, thetaD, thetaDD)
        result = thetaD ** 2 * math.sin(theta) - thetaDD * math.cos(theta)
        result *= self._mp * self._l
        result += self._F
        result -= self._muc * ncValue * sgn(ncValue * xd)
        result /= self._mc + self._mp

        return result
