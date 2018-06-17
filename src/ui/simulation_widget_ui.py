# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/simulation_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimulationWidget(object):
    def setupUi(self, SimulationWidget):
        SimulationWidget.setObjectName("SimulationWidget")
        SimulationWidget.resize(400, 107)
        self.formLayout = QtWidgets.QFormLayout(SimulationWidget)
        self.formLayout.setObjectName("formLayout")
        self.lblIntegrator = QtWidgets.QLabel(SimulationWidget)
        self.lblIntegrator.setObjectName("lblIntegrator")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblIntegrator)
        self.cboIntegrator = QtWidgets.QComboBox(SimulationWidget)
        self.cboIntegrator.setObjectName("cboIntegrator")
        self.cboIntegrator.addItem("")
        self.cboIntegrator.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cboIntegrator)
        self.lblCartAgent = QtWidgets.QLabel(SimulationWidget)
        self.lblCartAgent.setObjectName("lblCartAgent")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCartAgent)
        self.cboCartAgent = QtWidgets.QComboBox(SimulationWidget)
        self.cboCartAgent.setObjectName("cboCartAgent")
        self.cboCartAgent.addItem("")
        self.cboCartAgent.addItem("")
        self.cboCartAgent.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cboCartAgent)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStartPause = QtWidgets.QPushButton(SimulationWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStartPause.setIcon(icon)
        self.btnStartPause.setIconSize(QtCore.QSize(16, 16))
        self.btnStartPause.setShortcut("")
        self.btnStartPause.setObjectName("btnStartPause")
        self.horizontalLayout.addWidget(self.btnStartPause)
        self.btnReset = QtWidgets.QPushButton(SimulationWidget)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout.addWidget(self.btnReset)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.lblIntegrator.setBuddy(self.cboIntegrator)

        self.retranslateUi(SimulationWidget)
        QtCore.QMetaObject.connectSlotsByName(SimulationWidget)

    def retranslateUi(self, SimulationWidget):
        _translate = QtCore.QCoreApplication.translate
        SimulationWidget.setWindowTitle(_translate("SimulationWidget", "Simulation"))
        self.lblIntegrator.setText(_translate("SimulationWidget", "Integrator:"))
        self.cboIntegrator.setItemText(0, _translate("SimulationWidget", "Runge-Kutta (4th order)"))
        self.cboIntegrator.setItemText(1, _translate("SimulationWidget", "Euler"))
        self.lblCartAgent.setText(_translate("SimulationWidget", "Cart agent: "))
        self.cboCartAgent.setItemText(0, _translate("SimulationWidget", "Heuristic"))
        self.cboCartAgent.setItemText(1, _translate("SimulationWidget", "Deep Q-learning"))
        self.cboCartAgent.setItemText(2, _translate("SimulationWidget", "User keyboard"))
        self.btnStartPause.setText(_translate("SimulationWidget", "Start"))
        self.btnReset.setText(_translate("SimulationWidget", "Reset"))

import resources_rc
