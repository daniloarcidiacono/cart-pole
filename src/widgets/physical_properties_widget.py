from PyQt5.QtWidgets import QWidget
from src.ui.physical_properties_widget_ui import Ui_PhysicalPropertiesWidget

# Widget for editing the "physical" properties of the cart-pole environment
class PhysicalPropertiesWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_PhysicalPropertiesWidget()
        self.ui.setupUi(self)