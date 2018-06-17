from PyQt5.QtCore import QRectF, Qt, QPointF, pyqtSlot
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget

from pyplots.axes_plot import AxesPlot
from pyplots.legend_plot import LegendPlot
from pyplots.line_plot import LinePlot
from src.ui.cart_pole_graph_widget_ui import Ui_CartPoleGraphWidget


# Widget that displays the cart pole plots
class CartPoleGraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_CartPoleGraphWidget()
        self.ui.setupUi(self)

        # Plots data
        self._axesPlot = AxesPlot(rect=QRectF(0, -5, 10, 10), ticks=5)
        self._plotsData = {
            'position': LinePlot(points=[], pen=QPen(Qt.darkGreen, 0.05), title="Position (x)"),
            'velocity': LinePlot(points=[], pen=QPen(Qt.darkMagenta, 0.05), title="Velocity (x')"),
            'angle': LinePlot(points=[], pen=QPen(Qt.red, 0.05), title="Pole angle (θ)"),
            'angularVelocity': LinePlot(points=[], pen=QPen(Qt.blue, 0.05), title="Pole angle velocity (θ')")
        }

        # Init the plot widget
        self.ui.plotWidget._viewRect = QRectF(0, -5, 10, 10)
        self.ui.plotWidget._plots = [
            self._axesPlot,
            self._plotsData['position'],
            self._plotsData['velocity'],
            self._plotsData['angle'],
            self._plotsData['angularVelocity'],

            LegendPlot([
                self._plotsData['position'],
                self._plotsData['velocity'],
                self._plotsData['angle'],
                self._plotsData['angularVelocity']
            ])
        ]

    @pyqtSlot(int)
    def on_chkPosition_stateChanged(self, state):
        self._plotsData['position']._hidden = state == Qt.Unchecked
        self.ui.plotWidget.update()

    @pyqtSlot(int)
    def on_chkVelocity_stateChanged(self, state):
        self._plotsData['velocity']._hidden = state == Qt.Unchecked
        self.ui.plotWidget.update()

    @pyqtSlot(int)
    def on_chkAngle_stateChanged(self, state):
        self._plotsData['angle']._hidden = state == Qt.Unchecked
        self.ui.plotWidget.update()

    @pyqtSlot(int)
    def on_chkAngleVelocity_stateChanged(self, state):
        self._plotsData['angularVelocity']._hidden = state == Qt.Unchecked
        self.ui.plotWidget.update()

    def clearAll(self):
        for plot in self._plotsData.values():
            plot.clear()

        self.ui.plotWidget.update()

    def addPoint(self, plotName, x, y):
        if plotName in self._plotsData:
            self._plotsData[plotName].addPoint(QPointF(x, y))
            self.ui.plotWidget.update()