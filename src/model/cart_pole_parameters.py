# Defines the cart pole parameters
from PyQt5.QtCore import Qt, pyqtSignal, QObject


# Parameters of the cart-pole environment (physical, cosmetic, starting conditions)
class CartPoleParameters(QObject):
    # Signal emitted by notifyChanges
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Physical properties
        self._gravityForce = 9.8
        self._cartMass = 1
        self._poleMass = 1
        self._poleLength = 1
        self._frictionCart = 1
        self._frictionPole = 1

        # Cosmetic properties
        self._backgroundColor = Qt.white
        self._cartColor = Qt.black
        self._cartWidth = 3
        self._cartHeight = 1
        self._poleColor = Qt.red
        self._poleThickness = 0.1

        # Starting conditions
        self._startPosition = 0
        self._startVelocity = 0
        self._startAngle = 0
        self._startAngleVelocity = 0

        # Actual status
        self._position = self._startPosition
        self._velocity = self._startVelocity
        self._angle = self._startAngle
        self._angleVelocity = self._startAngleVelocity

    # Resets the state to the starting conditions
    def reset(self):
        self._position = self._startPosition
        self._velocity = self._startVelocity
        self._angle = self._startAngle
        self._angleVelocity = self._startAngleVelocity

    def notifyChanges(self):
        self.changed.emit()
