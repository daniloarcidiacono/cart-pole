# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cart_pole_graph_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CartPoleGraphWidget(object):
    def setupUi(self, CartPoleGraphWidget):
        CartPoleGraphWidget.setObjectName("CartPoleGraphWidget")
        CartPoleGraphWidget.resize(789, 474)
        self.verticalLayout = QtWidgets.QVBoxLayout(CartPoleGraphWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkPosition = QtWidgets.QCheckBox(CartPoleGraphWidget)
        self.chkPosition.setChecked(True)
        self.chkPosition.setObjectName("chkPosition")
        self.horizontalLayout.addWidget(self.chkPosition)
        self.chkVelocity = QtWidgets.QCheckBox(CartPoleGraphWidget)
        self.chkVelocity.setChecked(True)
        self.chkVelocity.setObjectName("chkVelocity")
        self.horizontalLayout.addWidget(self.chkVelocity)
        self.chkAngle = QtWidgets.QCheckBox(CartPoleGraphWidget)
        self.chkAngle.setChecked(True)
        self.chkAngle.setObjectName("chkAngle")
        self.horizontalLayout.addWidget(self.chkAngle)
        self.chkAngleVelocity = QtWidgets.QCheckBox(CartPoleGraphWidget)
        self.chkAngleVelocity.setChecked(True)
        self.chkAngleVelocity.setObjectName("chkAngleVelocity")
        self.horizontalLayout.addWidget(self.chkAngleVelocity)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plotWidget = PlotWidget(CartPoleGraphWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout.addWidget(self.plotWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblTimeSpan = QtWidgets.QLabel(CartPoleGraphWidget)
        self.lblTimeSpan.setObjectName("lblTimeSpan")
        self.horizontalLayout_2.addWidget(self.lblTimeSpan)
        self.spnTimeSpan = QtWidgets.QSpinBox(CartPoleGraphWidget)
        self.spnTimeSpan.setMaximum(120)
        self.spnTimeSpan.setObjectName("spnTimeSpan")
        self.horizontalLayout_2.addWidget(self.spnTimeSpan)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CartPoleGraphWidget)
        QtCore.QMetaObject.connectSlotsByName(CartPoleGraphWidget)

    def retranslateUi(self, CartPoleGraphWidget):
        _translate = QtCore.QCoreApplication.translate
        CartPoleGraphWidget.setWindowTitle(_translate("CartPoleGraphWidget", "Cart pole plots"))
        self.chkPosition.setText(_translate("CartPoleGraphWidget", "Position"))
        self.chkVelocity.setText(_translate("CartPoleGraphWidget", "Velocity"))
        self.chkAngle.setText(_translate("CartPoleGraphWidget", "Angle"))
        self.chkAngleVelocity.setText(_translate("CartPoleGraphWidget", "Angle velocity"))
        self.lblTimeSpan.setText(_translate("CartPoleGraphWidget", "Time span (s):"))

from pyplots.plot_widget import PlotWidget
