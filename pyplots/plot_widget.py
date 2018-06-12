from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QPainter, QTransform
from PyQt5.QtWidgets import QWidget

# Draws a series of plots
class PlotWidget(QWidget):
    def __init__(self, parent=None, viewRect=QRectF(-0.5, 0.5, 1, 1), backgroundColor=Qt.white):
        super().__init__(parent)

        self._viewRect = viewRect
        self._backgroundColor = backgroundColor
        self._mousePressPosition = None
        self._plots = []
        self.setAttribute(Qt.WA_OpaquePaintEvent)

    def resizeEvent(self, event):
        w = self.rect().width()
        h = self.rect().height()

        # Calculate the widget aspect ratio
        aspectRatio = h / w

        # The width of the function space remains constant, so we adjust the height
        adjustedHeight = self._viewRect.width() * aspectRatio

        # We also keep the center of the function space
        center = self._viewRect.center().y()

        # Recalculate
        self._viewRect.setTop(center - adjustedHeight / 2)
        self._viewRect.setBottom(center + adjustedHeight / 2)

    def mousePressEvent(self, event):
        # Keep track of the pressing point
        self._mousePressPosition = event.localPos()

    def mouseMoveEvent(self, event):
        # Calculate the displacement in widget space
        displacement = event.localPos() - self._mousePressPosition

        # Get the widget dimensions (needed for the matrix calculations)
        w = self.rect().width()
        h = self.rect().height()
        l = self._viewRect.left()
        r = self._viewRect.right()
        t = self._viewRect.top()
        b = self._viewRect.bottom()

        # Calculate the displacement in function space (this way the function space moves by the same
        # amount of the mouse pointer)
        displacement = QPointF(displacement.x() * (r - l) / w, displacement.y() * (b - t) / h)

        # Move the camera
        self._viewRect.translate(-displacement)

        # Update the last press position
        self._mousePressPosition = event.localPos()

        # Schedule a repaint
        self.repaint()

    def wheelEvent(self, event):
        if (event.angleDelta().y() > 0):
            self._viewRect = QRectF(self._viewRect.left() * 0.9,
                                    self._viewRect.top() * 0.9,
                                    self._viewRect.width() * 0.9,
                                    self._viewRect.height() * 0.9)
        else:
            self._viewRect = QRectF(self._viewRect.left() * 1.1,
                                    self._viewRect.top() * 1.1,
                                    self._viewRect.width() * 1.1,
                                    self._viewRect.height() * 1.1)

        # Schedule a repaint
        self.repaint()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        # Clear
        qp.setPen(self._backgroundColor)
        qp.setBrush(self._backgroundColor)
        qp.drawRect(self.rect())

        # Get the widget dimensions (needed for the matrix calculations)
        w = self.rect().width()
        h = self.rect().height()

        # function space => widget space
        # [l; r] => [0; w]
        # [t; b] => [0; h]
        # (x - l) * w / (r - l)
        # (y - t) * h / (b - t)
        l = self._viewRect.left()
        r = self._viewRect.right()
        t = self._viewRect.top()
        b = self._viewRect.bottom()

        # Compute the transformation matrix
        # Note: we invert the y axis in order to go upwards
        cameraMatrix = QTransform().scale(1, -1) * QTransform().translate(-l, -t) * QTransform().scale(w / (r - l), h / (b - t))

        # Also compute the inverse camera matrix (it can be useful to draw overlays with zoom-independent size)
        inverseCameraMatrix = cameraMatrix.inverted()

        # Setup
        qp.setTransform(cameraMatrix)

        # Draw the objects
        for plot in self._plots:
            qp.save()
            plot.draw(qp, cameraMatrix, inverseCameraMatrix)
            qp.restore()
