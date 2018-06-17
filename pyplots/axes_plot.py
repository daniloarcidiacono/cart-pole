from PyQt5.QtCore import QPointF, Qt, QLineF, QRectF
from PyQt5.QtGui import QPen, QFont, QVector2D

# Draws both axis
# Can be passed added to PlotWidget
class AxesPlot:
    def __init__(self,
                 rect=QRectF(-1, -1, 2, 2),
                 pen=QPen(Qt.black, 0),
                 gridPen=QPen(Qt.lightGray, 0),
                 axisX=True,
                 axisY=True,
                 ticks=11,
                 tickHeight=20,
                 font=QFont('Serif', 14, QFont.Light)):
        self._rect = rect
        self._pen = pen
        self._gridPen = gridPen
        self._axisX = axisX
        self._axisY = axisY

        # Number of ticks (at least two)
        self._ticks = ticks
        self._tickHeight = tickHeight
        self._font = font

    def draw(self, qp, cameraMatrix, inverseCameraMatrix):
        # Draw the axis
        qp.setPen(self._pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(
            self._rect
        )

        # Draw the grid
        qp.setPen(self._gridPen)

        # Horizontal ticks
        if self._axisX:
            tickStep = self._rect.width() / (self._ticks - 1)
            for tick in range(self._ticks):
                topPos = QVector2D(self._rect.topLeft()) + QVector2D(1, 0) * tick * tickStep
                bottomPos =  QVector2D(self._rect.bottomLeft()) + QVector2D(1, 0) * tick * tickStep

                # Draw the tick in screen space (this way, the height is not affected by the zoom factor)
                qp.drawLine(
                    QLineF(
                        QPointF(topPos.x(), topPos.y()),
                        QPointF(bottomPos.x(), bottomPos.y())
                    )
                )

        # Vertical ticks
        if self._axisY:
            tickStep = self._rect.height() / (self._ticks - 1)
            for tick in range(self._ticks):
                leftPos = QVector2D(self._rect.topLeft()) + QVector2D(0, 1) * tick * tickStep
                rightPos =  QVector2D(self._rect.topRight()) + QVector2D(0, 1) * tick * tickStep

                # Draw the tick in screen space (this way, the height is not affected by the zoom factor)
                qp.drawLine(
                    QLineF(
                        QPointF(leftPos.x(), leftPos.y()),
                        QPointF(rightPos.x(), rightPos.y())
                    )
                )

        # Draw in widget space (useful for overlays)
        oldTransform = qp.transform()
        qp.resetTransform()

        qp.setFont(self._font)
        metrics = qp.fontMetrics()
        fh = metrics.height()
        qp.setPen(self._pen)

        # Draw horizontal ticks
        if self._axisX:
            tickStep = self._rect.width() / (self._ticks - 1)
            for tick in range(self._ticks):
                # Tick position in function space
                tickPos = QVector2D(self._rect.topLeft()) + QVector2D(1, 0) * tick * tickStep

                # Calculate the tick position in screen space
                screenTickPos = cameraMatrix.map(QPointF(tickPos.x(), tickPos.y()))

                # Draw the tick in screen space (this way, the height is not affected by the zoom factor)
                qp.drawLine(
                    QLineF(
                        screenTickPos.x(),
                        screenTickPos.y(),
                        screenTickPos.x(),
                        screenTickPos.y() + self._tickHeight
                    )
                )

                # Draw the label in screen space (this way, the font size is not affected by the zoom factor)
                caption = str(round(tickPos.x(), 2))
                fw = metrics.width(caption)
                qp.drawText(
                    QPointF(
                        screenTickPos.x() - fw / 2,
                        screenTickPos.y() + self._tickHeight + fh
                    ),
                    caption
                )

        # Draw vertical ticks
        if self._axisY:
            tickStep = self._rect.height() / (self._ticks - 1)
            for tick in range(self._ticks):
                # Tick position in function space
                tickPos = QVector2D(self._rect.topLeft()) + QVector2D(0, 1) * tick * tickStep

                # Calculate the tick position in screen space
                screenTickPos = cameraMatrix.map(QPointF(tickPos.x(), tickPos.y()))

                # Draw the tick in screen space (this way, the height is not affected by the zoom factor)
                qp.drawLine(
                    QLineF(
                        screenTickPos.x(),
                        screenTickPos.y(),
                        screenTickPos.x() - self._tickHeight,
                        screenTickPos.y()
                    )
                )

                # Draw the label in screen space (this way, the font size is not affected by the zoom factor)
                caption = str(round(tickPos.y(), 2))
                fw = metrics.width(caption)
                qp.drawText(
                    QPointF(
                        screenTickPos.x() - self._tickHeight - fw,
                        screenTickPos.y() + fh / 4
                    ),
                    caption
                )

        qp.setTransform(oldTransform)

