# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys

class Ui_warningwin(object):
    def __init__(self, msg):
        #super().__init__()
        self.warning_msg = msg
        
        
    def setupUi(self, warningwin):
        warningwin.setObjectName("warningwin")
        warningwin.resize(539, 397)
        warningwin.setStyleSheet("background-color: rgb(37, 37, 38);")
        self.gridLayout_2 = QtWidgets.QGridLayout(warningwin)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.WARNING = QtWidgets.QLabel(warningwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        self.WARNING.setFont(font)
        self.WARNING.setStyleSheet("color:white;\n"
"")
        self.WARNING.setAlignment(QtCore.Qt.AlignCenter)
        self.WARNING.setObjectName("WARNING")
        self.gridLayout.addWidget(self.WARNING, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(warningwin)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(warningwin)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.warning_btn = QtWidgets.QPushButton(warningwin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warning_btn.sizePolicy().hasHeightForWidth())
        self.warning_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(10)
        self.warning_btn.setFont(font)
        self.warning_btn.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.warning_btn.setObjectName("warning_btn")
        self.horizontalLayout.addWidget(self.warning_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.warning_label = QtWidgets.QLabel(warningwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(11)
        self.warning_label.setFont(font)
        self.warning_label.setStyleSheet("color:white;")
        self.warning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_label.setObjectName("warning_label")
        self.gridLayout.addWidget(self.warning_label, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(warningwin)
        QtCore.QMetaObject.connectSlotsByName(warningwin)

    def retranslateUi(self, warningwin):
        _translate = QtCore.QCoreApplication.translate
        warningwin.setWindowTitle(_translate("warningwin", "Dialog"))
        self.WARNING.setText(_translate("warningwin", "Warning!"))
        self.warning_btn.setText(_translate("warningwin", "확인"))
        self.warning_label.setText(_translate("warningwin", f"{self.warning_msg}"))
        
        self.warning_btn.clicked.connect(warningwin.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    warningwin = QtWidgets.QDialog()
    ui = Ui_warningwin()
    ui.setupUi(warningwin)
    warningwin.show()
    sys.exit(app.exec_())

