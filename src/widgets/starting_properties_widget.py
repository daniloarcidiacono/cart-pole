import math

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget
from src.ui.starting_properties_widget_ui import Ui_StartingPropertiesWidget

# Widget for editing the starting conditions of the cart-pole environment
class StartingPropertiesWidget(QWidget):
    # Signal emitted when the model changes
    modelChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_StartingPropertiesWidget()
        self.ui.setupUi(self)

        # Init the data
        self._environment = None
        self.syncUI()

        # Connect signals
        self.ui.spnCartPosition.valueChanged.connect(self.syncModel)
        self.ui.spnCartVelocity.valueChanged.connect(self.syncModel)
        self.ui.spnPoleAngle.valueChanged.connect(self.syncModel)
        self.ui.spnPoleAngleVelocity.valueChanged.connect(self.syncModel)

    # Synchronizes the UI to the current environment
    @pyqtSlot()
    def syncUI(self):
        if self._environment is None:
            self.setEnabled(False)
            return

        self.setEnabled(True)

        self.lockSignals(True)
        self.ui.spnCartPosition.setValue(self._environment._startPosition)
        self.ui.spnCartVelocity.setValue(self._environment._startVelocity)
        self.ui.spnPoleAngle.setValue(math.degrees(self._environment._startAngle))
        self.ui.spnPoleAngleVelocity.setValue(math.degrees(self._environment._startAngleVelocity))
        self.lockSignals(False)

    # Synchronizes the model to the current UI
    @pyqtSlot()
    def syncModel(self):
        self._environment._startPosition = self.ui.spnCartPosition.value()
        self._environment._startVelocity = self.ui.spnCartVelocity.value()
        self._environment._startAngle = math.radians(self.ui.spnPoleAngle.value())
        self._environment._startAngleVelocity = math.radians(self.ui.spnPoleAngleVelocity.value())

        # Notify the changes
        self.modelChanged.emit()

    def lockSignals(self, lock):
        self.ui.spnCartPosition.blockSignals(lock)
        self.ui.spnCartVelocity.blockSignals(lock)
        self.ui.spnPoleAngle.blockSignals(lock)
        self.ui.spnPoleAngleVelocity.blockSignals(lock)

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, val):
        self._environment = val
        self.syncUI()
