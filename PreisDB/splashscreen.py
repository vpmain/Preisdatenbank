# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreisDB\splashscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 30px\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.splashTitlePic = QtWidgets.QLabel(self.dropShadowFrame)
        self.splashTitlePic.setGeometry(QtCore.QRect(16, 16, 341, 251))
        self.splashTitlePic.setText("")
        self.splashTitlePic.setPixmap(QtGui.QPixmap("../pic/Klammer.png"))
        self.splashTitlePic.setScaledContents(True)
        self.splashTitlePic.setObjectName("splashTitlePic")
        self.splashProgressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.splashProgressBar.setGeometry(QtCore.QRect(20, 290, 621, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.splashProgressBar.setFont(font)
        self.splashProgressBar.setStyleSheet("QProgressBar{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(230, 234, 236);\n"
"    border-style: none;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 5px;\n"
"    background-color: rgb(115, 127, 133);\n"
"}")
        self.splashProgressBar.setProperty("value", 21)
        self.splashProgressBar.setObjectName("splashProgressBar")
        self.label = QtWidgets.QLabel(self.dropShadowFrame)
        self.label.setGeometry(QtCore.QRect(-10, 320, 681, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_2.setGeometry(QtCore.QRect(69, 355, 571, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_3.setGeometry(QtCore.QRect(220, 130, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.splashText = QtWidgets.QLabel(self.dropShadowFrame)
        self.splashText.setGeometry(QtCore.QRect(220, 180, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.splashText.setFont(font)
        self.splashText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.splashText.setObjectName("splashText")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label.setText(_translate("SplashScreen", "loading..."))
        self.label_2.setText(_translate("SplashScreen", "<strong>Created by:</strong> Bernhard Edinger"))
        self.label_3.setText(_translate("SplashScreen", "Preisdatenbank"))
        self.splashText.setText(_translate("SplashScreen", "Preisdatenbank"))
