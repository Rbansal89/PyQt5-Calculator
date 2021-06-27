# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_world.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hello_world_name = QtWidgets.QLabel(self.centralwidget)
        self.hello_world_name.setGeometry(QtCore.QRect(140, 190, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.hello_world_name.setFont(font)
        self.hello_world_name.setObjectName("hello_world_name")
        self.click_me = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: press_it())
        self.click_me.setGeometry(QtCore.QRect(130, 310, 271, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.click_me.setFont(font)
        self.click_me.setObjectName("click_me")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def press_it():
            self.hello_world_name.setText("Boom!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hello_world_name.setText(_translate("MainWindow", "Hello World!"))
        self.click_me.setText(_translate("MainWindow", "Click me!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
