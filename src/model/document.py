from PyQt5.QtCore import Qt, pyqtSignal, QObject, QBasicTimer, pyqtSlot

from src.math.carpole_environment import CartPoleEnvironment
from src.model.cosmetic_properties import CosmeticProperties

# Keeps the state of the application
class Document(QObject):
    # Signal emitted by markModified
    changed = pyqtSignal()

    # Signal emitted when the system is stepped forward
    systemStepped = pyqtSignal()

    # Signal emitted when the system is resetted
    systemResetted = pyqtSignal()

    # Signal emitted when the simulation state changes
    simulationStateChanged = pyqtSignal()

    # Refresh rate
    FPS = 50

    def __init__(self, parent=None):
        super().__init__(parent)

        # Path name
        self._pathName = None

        # Agent
        self._agent = None

        # Environment
        self._environment = CartPoleEnvironment()

        # Cosmetic properties
        self._cosmeticProperties = CosmeticProperties(self)

        # Timer for update
        self._timer = QBasicTimer()

    def fromJson(self, json):
        self._environment.fromJson(json["environment"])
        self._cosmeticProperties.fromJson(json["cosmetic"])

    def toJson(self):
        return {
            'environment': self._environment.toJson(),
            'cosmetic': self._cosmeticProperties.toJson()
        }

    # Resets the state to the starting conditions
    def reset(self):
        self._environment.reset()
        self.systemResetted.emit()

    def isStarted(self):
        return self._timer.isActive()

    def start(self):
        if not self._timer.isActive():
            # If we start from a violation condition, try to reset first
            if self._environment.constraintsViolated():
                self._environment.reset()
                self.systemResetted.emit()

            # If the initial conditions violate the constraints, we do not start at all
            if not self._environment.constraintsViolated():
                self._timer.start(1000 / self.FPS, Qt.PreciseTimer, self)
                self.simulationStateChanged.emit()

    def pause(self):
        if self._timer.isActive():
            self._timer.stop()
            self.simulationStateChanged.emit()

    def stop(self):
        if self._timer.isActive():
            self._timer.stop()
            self.simulationStateChanged.emit()

    def timerEvent(self, event):
        if event.timerId() == self._timer.timerId():
            self.step(1 / self.FPS)
        else:
            super().timerEvent(event)

    def step(self, h):
        # Simulate
        self._environment._F = self._agent.getAction(self._environment)
        self._environment.step(h)

        # Signal that the environment has been updated
        self.systemStepped.emit()

    @pyqtSlot()
    def markModified(self):
        self.changed.emit()