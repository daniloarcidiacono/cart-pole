from PyQt5.QtCore import QRectF, QPointF, Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication

from pyplots.axes_plot import AxesPlot
from pyplots.line_plot import LinePlot
from pyplots.plot_widget import PlotWidget
from src.math.razvan_cartpole import RazvanCartPole
from src.math.rk4_integrator import RK4Integrator

class Camera:
    def __init__(self, screen_w, screen_h, zoom=100):
        self._zoom = zoom
        self._screen_w = screen_w
        self._screen_h = screen_h

    def tX(self, value):
        return value * self._zoom + self._screen_w/2

    def tY(self, value):
        return value * -self._zoom + self._screen_h/2

    def tL(self, value):
        return value * self._zoom

class CartPoleEnvironment:
    def __init__(self, initX=0,initTheta=0,initV=0,initThetaV=0, forceStrength=100, cartWidth=3, cartHeight = 1, poleThickness=0.1, cartColor=(0, 0, 0), poleColor=(255, 0, 0)):
        self._integrator = RK4Integrator()
        self._equations = RazvanCartPole(g=9.8, mc=5, mp=0.1, l=1, muc=0.9, mup=0.1)
        self._forceStrength = forceStrength

        # Cosmetic parameters
        self._cartColor = cartColor
        self._poleColor = poleColor
        self._poleThickness = poleThickness
        self._cartWidth = cartWidth
        self._cartHeight = cartHeight

        # Initial parameters
        self._t = self._initT = 0
        self._x = self._initX = initX
        self._theta = self._initTheta = initTheta
        self._v = self._initV = initV
        self._thetaV = self._initThetaV = initThetaV

    def move(self, amount):
        self._equations._F = amount * self._forceStrength

    def reset(self):
        self._t = self._initT
        self._x = self._initX
        self._theta = self._initTheta
        self._v = self._initV
        self._thetaV = self._initThetaV

    def update(self, h):
        self._t, self._x, self._theta, self._v, self._thetaV = \
            self._integrator.integrate(self._equations,
                                       self._t,
                                       self._x,
                                       self._theta,
                                       self._v,
                                       self._thetaV,
                                       h)
        # Reset the force
        self._equations._F = 0

    def draw(self, camera):
        pygame.draw.rect(screen, self._cartColor, (
            camera.tX(self._x - self._cartWidth / 2),
            camera.tY(0 + self._cartHeight / 2),
            camera.tL(self._cartWidth),
            camera.tL(self._cartHeight)
        ), 0)

        pygame.draw.lines(screen, self._poleColor, False, [
            (
                camera.tX(self._x),
                camera.tY(0)
            ),
            (
                camera.tX(self._x + math.cos(math.pi / 2 - self._theta) * 2*self._equations._l),
                camera.tY(0 + math.sin(math.pi / 2 - self._theta) * 2*self._equations._l)
            )
        ], math.trunc(camera.tL(self._poleThickness)))

import pygame
from pygame.locals import *

import math
import sys

SCREEN_WIDTH = math.trunc(1920 * 0.5)
SCREEN_HEIGHT = math.trunc(1080 * 0.5)
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Qt
app = QApplication(sys.argv)
w = PlotWidget(viewRect=QRectF(-5, -5, 10, 10))
# xPlot = LinePlot(pen=QPen(Qt.red, 0.01), points=[])
thetaPlot = LinePlot(pen=QPen(Qt.green, 0.05), points=[])
# xDPlot = LinePlot(pen=QPen(Qt.blue, 0.01), points=[])
thetaDPlot = LinePlot(pen=QPen(Qt.yellow, 0.05), points=[])
w._plots = [
    AxesPlot(rect=QRectF(0, -5, 120, 10)),
    thetaPlot,
    thetaDPlot
]
w.show()

# Main loop
done = False
clock = pygame.time.Clock()
fps = 0
env = CartPoleEnvironment()
camera = Camera(screen_w=SCREEN_WIDTH, screen_h=SCREEN_HEIGHT, zoom=50)

while not done:
    # Qt
    app.processEvents()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

            if event.key == pygame.K_r:
                env.reset()
                thetaDPlot.clear()
                thetaPlot.clear()

        if event.type == QUIT:
            done = True


    if pygame.key.get_pressed()[pygame.K_LEFT]:
        env.move(-1)

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        env.move(1)

    # Update
    env.update(1 / 60)

    thetaPlot.addPoint(QPointF(
        env._t, env._theta
    ))

    thetaDPlot.addPoint(QPointF(
        env._t, env._thetaV
    ))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw things
    env.draw(camera)

    # Render the FPS
    fpsText = font.render("FPS: %.2f" % round(fps, 2), False, (0, 0, 0))
    screen.blit(fpsText, (0, 0))

    # Update
    pygame.display.update()
    w.update()

    # FPS handling
    clock.tick(60)
    fps = clock.get_fps()

# Close
pygame.quit()
sys.exit()
