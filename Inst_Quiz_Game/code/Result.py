# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultwin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import os
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#from Warning import Ui_warningwin
import pandas as pd

class Ui_resultwin(object):
    def setupUi(self, resultwin, homewin, hw_ui, user):
        self.hw = homewin
        self.resultwin = resultwin
        self.hw_ui = hw_ui
        self.user = user
        self.user.if_minus_set_zero()
        self.info_file = './resources/user_info.pickle'
        #self.info_list = list()
        self.new_df = pd.DataFrame(data=[[self.user.score, self.user.major, self.user.name]], index=[self.user.id], columns=['score', 'major', 'name'])
        #self.new_df = pd.DataFrame(data=[[20,222, 1, 1],[77,444,2,2]], index=['row1','row2'], columns=['점수','학번','순위','이름'])
        self.df = None
        self.cnt = 1
        
        resultwin.setObjectName("resultwin")
        resultwin.resize(1333, 937)
        resultwin.setStyleSheet("background-color: rgb(37, 37, 38);")
        self.gridLayout_3 = QtWidgets.QGridLayout(resultwin)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.ALL_RANK = QtWidgets.QLabel(resultwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        self.ALL_RANK.setFont(font)
        self.ALL_RANK.setStyleSheet("color:white;")
        self.ALL_RANK.setAlignment(QtCore.Qt.AlignCenter)
        self.ALL_RANK.setIndent(50)
        self.ALL_RANK.setObjectName("ALL_RANK")
        self.horizontalLayout_4.addWidget(self.ALL_RANK)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 8)
        self.horizontalLayout_4.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(resultwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        #self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        '''
        for i, label in enumerate(["순위", "점수", "학과", "이름"]):
            item = QTableWidgetItem(label)
            item.setForeground(QtGui.QColor(255, 255, 255))
            item.setBackground(QtGui.QColor(51, 51, 55))
            self.tableWidget.setHorizontalHeaderItem(i, item)
        '''
        self.tableWidget.setHorizontalHeaderLabels(["순위", "점수", "학과", "이름"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        #self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(42)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 14)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 14)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 6, 0, 1, 1)
        self.celebrate_label = QtWidgets.QLabel(resultwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.celebrate_label.setFont(font)
        self.celebrate_label.setStyleSheet("color:white;")
        self.celebrate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.celebrate_label.setObjectName("celebrate_label")
        self.gridLayout.addWidget(self.celebrate_label, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(resultwin)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.horizontalLayout_3.setStretch(0, 4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(resultwin)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(resultwin)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.RANK = QtWidgets.QLabel(resultwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.RANK.setFont(font)
        self.RANK.setStyleSheet("color:white;")
        self.RANK.setAlignment(QtCore.Qt.AlignCenter)
        self.RANK.setObjectName("RANK")
        self.horizontalLayout_2.addWidget(self.RANK)
        self.rank_label = QtWidgets.QLabel(resultwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.rank_label.setFont(font)
        self.rank_label.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.rank_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rank_label.setObjectName("rank_label")
        self.horizontalLayout_2.addWidget(self.rank_label)
        self.label_9 = QtWidgets.QLabel(resultwin)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 4)
        self.horizontalLayout_2.setStretch(3, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(resultwin)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.SCORE = QtWidgets.QLabel(resultwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.SCORE.setFont(font)
        self.SCORE.setStyleSheet("color:white;")
        self.SCORE.setAlignment(QtCore.Qt.AlignCenter)
        self.SCORE.setObjectName("SCORE")
        self.horizontalLayout.addWidget(self.SCORE)
        self.score_label = QtWidgets.QLabel(resultwin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.score_label.setFont(font)
        self.score_label.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.score_label.setObjectName("score_label")
        self.horizontalLayout.addWidget(self.score_label)
        self.label_4 = QtWidgets.QLabel(resultwin)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 4)
        self.horizontalLayout.setStretch(3, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.home_btn = QtWidgets.QPushButton(resultwin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.home_btn.setObjectName("home_btn")
        self.horizontalLayout_5.addWidget(self.home_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_5.setStretch(0, 14)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 7, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(6, 9)
        self.gridLayout.setRowStretch(7, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        #self.save_result()
        #self.load_pickle()
        self.save_result()
        self.tableWidget.setRowCount(len(self.df))
        
        for i in range(len(self.df)):
            for j in range(4):
                # 순위, 점수, 학과, 이름
                if j == 0:
                    rank = QTableWidgetItem(str(int(self.df['rank'].values[i])))
                    #rank.setForeground(QtGui.QColor(255, 255, 255))
                    rank.setBackground(QtGui.QColor(255, 255, 255))
                    rank.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, rank)
                elif j == 1:
                    score = QTableWidgetItem(str(self.df['score'].values[i]))
                    score.setBackground(QtGui.QColor(255, 255, 255))
                    score.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, score)
                elif j == 2:
                    major = QTableWidgetItem(self.df['major'].values[i])
                    major.setBackground(QtGui.QColor(255, 255, 255))
                    major.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, major)
                elif j == 3:
                    name = self.df['name'].values[i]
                    encoded_name = QTableWidgetItem(name[0] + '*' * len(name[1:]))
                    encoded_name.setBackground(QtGui.QColor(255, 255, 255))
                    encoded_name.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(i, j, encoded_name)
                    
        
        #버튼
        self.home_btn.clicked.connect(self.return_to_home)
        
        self.retranslateUi(resultwin)
        QtCore.QMetaObject.connectSlotsByName(resultwin)

    def retranslateUi(self, resultwin):
        _translate = QtCore.QCoreApplication.translate
        resultwin.setWindowTitle(_translate("resultwin", "Form"))
        self.ALL_RANK.setText(_translate("resultwin", "<전체 순위>"))
        self.celebrate_label.setText(_translate("resultwin", f"{self.user.name} 님 축하합니다!"))
        self.RANK.setText(_translate("resultwin", "순위"))
        self.rank_label.setText(_translate("resultwin", f"{int(self.df.loc[self.user.id, 'rank'])}위"))
        self.SCORE.setText(_translate("resultwin", "총점"))
        self.score_label.setText(_translate("resultwin", f"{self.user.score}점"))
        self.home_btn.setText(_translate("resultwin", "\U0001F3E0 HOME"))
        
    def return_to_home(self):
        self.hw_ui.show_top_rank()
        #self.hw.show()
        self.hw.showFullScreen()
        self.resultwin.hide()
    
    def load_pickle(self):
        if not os.path.isfile(self.info_file):
            with open(self.info_file,'wb') as file:
                pickle.dump("some obejct", file)
            return False, False
        with open(self.info_file, 'rb') as f:
            info = pickle.load(f)
        
        return info, True
        
    def dump_pickle(self):
        with open(self.info_file, 'wb') as f:
            pickle.dump(self.df, f)
    
    def sort_rank(self):
        self.df['rank'] = self.df['score'].rank(method='dense', ascending=False)
        if len(self.df) > 1:
            self.df = self.df.sort_values(by=['rank'])
        
    def save_result(self):
        #info = load_pickle()
        self.df, is_exist = self.load_pickle()
        #df = pd.DataFrame(data=[[1,2],[3,4]], index=['row1','row2'], columns=['col1','col3'])
        #df2 = pd.DataFrame(data=[[5,6]],index=['row3'],columns=['col1','col3'])
        if is_exist:
            self.df = pd.concat([self.df, self.new_df])  
        else: 
            self.df = self.new_df
        self.sort_rank()
        #print(self.df)
        self.dump_pickle()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    resultwin = QtWidgets.QWidget()
    ui = Ui_resultwin()
    ui.setupUi(resultwin)
    resultwin.show()
    sys.exit(app.exec_())

