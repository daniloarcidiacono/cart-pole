from PyQt5.QtWidgets import QWidget
from src.ui.cosmetic_properties_widget_ui import Ui_CosmeticPropertiesWidget

# Widget for editing the "cosmetic" (i.e. visual) properties of the cart-pole environment
class CosmeticPropertiesWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_CosmeticPropertiesWidget()
        self.ui.setupUi(self)

        # Init the data
        self._parameters = None
        self.syncUI()

        # Connect signals
        self.connectSignals()

    # Synchronizes the UI to the current parameters
    def syncUI(self):
        if self._parameters is None:
            self.setEnabled(False)
            return

        self.setEnabled(True)

        self.disconnectSignals()
        self.ui.colBackground.color = self._parameters._backgroundColor
        self.ui.colCart.color = self._parameters._cartColor
        self.ui.spnCartWidth.setValue(self._parameters._cartWidth)
        self.ui.spnCartHeight.setValue(self._parameters._cartHeight)
        self.ui.colPole.color = self._parameters._poleColor
        self.ui.spnPoleThickness.setValue(self._parameters._poleThickness)
        self.connectSignals()

    # Synchronizes the model to the current UI
    def syncModel(self):
        self.disconnectSignals()
        self._parameters._backgroundColor = self.ui.colBackground.color
        self._parameters._cartColor = self.ui.colCart.color
        self._parameters._cartWidth = self.ui.spnCartWidth.value()
        self._parameters._cartHeight = self.ui.spnCartHeight.value()
        self._parameters._poleColor = self.ui.colPole.color
        self._parameters._poleThickness = self.ui.spnPoleThickness.value()

        # Notify the changes
        self._parameters.notifyChanges()
        self.connectSignals()

    def connectSignals(self):
        if self._parameters is not None:
            self._parameters.changed.connect(self.syncUI)

        self.ui.colBackground.colorChanged.connect(self.syncModel)
        self.ui.colCart.colorChanged.connect(self.syncModel)
        self.ui.spnCartWidth.valueChanged.connect(self.syncModel)
        self.ui.spnCartHeight.valueChanged.connect(self.syncModel)
        self.ui.colPole.colorChanged.connect(self.syncModel)
        self.ui.spnPoleThickness.valueChanged.connect(self.syncModel)

    def disconnectSignals(self):
        if self._parameters is not None:
            self._parameters.changed.disconnect(self.syncUI)

        self.ui.colBackground.colorChanged.disconnect(self.syncModel)
        self.ui.colCart.colorChanged.disconnect(self.syncModel)
        self.ui.spnCartWidth.valueChanged.disconnect(self.syncModel)
        self.ui.spnCartHeight.valueChanged.disconnect(self.syncModel)
        self.ui.colPole.colorChanged.disconnect(self.syncModel)
        self.ui.spnPoleThickness.valueChanged.disconnect(self.syncModel)

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, val):
        if self._parameters is not None:
            self._parameters.changed.disconnect(self.syncUI)

        self._parameters = val

        if self._parameters is not None:
            self._parameters.changed.connect(self.syncUI)

        self.syncUI()

