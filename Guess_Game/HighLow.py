# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuessGame.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    low_number = 1
    high_number = 10
    guess_left = 5
    hidden_number = random.randint(low_number, high_number)
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1348, 1095)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.round_label = QtWidgets.QLabel(self.centralwidget)
        self.round_label.setGeometry(QtCore.QRect(280, 130, 161, 51))
        self.round_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_label.setObjectName("round_label")
        self.round_count_label = QtWidgets.QLabel(self.centralwidget)
        self.round_count_label.setGeometry(QtCore.QRect(330, 230, 64, 51))
        self.round_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_count_label.setObjectName("round_count_label")
        self.highscore_label = QtWidgets.QLabel(self.centralwidget)
        self.highscore_label.setGeometry(QtCore.QRect(790, 130, 251, 61))
        self.highscore_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highscore_label.setObjectName("highscore_label")
        self.highscore_count_label = QtWidgets.QLabel(self.centralwidget)
        self.highscore_count_label.setGeometry(QtCore.QRect(900, 230, 64, 51))
        self.highscore_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highscore_count_label.setObjectName("highscore_count_label")
        self.entry_box = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_box.setGeometry(QtCore.QRect(410, 560, 511, 71))
        self.entry_box.setObjectName("entry_box")
        self.guess_button = QtWidgets.QPushButton(self.centralwidget)
        self.guess_button.setGeometry(QtCore.QRect(410, 640, 171, 41))
        self.guess_button.setObjectName("guess_button")
        self.guess_info = QtWidgets.QLabel(self.centralwidget)
        self.guess_info.setGeometry(QtCore.QRect(290, 440, 761, 111))
        self.guess_info.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_info.setObjectName("guess_info")
        self.hint = QtWidgets.QLabel(self.centralwidget)
        self.hint.setGeometry(QtCore.QRect(310, 720, 761, 111))
        self.hint.setAlignment(QtCore.Qt.AlignCenter)
        self.hint.setObjectName("hint")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1348, 48))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # 버튼 -> 동작(추측 숫자 입력받는 함수)과 연결하기(set up 때)
        self.guess_button.clicked.connect(self.guess_number)
        # 버튼 클릭 -> 엔트리박스에 있는 텍스트 guess 변수에 저장 -> 콘솔창에 출력
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.round_label.setText(_translate("MainWindow", "Round"))
        self.round_count_label.setText(_translate("MainWindow", "1"))
        self.highscore_label.setText(_translate("MainWindow", "High Score"))
        self.highscore_count_label.setText(_translate("MainWindow", "1"))
        self.guess_button.setText(_translate("MainWindow", "Guess"))
        # 남은 추측 개수 수정
        self.guess_info.setText(_translate("MainWindow", f"Guess a number between {self.low_number} and {self.high_number}.\n"
f"{self.guess_left} Guesses Left"))
        # 힌트문자는 변경되어야 함
        self.hint.setText(_translate("MainWindow", ""))
    
    
    # 추측 숫자 입력하는 함수
    def guess_number(self):
        guess = self.entry_box.text() # guess는 str타입
        try:
            guess = int(guess)
            if guess == self.hidden_number:
                self.high_number *= 2
                new_round = int(self.round_count_label.text()) + 1 # 라운드 1 증가
                self.round_count_label.setText(str(new_round))  # 라운드 1 증가 -> 텍스트 출력
                self.guess_left = 5
                self.hidden_number = random.randint(self.low_number, self.high_number)
                self.guess_info.setText(f"Guess a number between {self.low_number} and {self.high_number}.\n{self.guess_left} Guesses Left")
                
                self.entry_box.setText("") # 맞추면 입력창 비우기
            #elif self.guess_left > 1:
                
                
        except ValueError:
            self.hint.setText("What?") # 숫자 말고 다른 거 입력했을 시에 hint창에 what? 출력
            
        print(guess)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

