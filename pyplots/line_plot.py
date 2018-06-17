from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QPen

# Line plot
# Can be passed added to PlotWidget
class LinePlot:
    def __init__(self, points=[], pen=QPen(Qt.black, 0), title="LinePlot"):
        self._points = points
        self._pen = pen
        self._repaintIndex = 0
        self._title = title
        self._hidden = False

    def clear(self):
        self._points.clear()
        self._repaintIndex = 0

    def addPoint(self, point):
        self._points.append(point)
        # self._repaintIndex = max(0, len(self._points) - 2)

    def draw(self, qp, cameraMatrix, inverseCameraMatrix):
        if self._hidden:
            return

        qp.setPen(self._pen)
        # qp.drawLines(self._points)

        i = self._repaintIndex
        while i + 1 < len(self._points):
           qp.drawLine(
                QLineF(
                    self._points[i],
                    self._points[i + 1]
                )
           )

           i += 1