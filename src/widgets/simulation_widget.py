from PyQt5.QtWidgets import QWidget
from src.ui.simulation_widget_ui import Ui_SimulationWidget

# Widget for controlling the physical simulator
class SimulationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_SimulationWidget()
        self.ui.setupUi(self)