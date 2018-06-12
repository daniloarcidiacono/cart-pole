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
# by applying RK4, using time step h
class RK4Integrator:
    def __init__(self):
        pass

    def integrate(self, equations, t0, x0, y0, x0d, y0d, h):
        f = equations.xFunc
        g = equations.yFunc

        # Approximation of y" in t0
        l0 = g(t0, x0, y0, x0d, y0d) # = y0dd

        # Approximation of x" in t0
        k0 = f(t0, x0, y0, x0d, y0d, l0) # = x0dd

        # Approximation of x' in t0
        m0 = x0d

        # Approximation of y' in t0
        n0 = y0d

        # Approximation of x(t0 + h/2), using derivative at t0
        k0Half = x0 + h / 2 * m0

        # Approximation of y(t0 + h/2), using derivative at t0
        l0Half = y0 + h / 2 * n0

        # Approximation of x'(t0 + h/2), using second derivative at t0
        m0Half = x0d + h / 2 * k0

        # Approximation of y'(t0 + h/2), using second derivative at t0
        n0Half = y0d + h / 2 * l0

        # Value of y"(t0 + h / 2), using approximate first derivative and values
        l1 = g(t0 + h / 2, k0Half, l0Half, m0Half, n0Half)

        # Value of x"(t0 + h / 2), using approximate first derivate and values, and computed y"(t0 + h / 2) for coupling
        k1 = f(t0 + h / 2, k0Half, l0Half, m0Half, n0Half, l1)

        # Approximation of x'(t0 + h/2), using second derivative at t0
        m1 = m0Half #= m0 + h / 2 * k0

        # Approximation of y'(t0 + h/2), using second derivative at t0
        n1 = n0Half #=y0d + h / 2 * l0

        # Approximation of x(t0 + h/2), using derivative at t0 + h / 2 this time
        k1Half = x0 + h / 2 * m1

        # Approximation of y(t0 + h/2), using derivative at t0 + h / 2 this time
        l1Half = y0 + h / 2 * n1

        # Approximation of x'(t0 + h/2), using second derivative at t0 + h / 2 this time
        m1Half = x0d + h / 2 * k1

        # Approximation of y'(t0 + h/2), using second derivative at t0 + h / 2 this time
        n1Half = y0d + h / 2 * l1

        # Value of y"(t0 + h / 2), using approximate first derivative and values
        l2 = g(t0 + h / 2, k1Half, l1Half, m1Half, n1Half)

        # Value of x"(t0 + h / 2), using approximate first derivate and values, and computed y"(t0 + h / 2) for coupling
        k2 = f(t0 + h / 2, k1Half, l1Half, m1Half, n1Half, l2)

        # Approximation of x'(t0 + h/2), using second derivative at t0
        m2 = m1Half #= m0 + h / 2 * k1

        # Approximation of y'(t0 + h/2), using second derivative at t0
        n2 = n1Half #=y0d + h / 2 * l1

        # Approximation of x(t0 + h), using derivative at t0 + h / 2
        k2Full = x0 + h * m2

        # Approximation of y(t0 + h), using derivative at t0 + h / 2
        l2Full = y0 + h * n2

        # Approximation of x'(t0 + h), using second derivative at t0 + h / 2
        m2Full = x0d + h * k2

        # Approximation of y'(t0 + h/2), using second derivative at t0 + h / 2
        n2Full = y0d + h * l2

        # Value of y"(t0 + h), using approximate first derivative and values
        l3 = g(t0 + h, k2Full, l2Full, m2Full, n2Full)

        # Value of x"(t0 + h), using approximate first derivate and values, and computed y"(t0 + h) for coupling
        k3 = f(t0 + h, k2Full, l2Full, m2Full, n2Full, l3)

        # Approximation of x'(t0 + h), using second derivative at t0 + h / 2
        m3 = m2Full #= m0 + h * k2

        # Approximation of y'(t0 + h), using second derivative at t0 + h / 2
        n3 = n2Full #=y0d + h * l2

        # Finally, compute the result
        t1 = t0 + h
        x1 = x0 + h / 6 * (m0 + 2 * m1 + 2 * m2 + m3)
        x1d = x0d + h / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
        y1 = y0 + h / 6 * (n0 + 2 * n1 + 2 * n2 + n3)
        y1d = y0d + h / 6 * (l0 + 2 * l1 + 2 * l2 + l3)

        return [t1, x1, y1, x1d, y1d]
