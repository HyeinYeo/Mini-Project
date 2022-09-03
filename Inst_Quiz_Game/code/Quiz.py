# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from User import User
from Result import *
import pandas as pd
import pygame
G, Q, A, C = 0, 1, 2, 3


class Ui_queswin(object): 
        
    def setupUi(self, queswin, homewin, hw_ui, user):
        self.hw = homewin
        self.qw = queswin
        self.hw_ui = hw_ui
        
        self.user = user
        self.questions = list()
        df = pd.read_excel('./resources/quiz2.xlsx')
        for g in df['group'].unique():
            temp_df = df.query('group==@g').sample(n=2) ## 그룹별 데이터 추출 및 2개 비복원 추출
            subset = temp_df[['group', 'audio_file', 'answer', 'choice']]
            temp = [tuple(x) for x in subset.values]
            tuples = [(elem[G], elem[Q], elem[A].strip('"'), elem[C]) for elem in temp]
            self.questions.extend(tuples)
        self.bound = 4
        self.count = 0
        self.ques_msg = {'E': "악기를 고르세요(정답 1개)", 'M':"악기를 고르세요(정답 2개)", 'H':'악기를 고르세요(정답 3개)'}
        self.curr_qna = self.questions[self.count]
        self.sound = pygame.mixer
        self.bar_figure = 0
        
        
        queswin.setObjectName("queswin")
        queswin.resize(1313, 983)
        queswin.setStyleSheet("background-color: rgb(37, 37, 38);")
        self.gridLayout_2 = QtWidgets.QGridLayout(queswin)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(queswin)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkbox4 = QtWidgets.QCheckBox(queswin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox4.sizePolicy().hasHeightForWidth())
        self.checkbox4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.checkbox4.setFont(font)
        self.checkbox4.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"QCheckBox {\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.checkbox4.setObjectName("checkbox4")
        self.gridLayout_3.addWidget(self.checkbox4, 3, 2, 1, 1)
        self.checkbox2 = QtWidgets.QCheckBox(queswin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox2.sizePolicy().hasHeightForWidth())
        self.checkbox2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.checkbox2.setFont(font)
        self.checkbox2.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"QCheckBox {\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.checkbox2.setObjectName("checkbox2")
        self.gridLayout_3.addWidget(self.checkbox2, 1, 2, 1, 1)
        self.checkbox1 = QtWidgets.QCheckBox(queswin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox1.sizePolicy().hasHeightForWidth())
        self.checkbox1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.checkbox1.setFont(font)
        self.checkbox1.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"QCheckBox {\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.checkbox1.setObjectName("checkbox1")
        self.gridLayout_3.addWidget(self.checkbox1, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.B_indicator = QtWidgets.QLabel(queswin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        self.B_indicator.setFont(font)
        self.B_indicator.setText("")
        self.B_indicator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.B_indicator.setObjectName("B_indicator")
        self.gridLayout_3.addWidget(self.B_indicator, 1, 1, 1, 1)
        self.A_indicator = QtWidgets.QLabel(queswin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        self.A_indicator.setFont(font)
        self.A_indicator.setText("")
        self.A_indicator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.A_indicator.setObjectName("A_indicator")
        self.gridLayout_3.addWidget(self.A_indicator, 0, 1, 1, 1)
        self.D_indicator = QtWidgets.QLabel(queswin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        self.D_indicator.setFont(font)
        self.D_indicator.setText("")
        self.D_indicator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.D_indicator.setObjectName("D_indicator")
        self.gridLayout_3.addWidget(self.D_indicator, 3, 1, 1, 1)
        self.checkbox5 = QtWidgets.QCheckBox(queswin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox5.sizePolicy().hasHeightForWidth())
        self.checkbox5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.checkbox5.setFont(font)
        self.checkbox5.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"QCheckBox {\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.checkbox5.setObjectName("checkbox5")
        self.gridLayout_3.addWidget(self.checkbox5, 4, 2, 1, 1)
        self.E_indicator = QtWidgets.QLabel(queswin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        self.E_indicator.setFont(font)
        self.E_indicator.setText("")
        self.E_indicator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.E_indicator.setObjectName("E_indicator")
        self.gridLayout_3.addWidget(self.E_indicator, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 3, 0, 1, 1)
        self.C_indicator = QtWidgets.QLabel(queswin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(14)
        self.C_indicator.setFont(font)
        self.C_indicator.setText("")
        self.C_indicator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.C_indicator.setObjectName("C_indicator")
        self.gridLayout_3.addWidget(self.C_indicator, 2, 1, 1, 1)
        self.checkbox3 = QtWidgets.QCheckBox(queswin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox3.sizePolicy().hasHeightForWidth())
        self.checkbox3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Medium")
        font.setPointSize(16)
        self.checkbox3.setFont(font)
        self.checkbox3.setStyleSheet("QCheckBox::indicator {\n"
"    width: 40px;\n"
"    height: 40px;\n"
"}\n"
"QCheckBox {\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.checkbox3.setObjectName("checkbox3")
        self.gridLayout_3.addWidget(self.checkbox3, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 3, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 4, 3, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 11)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(queswin)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.next_btn = QtWidgets.QPushButton(queswin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet("background-color: rgb(51, 51, 55);\n"
"border:1px solid rgb(67, 67, 70);\n"
"color:white;")
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout_3.addWidget(self.next_btn)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.horizontalLayout_3.setStretch(0, 13)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(queswin)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(queswin)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.progressBar = QtWidgets.QProgressBar(queswin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Bold")
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(98, 114, 164);\n"
"color:rgb(200,200,200);\n"
"border-style: none;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", self.bar_figure)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 13)
        self.horizontalLayout_2.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.question_label = QtWidgets.QLabel(queswin)
        font = QtGui.QFont()
        font.setFamily("KoPubWorld돋움체_Pro Bold")
        font.setPointSize(20)
        self.question_label.setFont(font)
        self.question_label.setStyleSheet("color:white;\n"
"")
        self.question_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.question_label.setIndent(0)
        self.question_label.setObjectName("question_label")
        self.horizontalLayout_4.addWidget(self.question_label)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 13)
        self.horizontalLayout_4.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 8)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 1)
        self.gridLayout.setRowStretch(8, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        
        # 초기
        self.play_sound(self.curr_qna[Q])
        # 버튼
        self.next_btn.clicked.connect(self.click_next_btn)
        
        self.retranslateUi(queswin)
        QtCore.QMetaObject.connectSlotsByName(queswin)

    def retranslateUi(self, queswin):
        _translate = QtCore.QCoreApplication.translate
        queswin.setWindowTitle(_translate("queswin", "Form"))
        choice = self.curr_qna[C].split()
        self.checkbox1.setText(_translate("queswin", f"{choice[0]}"))
        self.checkbox2.setText(_translate("queswin", f"{choice[1]}"))
        self.checkbox3.setText(_translate("queswin", f"{choice[2]}"))
        self.checkbox4.setText(_translate("queswin", f"{choice[3]}"))
        self.checkbox5.setText(_translate("queswin", f"{choice[4]}"))
        self.next_btn.setText(_translate("queswin", "SUBMIT"))
        self.question_label.setText(_translate("queswin", f"{self.count + 1}. {self.ques_msg[self.curr_qna[G]]}"))
        self.indicators = [self.A_indicator, self.B_indicator, self.C_indicator, self.D_indicator, self.E_indicator]
    
    def countup(self):
        self.count += 1
    
    def click_next_btn(self):
        self.stop_sound()
        if self.next_btn.text() == "SUBMIT":
            #print('SUBMIT')
            self.check_answer()
            self.set_uncheckable()
            self.next_btn.setText("NEXT")
            self.bar_figure += 20
            self.progressBar.setValue(self.bar_figure)
            
        elif self.next_btn.text() == "NEXT":
            if self.count < self.bound:
                #print("NEXT")
                self.set_uncheck()
                self.set_chackable()
                self.reset_pixmap()
                self.countup()
                self.curr_qna = self.questions[self.count]
                self.question_label.setText(f"{self.count + 1}. {self.ques_msg[self.curr_qna[G]]}")
                choice = self.curr_qna[C].split()
                self.checkbox1.setText(f"{choice[0]}")
                self.checkbox2.setText(f"{choice[1]}")
                self.checkbox3.setText(f"{choice[2]}")
                self.checkbox4.setText(f"{choice[3]}")
                self.checkbox5.setText(f"{choice[4]}")
            
                self.next_btn.setText("SUBMIT")
                self.play_sound(self.curr_qna[Q])
            else:
                self.resultwin = QtWidgets.QWidget()
                self.ui = Ui_resultwin()
                self.ui.setupUi(self.resultwin, self.hw, self.hw_ui, self.user)
                self.qw.hide()
                #self.resultwin.show()
                self.resultwin.showFullScreen()
            
            
            
    def play_sound(self, file):
        #print(file)
        path = "./resources/audio/" + file + ".mp3"
        self.sound.init()
        self.sound.music.load(path)
        self.sound.music.play(0)
        
    def stop_sound(self):
        self.sound.music.stop()
            
    def check_answer(self):
        #print(self.curr_qna[A])
        answer = [int(num) for num in list(str(self.curr_qna[A]))]
        #print(answer)
        check_states = list()
        check_states.append(self.checkbox1.isChecked())
        check_states.append(self.checkbox2.isChecked())
        check_states.append(self.checkbox3.isChecked())
        check_states.append(self.checkbox4.isChecked())
        check_states.append(self.checkbox5.isChecked())
        
        for is_correct, is_check, indicator in zip(answer, check_states, self.indicators):
            if is_correct: # 정답 선지
                if is_correct == is_check: #정답 맞혔을 때
                    self.qPixmapFileVar = QtGui.QPixmap()
                    self.qPixmapFileVar.load("./resources/images/correct.png")
                    self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(40)
                    indicator.setPixmap(self.qPixmapFileVar)
                    ## 점수 증가
                    self.user.add_score(10)
                    
                else: #정답 체크 안 해서 틀렸을 때
                    self.qPixmapFileVar = QtGui.QPixmap()
                    self.qPixmapFileVar.load("./resources/images/correct.png")
                    self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(40)
                    indicator.setPixmap(self.qPixmapFileVar)
            else: # 오답 선지
                if is_correct != is_check: # 오답 골랐을 때
                    self.qPixmapFileVar = QtGui.QPixmap()
                    self.qPixmapFileVar.load("./resources/images/wrong.png")
                    self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(40)
                    indicator.setPixmap(self.qPixmapFileVar)
                    self.user.sub_score(1)
                else:
                    pass
        
    def set_chackable(self):
        self.checkbox1.setEnabled(True)
        self.checkbox2.setEnabled(True)
        self.checkbox3.setEnabled(True)
        self.checkbox4.setEnabled(True)
        self.checkbox5.setEnabled(True)
        
    def set_uncheckable(self):
        self.checkbox1.setEnabled(False)
        self.checkbox2.setEnabled(False)
        self.checkbox3.setEnabled(False)
        self.checkbox4.setEnabled(False)
        self.checkbox5.setEnabled(False)
        
    def set_uncheck(self):
        self.checkbox1.setCheckState(False)
        self.checkbox2.setCheckState(False)
        self.checkbox3.setCheckState(False)
        self.checkbox4.setCheckState(False)
        self.checkbox5.setCheckState(False)
    
    def reset_pixmap(self):
        for indicator in self.indicators:
            indicator.setText(" ")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    queswin = QtWidgets.QWidget()
    ui = Ui_queswin()
    ui.setupUi(queswin)
    queswin.show()
    sys.exit(app.exec_())

