import math

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget

from src.math.barto_cartpole import BartoCartPole
from src.math.razvan_cartpole import RazvanCartPole, RazvanFrictionlessCartPole
from src.ui.physical_properties_widget_ui import Ui_PhysicalPropertiesWidget

# Widget for editing the "physical" properties of the cart-pole environment
class PhysicalPropertiesWidget(QWidget):
    # Signal emitted when the model changes
    modelChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_PhysicalPropertiesWidget()
        self.ui.setupUi(self)

        # Note: the order must match the combo box
        self._models = [
            RazvanCartPole(),
            RazvanFrictionlessCartPole(),
            BartoCartPole()
        ]

        # Init the data
        self._environment = None
        self._cosmetic = None
        self.syncUI()

        # Connect signals
        self.ui.cboModel.currentIndexChanged.connect(self.syncModel)
        self.ui.spnGravity.valueChanged.connect(self.syncModel)
        self.ui.spnCartMass.valueChanged.connect(self.syncModel)
        self.ui.spnPoleMass.valueChanged.connect(self.syncModel)
        self.ui.spnPoleLength.valueChanged.connect(self.syncModel)
        self.ui.spnCartFriction.valueChanged.connect(self.syncModel)
        self.ui.spnPoleFriction.valueChanged.connect(self.syncModel)
        self.ui.spnLeftBound.valueChanged.connect(self.syncModel)
        self.ui.spnRightBound.valueChanged.connect(self.syncModel)
        self.ui.spnAngleTolerance.valueChanged.connect(self.syncModel)
        self.ui.btnShowAngleTolerance.toggled.connect(self.syncModel)

    # Synchronizes the UI to the current environment
    @pyqtSlot()
    def syncUI(self):
        self.setEnabled(self._environment is not None and self._cosmetic is not None)
        if self._environment is None or self._cosmetic is None:
            self.ui.cboModel.setCurrentIndex(-1)
            return

        self.lockSignals(True)
        self.ui.cboModel.setCurrentIndex(self._models.index(self._environment._equations))
        self.ui.spnGravity.setValue(self._environment._g)
        self.ui.spnCartMass.setValue(self._environment._mc)
        self.ui.spnPoleMass.setValue(self._environment._mp)
        self.ui.spnPoleLength.setValue(self._environment._l)
        self.ui.spnCartFriction.setValue(self._environment._muc)
        self.ui.spnPoleFriction.setValue(self._environment._mup)
        self.ui.spnLeftBound.setValue(self._environment._leftBound)
        self.ui.spnRightBound.setValue(self._environment._rightBound)
        self.ui.spnAngleTolerance.setValue(math.degrees(self._environment._angleTolerance))
        self.ui.btnShowAngleTolerance.setChecked(self._cosmetic._showAngleTolerance)
        self.lockSignals(False)

    def lockSignals(self, lock):
        self.ui.cboModel.blockSignals(lock)
        self.ui.spnGravity.blockSignals(lock)
        self.ui.spnCartMass.blockSignals(lock)
        self.ui.spnPoleMass.blockSignals(lock)
        self.ui.spnPoleLength.blockSignals(lock)
        self.ui.spnCartFriction.blockSignals(lock)
        self.ui.spnPoleFriction.blockSignals(lock)
        self.ui.spnLeftBound.blockSignals(lock)
        self.ui.spnRightBound.blockSignals(lock)
        self.ui.spnAngleTolerance.blockSignals(lock)
        self.ui.btnShowAngleTolerance.blockSignals(lock)

    # Synchronizes the model to the current UI
    @pyqtSlot()
    def syncModel(self):
        self._environment._equations = self._models[self.ui.cboModel.currentIndex()]
        self._environment._g = self.ui.spnGravity.value()
        self._environment._mc = self.ui.spnCartMass.value()
        self._environment._mp = self.ui.spnPoleMass.value()
        self._environment._l = self.ui.spnPoleLength.value()
        self._environment._muc = self.ui.spnCartFriction.value()
        self._environment._mup = self.ui.spnPoleFriction.value()
        self._environment._leftBound = self.ui.spnLeftBound.value()
        self._environment._rightBound = self.ui.spnRightBound.value()
        self._environment._angleTolerance = math.radians(self.ui.spnAngleTolerance.value())
        self._cosmetic._showAngleTolerance = self.ui.btnShowAngleTolerance.isChecked()

        # Notify the changes
        self.modelChanged.emit()

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, val):
        self._environment = val

        if self._environment is not None:
            # Set a default model
            if self._environment._equations is None:
                self._environment._equations = self._models[2]

        self.syncUI()

    @property
    def cosmeticProperties(self):
        return self._cosmetic

    @cosmeticProperties.setter
    def cosmeticProperties(self, val):
        self._cosmetic = val
        self.syncUI()

