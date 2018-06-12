# Solves the following system of second order ODEs
#
# { x" = f(t, x, y, x', y', y")
# { y" = g(t, x, y, x', y')
#
# with initial values
#
# t0
# x(t0) = x0
# y(t0) = y0
# x'(t0) = x0d
# y'(t0) = y0d
#
# by applying Euler, using time step h
class EulerIntegrator:
    def __init__(self):
        pass

    def integrate(self, equations, t0, x0, y0, x0d, y0d, h):
        f = equations.xFunc
        g = equations.yFunc

        # Approximation of y" in t0
        l0 = g(t0, x0, y0, x0d, y0d) # = y0dd

        # Approximation of x" in t0
        k0 = f(t0, x0, y0, x0d, y0d, l0) # = x0dd

        t1 = t0 + h
        x1d = x0d + h * k0
        y1d = y0d + h * l0
        x1 = x0 + h * x1d
        y1 = y0 + h * y1d

        return [t1, x1, y1, x1d, y1d]