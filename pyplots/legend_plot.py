from PyQt5.QtCore import QPointF, Qt, QLineF, QRectF

# Legend of line plots
# Can be passed added to PlotWidget
from PyQt5.QtGui import QFont, QPen, QBrush

class LegendPlot:
    def __init__(self, plots, rect=QRectF(20, 20, 250, 100), pen=QPen(Qt.black, 0), brush=QBrush(Qt.white), font=QFont('Serif', 14, QFont.Light)):
        self._plots = plots
        self._pen = pen
        self._font = font
        self._brush = brush
        self._rect = rect

    def draw(self, qp, cameraMatrix, inverseCameraMatrix):
        # Draw in screen space
        qp.resetTransform()

        # Setup the font
        qp.setFont(self._font)
        metrics = qp.fontMetrics()
        fh = metrics.height()

        # Clear
        qp.setPen(self._pen)
        qp.setBrush(self._brush)
        qp.drawRect(self._rect)

        curY = fh
        for plot in self._plots:
            # Draw the plot line
            qp.setPen(plot._pen)
            # qp.drawLine(
            #     QLineF(
            #         0,
            #         fh / 2,
            #         10,
            #         fh / 2
            #     )
            # )

            # Draw the plot name
            qp.drawText(
                QPointF(
                    self._rect.left() + metrics.averageCharWidth(),
                    self._rect.top() + curY
                ),
                plot._title
            )

            # New row
            curY += fh