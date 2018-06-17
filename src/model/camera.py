from PyQt5.QtGui import QTransform

# Defines the view camera
class Camera:
    def __init__(self):
        self._center = [0, 0]
        self._horizontalLength = 5

    # Returns the camera transform
    def getViewTransform(self):
        return QTransform(
            1, 0, 0,
            0, 1, 0,
            -self._center[0], -self._center[1], 1
        )

    def getProjTransform(self, w, h):
        coeff = w / self._horizontalLength

        return QTransform(
            coeff, 0, 0,
            0, coeff, 0,
            w / 2, h / 2, 1
        )

