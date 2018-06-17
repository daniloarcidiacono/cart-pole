# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/starting_properties_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartingPropertiesWidget(object):
    def setupUi(self, StartingPropertiesWidget):
        StartingPropertiesWidget.setObjectName("StartingPropertiesWidget")
        StartingPropertiesWidget.resize(391, 140)
        self.formLayout = QtWidgets.QFormLayout(StartingPropertiesWidget)
        self.formLayout.setObjectName("formLayout")
        self.lblCartPosition = QtWidgets.QLabel(StartingPropertiesWidget)
        self.lblCartPosition.setObjectName("lblCartPosition")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblCartPosition)
        self.spnCartPosition = QtWidgets.QDoubleSpinBox(StartingPropertiesWidget)
        self.spnCartPosition.setMinimum(-99.99)
        self.spnCartPosition.setSingleStep(0.05)
        self.spnCartPosition.setObjectName("spnCartPosition")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spnCartPosition)
        self.lblCartVelocity = QtWidgets.QLabel(StartingPropertiesWidget)
        self.lblCartVelocity.setObjectName("lblCartVelocity")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCartVelocity)
        self.spnCartVelocity = QtWidgets.QDoubleSpinBox(StartingPropertiesWidget)
        self.spnCartVelocity.setMinimum(-99.99)
        self.spnCartVelocity.setSingleStep(0.05)
        self.spnCartVelocity.setObjectName("spnCartVelocity")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spnCartVelocity)
        self.lblPoleAngle = QtWidgets.QLabel(StartingPropertiesWidget)
        self.lblPoleAngle.setObjectName("lblPoleAngle")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblPoleAngle)
        self.spnPoleAngle = QtWidgets.QDoubleSpinBox(StartingPropertiesWidget)
        self.spnPoleAngle.setMaximum(359.0)
        self.spnPoleAngle.setObjectName("spnPoleAngle")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spnPoleAngle)
        self.spnPoleAngleVelocity = QtWidgets.QDoubleSpinBox(StartingPropertiesWidget)
        self.spnPoleAngleVelocity.setMinimum(-100.0)
        self.spnPoleAngleVelocity.setMaximum(100.0)
        self.spnPoleAngleVelocity.setObjectName("spnPoleAngleVelocity")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spnPoleAngleVelocity)
        self.lblPoleAngleVelocity = QtWidgets.QLabel(StartingPropertiesWidget)
        self.lblPoleAngleVelocity.setObjectName("lblPoleAngleVelocity")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblPoleAngleVelocity)
        self.lblCartPosition.setBuddy(self.spnCartPosition)
        self.lblCartVelocity.setBuddy(self.spnCartVelocity)
        self.lblPoleAngle.setBuddy(self.spnPoleAngle)
        self.lblPoleAngleVelocity.setBuddy(self.spnPoleAngleVelocity)

        self.retranslateUi(StartingPropertiesWidget)
        QtCore.QMetaObject.connectSlotsByName(StartingPropertiesWidget)

    def retranslateUi(self, StartingPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        StartingPropertiesWidget.setWindowTitle(_translate("StartingPropertiesWidget", "Initial conditions"))
        self.lblCartPosition.setText(_translate("StartingPropertiesWidget", "Cart position (m):"))
        self.lblCartVelocity.setText(_translate("StartingPropertiesWidget", "Cart velocity (m/s):"))
        self.lblPoleAngle.setText(_translate("StartingPropertiesWidget", "Pole angle (deg):"))
        self.lblPoleAngleVelocity.setText(_translate("StartingPropertiesWidget", "Pole angular velocity (deg/s):"))

