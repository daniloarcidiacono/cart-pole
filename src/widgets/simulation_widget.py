from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget

from src.agents.dqn_agent import DQNAgent
from src.agents.heuristic_agent import HeuristicAgent
from src.math.euler_integrator import EulerIntegrator
from src.math.rk4_integrator import RK4Integrator
from src.agents.user_agent import UserAgent
from src.ui.simulation_widget_ui import Ui_SimulationWidget


# Widget for controlling the physical simulator
class SimulationWidget(QWidget):
    # Signal emitted when the model changes
    integratorChanged = pyqtSignal()
    agentChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Init the UI
        self.ui = Ui_SimulationWidget()
        self._pauseIcon = QIcon(":/icons/icons/pause.png")
        self._playIcon = QIcon(":/icons/icons/play.png")
        self.ui.setupUi(self)

        # Note: the order must match the combo box
        self._integrators = [ RK4Integrator(), EulerIntegrator() ]
        self._agents = [ HeuristicAgent(), DQNAgent(), UserAgent() ]

        # Init the data
        self._document = None
        self.syncUI()

        # Connect signals
        self.ui.btnStartPause.clicked.connect(self.onStartPauseClicked)
        self.ui.btnReset.clicked.connect(self.onResetClicked)
        self.ui.cboIntegrator.currentIndexChanged.connect(self.onIntegratorChanged)
        self.ui.cboCartAgent.currentIndexChanged.connect(self.onAgentChanged)

    @pyqtSlot(int)
    def onIntegratorChanged(self, index):
        self._document._environment._integrator = self._integrators[index]
        self.integratorChanged.emit()

    @pyqtSlot(int)
    def onAgentChanged(self, index):
        self._document._agent = self._agents[index]
        self.agentChanged.emit()

    @pyqtSlot()
    def onStartPauseClicked(self):
        if not self._document.isStarted():
            self._document.start()
        else:
            self._document.stop()

    @pyqtSlot()
    def onResetClicked(self):
        self._document.reset()

    # Synchronizes the UI to the current document
    @pyqtSlot()
    def syncUI(self):
        self.setEnabled(self._document is not None)
        if self._document is None:
            self.ui.cboIntegrator.setCurrentIndex(-1)
            self.ui.cboCartAgent.setCurrentIndex(-1)
            return

        self.lockSignals(True)
        self.ui.cboIntegrator.setCurrentIndex(self._integrators.index(self._document._environment._integrator))
        self.ui.cboCartAgent.setCurrentIndex(self._agents.index(self._document._agent))
        self.ui.btnStartPause.setEnabled((self._document._environment._integrator is not None) and (self._document._environment._equations is not None))

        if self._document.isStarted():
            self.ui.btnStartPause.setText("Stop")
            self.ui.btnStartPause.setIcon(self._pauseIcon)
        else:
            self.ui.btnStartPause.setText("Start")
            self.ui.btnStartPause.setIcon(self._playIcon)

        self.lockSignals(False)

    def lockSignals(self, lock):
        self.ui.btnStartPause.blockSignals(lock)
        self.ui.btnReset.blockSignals(lock)
        self.ui.cboIntegrator.blockSignals(lock)
        self.ui.cboCartAgent.blockSignals(lock)

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, val):
        if self._document is not None:
            self._document.simulationStateChanged.disconnect(self.syncUI)

        self._document = val

        if self._document is not None:
            self._document.simulationStateChanged.connect(self.syncUI)

        if self._document is not None:
            # Set a default integrator
            if self._document._environment._integrator is None:
                self._document._environment._integrator = self._integrators[1]
                self.integratorChanged.emit()

            # Set a default agent
            if self._document._agent is None:
                self._document._agent = self._agents[0]
                self.agentChanged.emit()

        self.syncUI()
