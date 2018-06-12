# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cosmetic_properties_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CosmeticPropertiesWidget(object):
    def setupUi(self, CosmeticPropertiesWidget):
        CosmeticPropertiesWidget.setObjectName("CosmeticPropertiesWidget")
        CosmeticPropertiesWidget.resize(460, 177)
        self.formLayout = QtWidgets.QFormLayout(CosmeticPropertiesWidget)
        self.formLayout.setObjectName("formLayout")
        self.lblBackgroundColor = QtWidgets.QLabel(CosmeticPropertiesWidget)
        self.lblBackgroundColor.setObjectName("lblBackgroundColor")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblBackgroundColor)
        self.colBackground = ColorPickerWidget(CosmeticPropertiesWidget)
        self.colBackground.setObjectName("colBackground")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.colBackground)
        self.lblCartColor = QtWidgets.QLabel(CosmeticPropertiesWidget)
        self.lblCartColor.setObjectName("lblCartColor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCartColor)
        self.colCart = ColorPickerWidget(CosmeticPropertiesWidget)
        self.colCart.setObjectName("colCart")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.colCart)
        self.lblCartWidth = QtWidgets.QLabel(CosmeticPropertiesWidget)
        self.lblCartWidth.setObjectName("lblCartWidth")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblCartWidth)
        self.spnCartWidth = QtWidgets.QDoubleSpinBox(CosmeticPropertiesWidget)
        self.spnCartWidth.setObjectName("spnCartWidth")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spnCartWidth)
        self.lblCartHeight = QtWidgets.QLabel(CosmeticPropertiesWidget)
        self.lblCartHeight.setObjectName("lblCartHeight")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblCartHeight)
        self.spnCartHeight = QtWidgets.QDoubleSpinBox(CosmeticPropertiesWidget)
        self.spnCartHeight.setObjectName("spnCartHeight")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spnCartHeight)
        self.lblPoleColor = QtWidgets.QLabel(CosmeticPropertiesWidget)
        self.lblPoleColor.setObjectName("lblPoleColor")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblPoleColor)
        self.colPole = ColorPickerWidget(CosmeticPropertiesWidget)
        self.colPole.setObjectName("colPole")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.colPole)
        self.lblPoleThickness = QtWidgets.QLabel(CosmeticPropertiesWidget)
        self.lblPoleThickness.setObjectName("lblPoleThickness")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblPoleThickness)
        self.spnPoleThickness = QtWidgets.QDoubleSpinBox(CosmeticPropertiesWidget)
        self.spnPoleThickness.setSingleStep(0.05)
        self.spnPoleThickness.setObjectName("spnPoleThickness")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spnPoleThickness)
        self.lblBackgroundColor.setBuddy(self.colBackground)
        self.lblCartColor.setBuddy(self.colCart)
        self.lblCartWidth.setBuddy(self.spnCartWidth)
        self.lblCartHeight.setBuddy(self.spnCartHeight)
        self.lblPoleColor.setBuddy(self.colPole)
        self.lblPoleThickness.setBuddy(self.spnPoleThickness)

        self.retranslateUi(CosmeticPropertiesWidget)
        QtCore.QMetaObject.connectSlotsByName(CosmeticPropertiesWidget)
        CosmeticPropertiesWidget.setTabOrder(self.spnCartWidth, self.spnCartHeight)
        CosmeticPropertiesWidget.setTabOrder(self.spnCartHeight, self.spnPoleThickness)

    def retranslateUi(self, CosmeticPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        CosmeticPropertiesWidget.setWindowTitle(_translate("CosmeticPropertiesWidget", "Form"))
        self.lblBackgroundColor.setText(_translate("CosmeticPropertiesWidget", "Background color:"))
        self.lblCartColor.setText(_translate("CosmeticPropertiesWidget", "Cart color:"))
        self.lblCartWidth.setText(_translate("CosmeticPropertiesWidget", "Cart width (m):"))
        self.lblCartHeight.setText(_translate("CosmeticPropertiesWidget", "Cart height(m):"))
        self.lblPoleColor.setText(_translate("CosmeticPropertiesWidget", "Pole color:"))
        self.lblPoleThickness.setText(_translate("CosmeticPropertiesWidget", "Pole thickness (m):"))

from src.widgets.color_picker_widget import ColorPickerWidget
