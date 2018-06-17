import math

from PyQt5.QtCore import Qt, QRectF, QLineF, QPointF, QElapsedTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QFont, QTransform
from PyQt5.QtWidgets import QWidget

from pyplots.axes_plot import AxesPlot
from src.model.camera import Camera

# Widget that displays the cart pole
from src.model.cartpole_shape import CartPoleShape


class CartPoleWidget(QWidget):
    # Emitted when a key is pressed
    keyPressed = pyqtSignal(object)

    def __init__(self, parent):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)

        # Init data
        self._font = QFont('Serif', 14, QFont.Light)
        self._fpsTimer = QElapsedTimer()
        self._frameCount = 0
        self._fps = 0
        self._fpsTimer.start()
        self._camera = Camera()
        self._displayFrameRate = False
        self._cosmeticProperties = None
        self._environment = None
        self._cartShape = CartPoleShape()
        self._axisPlot = AxesPlot(
            rect=QRectF(-1, 0, 2, 0),
            axisX=True,
            axisY=False,
            pen=QPen(Qt.blue, 0),
            font=self._font,
            ticks=11,
            tickHeight=20
        )
        self.setEnabled(False)

    def mousePressEvent(self, event):
        # Keep track of the pressing point
        self._mousePressPosition = event.localPos()

    def mouseMoveEvent(self, event):
        # Calculate the displacement
        displacement = event.localPos() - self._mousePressPosition

        # Move the camera
        self._camera._center[0] -= displacement.x()
        self._camera._center[1] -= displacement.y()

        # Update the last press position
        self._mousePressPosition = event.localPos()

        # Schedule a repaint
        self.repaint()

    def keyPressEvent(self, event):
        self.keyPressed.emit(event)
        super().keyPressEvent(event)

    def wheelEvent(self, event):
        if (event.angleDelta().y() > 0):
            self._camera._horizontalLength *= 0.9
        else:
            self._camera._horizontalLength *= 1.1

        # Schedule a repaint
        self.repaint()

    def paintEvent(self, e):
        if self._cosmeticProperties is not None:
            qp = QPainter()
            qp.begin(self)
            self.drawWidget(qp)
            qp.end()

    # Returns the plot point at angle
    # (note: angle is the angle of the pole w.r.t. the vertical)
    def getPolePoint(self, center, angle):
        return QPointF(
            center.x() + math.cos(math.pi / 2 - angle) * self._environment._l * 2,
            center.y() - math.sin(math.pi / 2 - angle) * self._environment._l * 2
        )

    def drawWidget(self, qp):
        # Clear
        qp.setPen(self._cosmeticProperties._backgroundColor)
        qp.setBrush(self._cosmeticProperties._backgroundColor)
        qp.drawRect(self.rect())

        # Setup the font
        qp.setFont(self._font)
        qp.setPen(QPen(Qt.black, 0))

        # During simulation, we display the frame rate
        if self._displayFrameRate:
            # Calculate the FPS
            self._frameCount += 1
            if self._fpsTimer.elapsed() >= 1000:
                self._fps = self._frameCount / (self._fpsTimer.restart() / 1000)
                self._frameCount = 0

        # Draw the FPS, environment state and time
        self.drawStatistics(qp)

        # Get viewport size
        w = self.rect().width()
        h = self.rect().height()

        # Compute the view-projection matrix
        viewProj = self._camera.getProjTransform(w, h) * self._camera.getViewTransform()

        # Compute the model matrix for the cart
        model = self._cartShape.modelMatrix(QPointF(-self._environment._position, 0), self._cosmeticProperties._cartWidth)

        # Draw the cart in world space
        qp.setTransform(model * viewProj)
        pen = QPen(self._cosmeticProperties._cartColor, 0)
        self._cartShape.draw(qp, pen)

        # Reset the model matrix for the cart
        qp.setTransform(viewProj)

        # Transform the cart shapes in world space
        cartBounds = model.mapRect(self._cartShape._boundingBox)
        cartBody = model.mapRect(self._cartShape._cartBody)
        poleCenter = model.map(self._cartShape._poleCenter)

        # Draw the bounds (in world space)
        qp.setPen(QPen(Qt.blue, 0))
        qp.drawLines(
            [
                QLineF(
                    self._environment._leftBound,
                    cartBounds.bottom(),
                    self._environment._rightBound,
                    cartBounds.bottom()
                ),
                QLineF(
                    self._environment._leftBound,
                    cartBounds.bottom(),
                    self._environment._leftBound,
                    cartBody.top(),
                ),
                QLineF(
                    self._environment._rightBound,
                    cartBounds.bottom(),
                    self._environment._rightBound,
                    cartBody.top(),
                )
            ]
        )

        # Draw the horizontal axis
        self._axisPlot._rect = QRectF(self._environment._leftBound, cartBounds.bottom(), self._environment._rightBound - self._environment._leftBound, 0)
        self._axisPlot.draw(qp, viewProj, QTransform())

        # Calculate pole position and bounds
        poleMassMin = self.getPolePoint(poleCenter, -self._environment._angleTolerance)
        poleMass = self.getPolePoint(poleCenter, self._environment._angle)
        poleMassMax = self.getPolePoint(poleCenter, self._environment._angleTolerance)

        # Draw the pole bounds
        if self._cosmeticProperties._showAngleTolerance:
            qp.setPen(QPen(self._cosmeticProperties._poleColor, 0, Qt.DashLine))
            qp.drawLine(QLineF(poleCenter, poleMassMin))
            qp.drawLine(QLineF(poleCenter, poleMassMax))

        # Draw the pole
        qp.setPen(QPen(self._cosmeticProperties._poleColor, self._cosmeticProperties._poleThickness, Qt.SolidLine, Qt.RoundCap))
        qp.setBrush(self._cosmeticProperties._poleColor)
        qp.drawLine(QLineF(poleCenter, poleMass))

    def drawStatistics(self, qp):
        metrics = qp.fontMetrics()
        fw_avg = metrics.averageCharWidth()
        fh = metrics.height()

        if self._displayFrameRate:
            # Draw the fps (in screen space)
            qp.drawText(
                QPointF(
                    fw_avg,
                    fh
                ),
                str(round(self._fps, 2)) + " frames per second"
            )

        qp.drawText(
            QPointF(
                fw_avg,
                2 * fh
            ),
            "Position: %.2f m, Velocity: %.2f m/s" % (self._environment._position, self._environment._velocity)
        )

        qp.drawText(
            QPointF(
                fw_avg,
                3 * fh
            ),
            "Angle: %.2f deg, Angle velocity: %.2f deg/s" % (math.degrees(self._environment._angle), math.degrees(self._environment._angleVelocity))
        )

        # Draw the time (in screen space)
        qp.drawText(
            QPointF(
                fw_avg,
                4 * fh
            ),
            str(round(self._environment._time, 2)) + " seconds"
        )

    # Synchronizes the ui
    def syncUI(self):
        if self._environment is None or self._cosmeticProperties is None:
            self.setEnabled(False)
            return

        self.setEnabled(True)

    @property
    def cosmeticProperties(self):
        return self._cosmeticProperties

    @cosmeticProperties.setter
    def cosmeticProperties(self, val):
        self._cosmeticProperties = val
        self.syncUI()

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, val):
        self._environment = val
        self.syncUI()

