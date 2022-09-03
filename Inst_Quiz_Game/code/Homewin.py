from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from User import User
from Warning import Ui_warningwin
from Quiz import *
import pandas as pd

class Ui_homewin(object):
    def setupUi(self, homewin):
        self.hw = homewin
        self.info_file = './resources/user_info.pickle'
        self.df = None
        
        homewin.setObjectName("homewin")
        homewin.resize(1653, 1012)
        homewin.setAutoFillBackground(False)
        homewin.setStyleSheet("background-color: rgb(37, 37, 38);")
        self.centralwidget = QtWidgets.QWidget(homewin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setObjectName("main_layout")
        self.quiz_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.quiz_title.setFont(font)
        self.quiz_title.setStyleSheet("color: white;")
        self.quiz_title.setAlignment(QtCore.Qt.AlignCenter)
        self.quiz_title.setObjectName("quiz_title")
        self.main_layout.addWidget(self.quiz_title, 2, 1, 1, 1)
        self.club_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Bold")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.club_name.setFont(font)
        self.club_name.setStyleSheet("color:white;")
        self.club_name.setAlignment(QtCore.Qt.AlignCenter)
        self.club_name.setObjectName("club_name")
        self.main_layout.addWidget(self.club_name, 0, 1, 1, 1)
        self.regi_layout = QtWidgets.QHBoxLayout()
        self.regi_layout.setObjectName("regi_layout")
        self.space_4 = QtWidgets.QLabel(self.centralwidget)
        self.space_4.setText("")
        self.space_4.setObjectName("space_4")
        self.regi_layout.addWidget(self.space_4)
        self.regi_layout_2 = QtWidgets.QGridLayout()
        self.regi_layout_2.setObjectName("regi_layout_2")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy)
        self.name_input.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.name_input.setObjectName("name_input")
        self.regi_layout_2.addWidget(self.name_input, 2, 2, 1, 1)
        self.major_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.major_box.sizePolicy().hasHeightForWidth())
        self.major_box.setSizePolicy(sizePolicy)
        self.major_box.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.major_box.setObjectName("major_box")
        #self.combobox.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        for i in range(40):
            self.major_box.addItem("")
        self.regi_layout_2.addWidget(self.major_box, 0, 2, 1, 1)
        self.STUID = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Light")
        font.setPointSize(14)
        self.STUID.setFont(font)
        self.STUID.setStyleSheet("color:white;")
        self.STUID.setAlignment(QtCore.Qt.AlignCenter)
        self.STUID.setObjectName("STUID")
        self.regi_layout_2.addWidget(self.STUID, 1, 0, 1, 2)
        self.NAME = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Light")
        font.setPointSize(14)
        self.NAME.setFont(font)
        self.NAME.setStyleSheet("color:white;")
        self.NAME.setAlignment(QtCore.Qt.AlignCenter)
        self.NAME.setObjectName("NAME")
        self.regi_layout_2.addWidget(self.NAME, 2, 0, 1, 2)
        self.MAJOR = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Light")
        font.setPointSize(14)
        self.MAJOR.setFont(font)
        self.MAJOR.setStyleSheet("color:white;")
        self.MAJOR.setAlignment(QtCore.Qt.AlignCenter)
        self.MAJOR.setObjectName("MAJOR")
        self.regi_layout_2.addWidget(self.MAJOR, 0, 0, 1, 2)
        self.stuid_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stuid_input.sizePolicy().hasHeightForWidth())
        self.stuid_input.setSizePolicy(sizePolicy)
        self.stuid_input.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.stuid_input.setObjectName("stuid_input")
        self.regi_layout_2.addWidget(self.stuid_input, 1, 2, 1, 1)
        self.regi_layout_2.setColumnStretch(0, 1)
        self.regi_layout_2.setColumnStretch(2, 3)
        self.regi_layout.addLayout(self.regi_layout_2)
        self.space_3 = QtWidgets.QLabel(self.centralwidget)
        self.space_3.setText("")
        self.space_3.setObjectName("space_3")
        self.regi_layout.addWidget(self.space_3)
        self.regi_layout.setStretch(0, 1)
        self.regi_layout.setStretch(1, 1)
        self.regi_layout.setStretch(2, 1)
        self.main_layout.addLayout(self.regi_layout, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.regi_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regi_btn.sizePolicy().hasHeightForWidth())
        self.regi_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.regi_btn.setFont(font)
        self.regi_btn.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.regi_btn.setObjectName("regi_btn")
        self.horizontalLayout_2.addWidget(self.regi_btn)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.main_layout.addLayout(self.horizontalLayout_2, 7, 1, 1, 1)
        self.rank_layout_2 = QtWidgets.QHBoxLayout()
        self.rank_layout_2.setContentsMargins(0, -1, -1, -1)
        self.rank_layout_2.setObjectName("rank_layout_2")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.rank_layout_2.addWidget(self.label_24)
        self.rank_table = QtWidgets.QGridLayout()
        self.rank_table.setContentsMargins(0, -1, -1, -1)
        self.rank_table.setObjectName("rank_table")
        self.major_1 = QtWidgets.QLabel(self.centralwidget)
        self.major_1.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.major_1.setAlignment(QtCore.Qt.AlignCenter)
        self.major_1.setObjectName("major_1")
        self.rank_table.addWidget(self.major_1, 1, 1, 1, 1)
        self.RANK1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RANK1.setFont(font)
        self.RANK1.setAutoFillBackground(False)
        self.RANK1.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.RANK1.setAlignment(QtCore.Qt.AlignCenter)
        self.RANK1.setObjectName("RANK1")
        self.rank_table.addWidget(self.RANK1, 1, 0, 1, 1)
        self.score_2 = QtWidgets.QLabel(self.centralwidget)
        self.score_2.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.score_2.setObjectName("score_2")
        self.rank_table.addWidget(self.score_2, 2, 3, 1, 1)
        self.major_3 = QtWidgets.QLabel(self.centralwidget)
        self.major_3.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.major_3.setAlignment(QtCore.Qt.AlignCenter)
        self.major_3.setObjectName("major_3")
        self.rank_table.addWidget(self.major_3, 3, 1, 1, 1)
        self.score_3 = QtWidgets.QLabel(self.centralwidget)
        self.score_3.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.score_3.setAlignment(QtCore.Qt.AlignCenter)
        self.score_3.setObjectName("score_3")
        self.rank_table.addWidget(self.score_3, 3, 3, 1, 1)
        self.RANK3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RANK3.setFont(font)
        self.RANK3.setAutoFillBackground(False)
        self.RANK3.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.RANK3.setAlignment(QtCore.Qt.AlignCenter)
        self.RANK3.setObjectName("RANK3")
        self.rank_table.addWidget(self.RANK3, 3, 0, 1, 1)
        self.name_1 = QtWidgets.QLabel(self.centralwidget)
        self.name_1.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_1.setObjectName("name_1")
        self.rank_table.addWidget(self.name_1, 1, 2, 1, 1)
        self.name_3 = QtWidgets.QLabel(self.centralwidget)
        self.name_3.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.name_3.setAlignment(QtCore.Qt.AlignCenter)
        self.name_3.setObjectName("name_3")
        self.rank_table.addWidget(self.name_3, 3, 2, 1, 1)
        self.major_col = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.major_col.setFont(font)
        self.major_col.setAutoFillBackground(False)
        self.major_col.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.major_col.setAlignment(QtCore.Qt.AlignCenter)
        self.major_col.setObjectName("major_col")
        self.rank_table.addWidget(self.major_col, 0, 1, 1, 1)
        self.major_2 = QtWidgets.QLabel(self.centralwidget)
        self.major_2.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.major_2.setAlignment(QtCore.Qt.AlignCenter)
        self.major_2.setObjectName("major_2")
        self.rank_table.addWidget(self.major_2, 2, 1, 1, 1)
        self.name_col = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.name_col.setFont(font)
        self.name_col.setAutoFillBackground(False)
        self.name_col.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.name_col.setAlignment(QtCore.Qt.AlignCenter)
        self.name_col.setObjectName("name_col")
        self.rank_table.addWidget(self.name_col, 0, 2, 1, 1)
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_2.setObjectName("name_2")
        self.rank_table.addWidget(self.name_2, 2, 2, 1, 1)
        self.score_1 = QtWidgets.QLabel(self.centralwidget)
        self.score_1.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.score_1.setObjectName("score_1")
        self.rank_table.addWidget(self.score_1, 1, 3, 1, 1)
        self.RANK2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RANK2.setFont(font)
        self.RANK2.setAutoFillBackground(False)
        self.RANK2.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.RANK2.setAlignment(QtCore.Qt.AlignCenter)
        self.RANK2.setObjectName("RANK2")
        self.rank_table.addWidget(self.RANK2, 2, 0, 1, 1)
        self.score_col = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.score_col.setFont(font)
        self.score_col.setAutoFillBackground(False)
        self.score_col.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.score_col.setAlignment(QtCore.Qt.AlignCenter)
        self.score_col.setObjectName("score_col")
        self.rank_table.addWidget(self.score_col, 0, 3, 1, 1)
        self.rank_col = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rank_col.setFont(font)
        self.rank_col.setAutoFillBackground(False)
        self.rank_col.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.rank_col.setAlignment(QtCore.Qt.AlignCenter)
        self.rank_col.setObjectName("rank_col")
        self.rank_table.addWidget(self.rank_col, 0, 0, 1, 1)
        self.rank_layout_2.addLayout(self.rank_table)
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.rank_layout_2.addWidget(self.label_41)
        self.rank_layout_2.setStretch(0, 1)
        self.rank_layout_2.setStretch(1, 2)
        self.rank_layout_2.setStretch(2, 1)
        self.main_layout.addLayout(self.rank_layout_2, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.main_layout.addWidget(self.label_23, 4, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.main_layout.addWidget(self.label_22, 6, 1, 1, 1)
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.setRowStretch(3, 2)
        self.main_layout.setRowStretch(4, 1)
        self.main_layout.setRowStretch(5, 1)
        self.gridLayout.addLayout(self.main_layout, 1, 0, 1, 1)
        
        
        self.btn_layout = QtWidgets.QHBoxLayout()
        self.btn_layout.setObjectName("btn_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_layout.addItem(spacerItem)
        self.mini_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mini_btn.setFont(font)
        self.mini_btn.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color: white;")
        self.mini_btn.setObjectName("mini_btn")
        self.btn_layout.addWidget(self.mini_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_layout.addItem(spacerItem1)
        self.max_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.max_btn.setFont(font)
        self.max_btn.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color: white;")
        self.max_btn.setObjectName("max_btn")
        self.btn_layout.addWidget(self.max_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn_layout.addItem(spacerItem2)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color: white;")
        self.exit_btn.setObjectName("exit_btn")
        self.btn_layout.addWidget(self.exit_btn)
        self.btn_layout.setStretch(0, 25)
        self.btn_layout.setStretch(1, 1)
        self.btn_layout.setStretch(2, 1)
        self.btn_layout.setStretch(3, 1)
        self.btn_layout.setStretch(4, 1)
        self.btn_layout.setStretch(5, 1)
        self.gridLayout.addLayout(self.btn_layout, 0, 0, 1, 1)
        
        
        
        homewin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homewin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1653, 26))
        self.menubar.setObjectName("menubar")
        homewin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homewin)
        self.statusbar.setObjectName("statusbar")
        homewin.setStatusBar(self.statusbar)
        
        
        # regi 버튼 클릭 시
        self.regi_btn.clicked.connect(self.is_valid)
        
        self.mini_btn.clicked.connect(self.show_normal_screen)
        self.max_btn.clicked.connect(self.show_full_screen)
        self.exit_btn.clicked.connect(self.close_window)
        
        self.retranslateUi(homewin)
        if not self.show_top_rank():
            pass
        QtCore.QMetaObject.connectSlotsByName(homewin)
        


    def retranslateUi(self, homewin):
        _translate = QtCore.QCoreApplication.translate
        homewin.setWindowTitle(_translate("homewin", "MainWindow"))
        self.quiz_title.setText(_translate("homewin", "TOP 3"))
        self.club_name.setText(_translate("homewin", "국악기 맞히기 퀴즈"))
        major_file_path = './resources/major.txt'
        list_of_major = self.load_file(major_file_path)
        for i, major in enumerate(list_of_major):
            self.major_box.setItemText(i, _translate("homewin", f"{major}"))
            
        #self.major_box.setItemText(0, _translate("homewin", "ELLT"))
        self.STUID.setText(_translate("homewin", "학번"))
        self.NAME.setText(_translate("homewin", "이름"))
        self.MAJOR.setText(_translate("homewin", "학과"))
        self.regi_btn.setText(_translate("homewin", "REGISTER"))
        self.major_1.setText(_translate("homewin", "-"))
        self.RANK1.setText(_translate("homewin", "1"))
        self.score_2.setText(_translate("homewin", "-"))
        self.major_3.setText(_translate("homewin", "-"))
        self.score_3.setText(_translate("homewin", "-"))
        self.RANK3.setText(_translate("homewin", "3"))
        self.name_1.setText(_translate("homewin", "-"))
        self.name_3.setText(_translate("homewin", "-"))
        self.major_col.setText(_translate("homewin", "학과"))
        self.major_2.setText(_translate("homewin", "-"))
        self.name_col.setText(_translate("homewin", "이름"))
        self.name_2.setText(_translate("homewin", "-"))
        self.score_1.setText(_translate("homewin", "-"))
        self.RANK2.setText(_translate("homewin", "2"))
        self.score_col.setText(_translate("homewin", "점수"))
        self.rank_col.setText(_translate("homewin", "순위"))
        self.mini_btn.setText(_translate("homewin", "-"))
        self.max_btn.setText(_translate("homewin", "□"))
        self.exit_btn.setText(_translate("homewin", "X"))
    
    def close_window(self):
        self.hw.close()
        
    def show_normal_screen(self):
        self.hw.showNormal()
    
    def show_full_screen(self):
        self.hw.showFullScreen()
    
    def show_top_rank(self):
        df, is_exist = self.load_pickle()
        if not is_exist:
            return False
        
        rank, major, encoded_name, score = [], [], [], []
        if len(df) < 3:
            data = df
        else:
            data = df.head(3)
            
        for i in range(len(data)):
            rank.append(int(df['rank'].values[i]))
            major.append(df['major'].values[i])
            score.append(df['score'].values[i])
            raw_name = df['name'].values[i]
            name = raw_name[0] + '*' * len(raw_name[1:])
            encoded_name.append(name)
            
        #print(rank, major, encoded_name, score)
        
        if len(df) == 1:
            self.RANK1.setText(f"{rank[0]}")
            self.major_1.setText(f"{major[0]}")
            self.name_1.setText(f"{encoded_name[0]}")
            self.score_1.setText(f"{score[0]}")
        elif len(df) == 2:
            self.RANK1.setText(f"{rank[0]}")
            self.major_1.setText(f"{major[0]}")
            self.name_1.setText(f"{encoded_name[0]}")
            self.score_1.setText(f"{score[0]}")
            self.RANK2.setText(f"{rank[1]}")
            self.major_2.setText(f"{major[1]}")
            self.name_2.setText(f"{encoded_name[1]}")
            self.score_2.setText(f"{score[1]}")
        else:
            #print("3")
            self.RANK1.setText(f"{rank[0]}")
            self.major_1.setText(f"{major[0]}")
            self.name_1.setText(f"{encoded_name[0]}")
            self.score_1.setText(f"{score[0]}")
            self.RANK2.setText(f"{rank[1]}")
            self.major_2.setText(f"{major[1]}")
            self.name_2.setText(f"{encoded_name[1]}")
            self.score_2.setText(f"{score[1]}")
            self.RANK3.setText(f"{rank[2]}")
            self.major_3.setText(f"{major[2]}")
            self.name_3.setText(f"{encoded_name[2]}")
            self.score_3.setText(f"{score[2]}")
        
        return True
    
    
    
    def exec_question(self, user):
        self.queswin = QtWidgets.QWidget()
        self.quesui = Ui_queswin()
        self.quesui.setupUi(self.queswin, self.hw, self, user)
        self.hw.hide()
        #self.queswin.show()
        self.queswin.showFullScreen()
    
    
    def is_valid(self):
        if self.check_id() and self.check_name(): 
            major = self.major_box.currentText()
            user_id = int(self.stuid_input.text())
            name = self.name_input.text()
            #print(type(major), type(user_id), type(name))
            user = User(major, user_id, name)
            self.stuid_input.setText("")
            self.name_input.setText("")
            self.exec_question(user)
  
    def exec_warning(self, msg):
        self.warningwin = QtWidgets.QDialog()
        self.ui = Ui_warningwin(msg)
        self.ui.setupUi(self.warningwin)
        self.warningwin.show()
        
    def check_id(self):
        student_id = self.stuid_input.text().replace(" ", "")
            
        if len(student_id) == 0:
            msg = "학번을 입력해주세요"
            self.stuid_input.setText("")
            self.name_input.setText("")
            return self.exec_warning(msg)
        
        elif (not student_id.isdigit()) or (len(student_id) != 9):
            msg = "학번을 잘못 입력하셨습니다"
            self.stuid_input.setText("")
            self.name_input.setText("")
            return self.exec_warning(msg)
        
        elif self.check_duplication(int(student_id)):
            msg = "이미 등록된 학번입니다"
            self.stuid_input.setText("")
            self.name_input.setText("")
            return self.exec_warning(msg)
        return True
    
    def check_name(self):
        name = self.name_input.text().replace(" ", "")
        if len(name) == 0:
            msg = "이름을 입력해주세요"
            self.name_input.setText("")
            return self.exec_warning(msg)
        return True
            
        #print(type(student_id))    
    
    @staticmethod
    def load_file(path):
        if os.path.isfile(path):
            with open(path, 'rt', encoding='UTF8') as f:
                data = f.read().split('\n')
                print("file loaded")
            return data
                
            
    def load_pickle(self):
        if not os.path.isfile(self.info_file):
            return False, False
        with open(self.info_file, 'rb') as f:
            info = pickle.load(f)
        
        return info, True
    
    def get_id_list(self):
        df, is_exist = self.load_pickle()
        if not is_exist:
            return False
        return list(df.index)
    
    
    def check_duplication(self, student_id):
        id_list = self.get_id_list()
        if not id_list:
            return False
        if student_id in id_list:
            return True
        else:
            return False

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homewin = QtWidgets.QMainWindow()
    ui = Ui_homewin()
    ui.setupUi(homewin)
    #homewin.show()
    homewin.showFullScreen()
    sys.exit(app.exec_())
'''
