from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget
from src.ui.cosmetic_properties_widget_ui import Ui_CosmeticPropertiesWidget

# Widget for editing the CosmeticProperties
class CosmeticPropertiesWidget(QWidget):
    # Signal emitted when the model changes
    modelChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_CosmeticPropertiesWidget()
        self.ui.setupUi(self)

        # Init the data
        self._properties = None
        self.syncUI()

        # Connect signals
        self.ui.colBackground.colorChanged.connect(self.syncModel)
        self.ui.colCart.colorChanged.connect(self.syncModel)
        self.ui.spnCartWidth.valueChanged.connect(self.syncModel)
        self.ui.colPole.colorChanged.connect(self.syncModel)

    # Synchronizes the UI to the current document
    @pyqtSlot()
    def syncUI(self):
        if self._properties is None:
            self.setEnabled(False)
            return

        self.setEnabled(True)

        self.lockSignals(True)
        self.ui.colBackground.color = self._properties._backgroundColor
        self.ui.colCart.color = self._properties._cartColor
        self.ui.spnCartWidth.setValue(self._properties._cartWidth)
        self.ui.colPole.color = self._properties._poleColor
        self.lockSignals(False)

    # Synchronizes the model to the current UI
    @pyqtSlot()
    def syncModel(self):
        self._properties._backgroundColor = self.ui.colBackground.color
        self._properties._cartColor = self.ui.colCart.color
        self._properties._cartWidth = self.ui.spnCartWidth.value()
        self._properties._poleColor = self.ui.colPole.color

        # Notify the changes
        self.modelChanged.emit()

    def lockSignals(self, lock):
        self.ui.colBackground.blockSignals(lock)
        self.ui.colCart.blockSignals(lock)
        self.ui.spnCartWidth.blockSignals(lock)
        self.ui.colPole.blockSignals(lock)

    @property
    def document(self):
        return self._properties

    @document.setter
    def document(self, val):
        self._properties = val
        self.syncUI()

