# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutDialog.resize(805, 513)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setMaximumSize(QtCore.QSize(805, 513))
        AboutDialog.setSizeGripEnabled(False)
        AboutDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, 18, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(64, 64))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/cart.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(32, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.lblAbout = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAbout.sizePolicy().hasHeightForWidth())
        self.lblAbout.setSizePolicy(sizePolicy)
        self.lblAbout.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblAbout.setTextFormat(QtCore.Qt.RichText)
        self.lblAbout.setScaledContents(False)
        self.lblAbout.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblAbout.setOpenExternalLinks(True)
        self.lblAbout.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lblAbout.setObjectName("lblAbout")
        self.horizontalLayout_2.addWidget(self.lblAbout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(AboutDialog)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(AboutDialog)
        self.pushButton.clicked.connect(AboutDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.lblAbout.setText(_translate("AboutDialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">About CartPole<br/></span>Cart pole simulator<br/><br/>by Danilo Arcidiacono</p><p><br/></p><p><span style=\" font-size:16pt; font-weight:600;\">MIT License </span></p><p>Copyright (c) 2018 Danilo Arcidiacono<br/></p><p>Permission is hereby granted, free of charge, to any person obtaining a copy of this software<br/>and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction,<br/>including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,<br/>and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do<br/>so, subject to the following conditions:</p><p>The above copyright notice and this permission notice shall be included in all copies or substantial<br/>portions of the Software.</p><p>THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,<br/>INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A<br/>PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR<br/>COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN<br/>AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION <br/>WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p></body></html>"))
        self.pushButton.setText(_translate("AboutDialog", "&OK"))

import resources_rc
