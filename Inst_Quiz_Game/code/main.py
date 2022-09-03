from Homewin import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homewin = QtWidgets.QMainWindow()
    ui = Ui_homewin()
    ui.setupUi(homewin)
    #homewin.show()
    homewin.showFullScreen()
    sys.exit(app.exec_())