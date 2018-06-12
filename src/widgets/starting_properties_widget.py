from PyQt5.QtWidgets import QWidget
from src.ui.starting_properties_widget_ui import Ui_StartingPropertiesWidget

# Widget for editing the starting conditions of the cart-pole environment
class StartingPropertiesWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_StartingPropertiesWidget()
        self.ui.setupUi(self)