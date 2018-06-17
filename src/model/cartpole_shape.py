from PyQt5.QtCore import QRectF, QLineF
from PyQt5.QtGui import QTransform


# Helper class defining the cart pole shape drawn by CartPoleWidget
# Shape is defined in a box of size (239, 216) centered at origin
class CartPoleShape:
    def __init__(self):
        self._boundingBox = QRectF(
            -239 / 2,
            -216 / 2,
            239,
            216
        )

        self._cartBody = QRectF(
            self._boundingBox.left(),
            self._boundingBox.top() + 82,
            self._boundingBox.width(),
            106
        )

        self._cartJointBody = QRectF(
            self._cartBody.center().x() - 53 / 2,
            self._boundingBox.top() + 53 / 2,
            53,
            self._cartBody.top() - self._boundingBox.top() - 53 / 2
        )

        self._cartJointBall = QRectF(
            self._cartJointBody.center().x() - self._cartJointBody.width() / 2,
            self._cartJointBody.top() - self._cartJointBody.width() / 2,
            self._cartJointBody.width(),
            self._cartJointBody.width()
        )

        self._poleCenter = self._cartJointBall.center()

        self._leftGear = QRectF(
            self._boundingBox.left() + 43 - 26,
            self._boundingBox.top() + 188 - 26,
            26*2,
            26*2
        )

        self._leftGearJoint = QRectF(
            self._boundingBox.left() + 43 - 2,
            self._boundingBox.top() + 188 - 2,
            4,
            4
        )

        self._rightGear = QRectF(
            self._boundingBox.left() + 194 - 26,
            self._boundingBox.top() + 188 - 26,
            26*2,
            26*2
        )

        self._rightGearJoint = QRectF(
            self._boundingBox.left() + 194 - 2,
            self._boundingBox.top() + 188 - 2,
            4,
            4
        )

    def draw(self, qp, pen):
        qp.setPen(pen)
        qp.drawRect(self._cartBody)
        qp.drawLines([
            QLineF(self._cartJointBody.topLeft(), self._cartJointBody.bottomLeft()),
            QLineF(self._cartJointBody.topRight(), self._cartJointBody.bottomRight()),
            QLineF(self._cartJointBody.bottomLeft(), self._cartJointBody.bottomRight())
        ])
        qp.drawArc(self._cartJointBall, 0, 180 * 16)
        qp.drawEllipse(self._leftGear)
        qp.drawEllipse(self._leftGearJoint)
        qp.drawEllipse(self._rightGear)
        qp.drawEllipse(self._rightGearJoint)

    # Computes the model matrix that moves the cart in center and has
    # size width
    def modelMatrix(self, center, width):
        return QTransform.fromScale(width / 239, width / 239) * QTransform.fromTranslate(-center.x(), -center.y())