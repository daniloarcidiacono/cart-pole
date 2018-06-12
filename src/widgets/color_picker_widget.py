from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QColorDialog

# Colored box that when clicked displays a QColorDialog
class ColorPickerWidget(QWidget):
    # Signal emitted when the color changes
    colorChanged = pyqtSignal(QColor)

    def __init__(self, parent, color = Qt.white):
        super().__init__(parent)
        self._color = color

    def mousePressEvent(self, event):
        newColor = QColorDialog.getColor(initial=self._color, parent=self)

        if newColor.isValid():
            self._color = newColor
            self.colorChanged.emit(self._color)
            self.repaint()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        # Clear
        qp.setPen(self._color)
        qp.setBrush(self._color)
        qp.drawRect(self.rect())
        qp.end()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        self._color = val
        self.colorChanged.emit(self._color)
        self.repaint()