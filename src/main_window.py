from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QDockWidget
from src.model.document import Document
from src.ui.main_window_ui import Ui_MainWindow
from src.widgets.cosmetic_properties_widget import CosmeticPropertiesWidget
from src.widgets.physical_properties_widget import PhysicalPropertiesWidget
from src.widgets.simulation_widget import SimulationWidget
from src.widgets.starting_properties_widget import StartingPropertiesWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the document
        self._document = Document()

        # Init the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initDockWidgets()

        # Inject the cart pole in the visualizer
        self.ui.cartPoleWidget.cartPole = self._document._parameters

        # Done
        self.showMaximized()

        self._status_update_timer = QTimer(self)
        self._status_update_timer.setSingleShot(False)
        self._status_update_timer.timeout.connect(self.updateStatus)
        self._status_update_timer.start(500)

    def updateStatus(self):
        self._document._parameters._poleThickness *= 1.1
        self._document._parameters.notifyChanges()

    def initDockWidgets(self):
        # Create the containers of the widget that can be docked
        cosmeticPropertiesDockWidget = QDockWidget()
        physicalPropertiesDockWidget = QDockWidget()
        startingPropertiesDockWidget = QDockWidget()
        simulationDockWidget = QDockWidget()

        # Instance the widgets
        self._cosmeticPropertiesWidget = CosmeticPropertiesWidget(cosmeticPropertiesDockWidget)
        self._physicalPropertiesWidget = PhysicalPropertiesWidget(physicalPropertiesDockWidget)
        self._startingPropertiesWidget = StartingPropertiesWidget(startingPropertiesDockWidget)
        self._simulationWidget = SimulationWidget(simulationDockWidget)

        # Add them to the UI
        self.addDockWidget(Qt.LeftDockWidgetArea, cosmeticPropertiesDockWidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, physicalPropertiesDockWidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, startingPropertiesDockWidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, simulationDockWidget)

        # Inject the data into the dock widget
        self._cosmeticPropertiesWidget.parameters = self._document._parameters