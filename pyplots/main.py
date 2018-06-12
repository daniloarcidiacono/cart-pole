import math
import sys

from PyQt5.QtCore import QPointF, Qt, QRectF
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication

from pyplots.axis_plot import AxisPlot
from pyplots.line_plot import LinePlot
from pyplots.plot_widget import PlotWidget

#
# Solve IVP:
#
# x^2 y'' + xy' - y = 3x
#
# y(1) = 1
# y'(1) = 0
#
# Analytical solution
#
# y(x) = -x/4 + 5/(4x) + 3/2 x log x
# y'(x) = 1/4 * (-5/(x**2) + 6 * log (x) + 5
def solution(x):
    return -x/4 + 5/(4*x) + 3/2 * x * math.log(x)

def solutionDer(x):
    return 1 / 4 * (-5 / (x ** 2) + 6 * math.log(x) + 5)

# Generates a series of #pts QPointF of type (x; f(x)) from x in [start; end]
# Ill-defined values are skipped
def funcGen(f, start, end, pts):
    result = []
    step = (end - start) / (pts - 1)
    for i in range(pts):
        x = start + i * step
        try:
            y = f(x)
            result.append(QPointF(x, y))
        except ArithmeticError:
            pass

    return result

# Write the IVP as a linear system of two equations:
#
#  y'' = (3x - xy' + y) / x^2
#
#  { z = dy/dx = f(x, y, z) = z
#  { dz/dx = (3x - xz + y) / x^2 = g(x, y, z)
#
def rk4_f(x, y, z):
    return z

def rk4_g(x, y, z):
    return (3*x - x * z + y) / (x**2)

# RK4 for the system
#
# { z = dy/dx = f(x, y, z)
# { dz/dx = g(x, y, z)
#
# on interval [x0; xn] with N sampled points
#
# (x0, y0, z0) starting conditions
#
# Algorithm taken from
#
# https://math.stackexchange.com/questions/721076/help-with-using-the-runge-kutta-4th-order-method-on-a-system-of-2-first-order-od
def rk4(f, g, x0, xn, N, y0, z0):
    result = []
    h = (xn - x0) / N

    # Starting point
    x = x0
    y = y0
    z = z0

    for i in range(N):
        k0 = h * f(x, y, z)
        l0 = h * g(x, y, z)
        k1 = h * f(x + 1 / 2 * h, y + 1 / 2 * k0, z + 1 / 2 * l0)
        l1 = h * g(x + 1 / 2 * h, y + 1 / 2 * k0, z + 1 / 2 * l0)
        k2 = h * f(x + 1 / 2 * h, y + 1 / 2 * k1, z + 1 / 2 * l1)
        l2 = h * g(x + 1 / 2 * h, y + 1 / 2 * k1, z + 1 / 2 * l1)
        k3 = h * f(x + h, y + k2, z + l2)
        l3 = h * g(x + h, y + k2, z + l2)

        # Stepping
        y += 1 / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
        z += 1 / 6 * (l0 + 2 * l1 + 2 * l2 + l3)
        x += h

        # Resulting
        result.append(QPointF(x, y))

    return result

app = QApplication(sys.argv)
w = PlotWidget(viewRect=QRectF(-math.pi, -math.pi, 2 * math.pi, 2 * math.pi))
w._plots = [
    AxisPlot(startPt=QPointF(-3, 0), endPt=QPointF(3, 0), axisPen=QPen(Qt.black, 0), ticks=7),
    AxisPlot(startPt=QPointF(0, 0), endPt=QPointF(0, 8), axisPen=QPen(Qt.black, 0), ticks=9),
    LinePlot(points=funcGen(solution, 0.2, 3, 50), pen=QPen(Qt.blue, 0, Qt.SolidLine, Qt.RoundCap)),
    LinePlot(points=funcGen(solutionDer, 0.2, 3, 50), pen=QPen(Qt.red, 0, Qt.SolidLine, Qt.RoundCap)),
    LinePlot(points=rk4(rk4_f, rk4_g, 0.2, 3, 200, solution(0.2), solutionDer(0.2)), pen=QPen(Qt.green, 0, Qt.SolidLine, Qt.RoundCap))
]
w.showMaximized()
sys.exit(app.exec_())


