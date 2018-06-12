import math

from PyQt5.QtCore import Qt, QRectF, QLineF, QPointF
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QWidget

from src.model.camera import Camera

# Widget that displays the cart pole
class CartPoleWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Cart pole data
        self._cartPole = None
        self.setEnabled(False)

        # Camera
        self._camera = Camera()

        # Font
        self._font = None


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

    def wheelEvent(self, event):
        if (event.angleDelta().y() > 0):
            self._camera._horizontalLength *= 0.9
        else:
            self._camera._horizontalLength *= 1.1

        # Schedule a repaint
        self.repaint()

    def paintEvent(self, e):
        if self._cartPole is not None:
            qp = QPainter()
            qp.begin(self)
            self.drawWidget(qp)
            qp.end()

    def drawWidget(self, qp):
        # Clear
        qp.setPen(self._cartPole._backgroundColor)
        qp.setBrush(self._cartPole._backgroundColor)
        qp.drawRect(self.rect())

        # Get viewport size
        w = self.rect().width()
        h = self.rect().height()

        # Draw the ground (we draw in screen space to get an infinite plane)
        qp.setPen(QPen(Qt.blue, 0))
        qp.drawLine(
            QLineF(
                0,
                h / 2 - self._camera._center[1],
                w,
                h / 2 - self._camera._center[1]
            )
        )

        # Compute the camera matrix
        viewProj = self._camera.getProjTransform(w, h) * self._camera.getViewTransform()

        # Draw the horizontal ticks
        self.drawTicks(qp, -5, 5, 10, viewProj)

        # If we have the cart data set
        if self._cartPole is not None:
            # Apply the camera transform
            qp.setTransform(viewProj)

            # Draw the cart
            qp.setPen(QPen(self._cartPole._cartColor, 0))
            qp.setBrush(self._cartPole._cartColor)
            qp.drawRect(
                QRectF(
                    self._cartPole._position - self._cartPole._cartWidth / 2,
                    -self._cartPole._cartHeight / 2,
                    self._cartPole._cartWidth,
                    self._cartPole._cartHeight
                )
            )

            # Calculate pole position
            # (note: poleAngle is the angle of the pole w.r.t. the vertical)
            poleMassX = self._cartPole._position + math.cos(math.pi / 2 - self._cartPole._angle) * self._cartPole._poleLength * 2
            poleMassY = -math.sin(math.pi / 2 - self._cartPole._angle) * self._cartPole._poleLength * 2

            # Draw the pole
            qp.setPen(QPen(self._cartPole._poleColor, self._cartPole._poleThickness, Qt.SolidLine, Qt.RoundCap))
            qp.setBrush(self._cartPole._poleColor)
            qp.drawLine(
                QLineF(
                    self._cartPole._position,
                    0,
                    poleMassX,
                    poleMassY
                )
            )

    # Draws the horizontal ticks
    def drawTicks(self, qp, start, end, tickHeight, viewProj):
        if self._font is None:
            self._font = QFont('Serif', 14, QFont.Light)

        qp.setFont(self._font)
        metrics = qp.fontMetrics()
        fh = metrics.height()

        # Draw ticks
        for tick in range(start, end + 1):
            # Calculate the tick position in screen space
            screenTickPos = viewProj.map(QPointF(tick, 0))

            # Draw the tick in screen space (this way, the height is not affected by the zoom factor)
            qp.drawLine(
                QLineF(
                    screenTickPos.x(),
                    screenTickPos.y() + tickHeight,
                    screenTickPos.x(),
                    screenTickPos.y() - tickHeight
                )
            )

            # Draw the label in screen space (this way, the font size is not affected by the zoom factor)
            caption = str(tick)
            fw = metrics.width(caption)
            qp.drawText(
                QPointF(
                    screenTickPos.x() - fw / 2,
                    screenTickPos.y() + tickHeight + fh
                ),
                caption
            )

    # Synchronizes the ui
    def syncUI(self):
        if self._cartPole is None:
            self.setEnabled(False)
            return

        self.setEnabled(True)

    @property
    def cartPole(self):
        return self._cartPole

    @cartPole.setter
    def cartPole(self, val):
        if self._cartPole is not None:
            self._cartPole.changed.disconnect(self.repaint)

        self._cartPole = val

        if self._cartPole is not None:
            self._cartPole.changed.connect(self.repaint)

        self.syncUI()
