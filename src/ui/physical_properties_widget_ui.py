# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/physical_properties_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhysicalPropertiesWidget(object):
    def setupUi(self, PhysicalPropertiesWidget):
        PhysicalPropertiesWidget.setObjectName("PhysicalPropertiesWidget")
        PhysicalPropertiesWidget.resize(374, 204)
        self.formLayout = QtWidgets.QFormLayout(PhysicalPropertiesWidget)
        self.formLayout.setObjectName("formLayout")
        self.lblGravity = QtWidgets.QLabel(PhysicalPropertiesWidget)
        self.lblGravity.setObjectName("lblGravity")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblGravity)
        self.spnGravity = QtWidgets.QDoubleSpinBox(PhysicalPropertiesWidget)
        self.spnGravity.setObjectName("spnGravity")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spnGravity)
        self.lblCartMass = QtWidgets.QLabel(PhysicalPropertiesWidget)
        self.lblCartMass.setObjectName("lblCartMass")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCartMass)
        self.spnCartMass = QtWidgets.QDoubleSpinBox(PhysicalPropertiesWidget)
        self.spnCartMass.setObjectName("spnCartMass")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spnCartMass)
        self.lblPoleMass = QtWidgets.QLabel(PhysicalPropertiesWidget)
        self.lblPoleMass.setObjectName("lblPoleMass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblPoleMass)
        self.spnPoleMass = QtWidgets.QDoubleSpinBox(PhysicalPropertiesWidget)
        self.spnPoleMass.setObjectName("spnPoleMass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spnPoleMass)
        self.lblPoleLength = QtWidgets.QLabel(PhysicalPropertiesWidget)
        self.lblPoleLength.setObjectName("lblPoleLength")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblPoleLength)
        self.spnPoleLength = QtWidgets.QDoubleSpinBox(PhysicalPropertiesWidget)
        self.spnPoleLength.setObjectName("spnPoleLength")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spnPoleLength)
        self.lblCartFriction = QtWidgets.QLabel(PhysicalPropertiesWidget)
        self.lblCartFriction.setObjectName("lblCartFriction")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblCartFriction)
        self.spnCartFriction = QtWidgets.QDoubleSpinBox(PhysicalPropertiesWidget)
        self.spnCartFriction.setObjectName("spnCartFriction")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spnCartFriction)
        self.lblPoleFriction = QtWidgets.QLabel(PhysicalPropertiesWidget)
        self.lblPoleFriction.setObjectName("lblPoleFriction")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblPoleFriction)
        self.spnPoleFriction = QtWidgets.QDoubleSpinBox(PhysicalPropertiesWidget)
        self.spnPoleFriction.setObjectName("spnPoleFriction")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spnPoleFriction)
        self.lblGravity.setBuddy(self.spnGravity)
        self.lblCartMass.setBuddy(self.spnCartMass)
        self.lblPoleMass.setBuddy(self.spnPoleMass)
        self.lblPoleLength.setBuddy(self.spnPoleLength)
        self.lblCartFriction.setBuddy(self.spnCartFriction)
        self.lblPoleFriction.setBuddy(self.spnPoleFriction)

        self.retranslateUi(PhysicalPropertiesWidget)
        QtCore.QMetaObject.connectSlotsByName(PhysicalPropertiesWidget)

    def retranslateUi(self, PhysicalPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        PhysicalPropertiesWidget.setWindowTitle(_translate("PhysicalPropertiesWidget", "Form"))
        self.lblGravity.setText(_translate("PhysicalPropertiesWidget", "Gravity (m/s^2):"))
        self.lblCartMass.setText(_translate("PhysicalPropertiesWidget", "Cart mass (kg):"))
        self.lblPoleMass.setText(_translate("PhysicalPropertiesWidget", "Pole mass (kg):"))
        self.lblPoleLength.setText(_translate("PhysicalPropertiesWidget", "Pole length (m):"))
        self.lblCartFriction.setText(_translate("PhysicalPropertiesWidget", "Cart friction:"))
        self.lblPoleFriction.setText(_translate("PhysicalPropertiesWidget", "Pole friction:"))

