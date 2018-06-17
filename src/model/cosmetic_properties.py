import json
from PyQt5.QtCore import QObject, pyqtSignal, Qt

from PyQt5.QtGui import QColor


# Contains the cosmetic (i.e. visual) properties of the cart-pole environment
class CosmeticProperties(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Cosmetic properties
        self._backgroundColor = Qt.white
        self._cartColor = Qt.black
        self._cartWidth = 1
        self._poleColor = Qt.red
        self._poleThickness = 0.05
        self._showAngleTolerance = True

    def fromJson(self, json):
        self._backgroundColor = QColor.fromRgb(json["backgroundColor"]["r"], json["backgroundColor"]["g"],
                                               json["backgroundColor"]["b"])
        self._cartColor = QColor.fromRgb(json["cartColor"]["r"], json["cartColor"]["g"], json["cartColor"]["b"])
        self._cartWidth = json["cartWidth"]
        self._poleColor = QColor.fromRgb(json["poleColor"]["r"], json["poleColor"]["g"], json["poleColor"]["b"])
        self._showAngleTolerance = json["showAngleTolerance"]

    def toJson(self):
        # Qt.red ecc are integers
        bg = QColor(self._backgroundColor)
        pl = QColor(self._poleColor)
        cc = QColor(self._cartColor)

        return {
            'backgroundColor': {
                'r': bg.red(),
                'g': bg.green(),
                'b': bg.blue(),
            },
            'cartColor': {
                'r': cc.red(),
                'g': cc.green(),
                'b': cc.blue(),
            },
            'cartWidth': self._cartWidth,
            'poleColor': {
                'r': pl.red(),
                'g': pl.green(),
                'b': pl.blue(),
            },
            'showAngleTolerance': self._showAngleTolerance
        }