# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreisDB\kennwertebau.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KennwerteBau(object):
    def setupUi(self, KennwerteBau):
        KennwerteBau.setObjectName("KennwerteBau")
        KennwerteBau.resize(997, 805)
        KennwerteBau.setMinimumSize(QtCore.QSize(997, 805))
        KennwerteBau.setStyleSheet("*{\n"
"    font-family:segoe ui;\n"
"    font-size:12px;\n"
"}\n"
"\n"
"QMainWindow::separator {\n"
"    background: yellow;\n"
"    width: 10px; /* when vertical */\n"
"    height: 10px; /* when horizontal */\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"    background: #d0d6da;\n"
"}\n"
"\n"
"QMenuBar{\n"
"    font-size:12px;\n"
"    background: #e7eaec;\n"
"}\n"
"\n"
"QMenu{\n"
"    font-size:12px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    font-size:12px;\n"
"    background:#b8c0c6;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    font-size:12px;\n"
"    background:#d0d6da;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font-size:12px;\n"
"    background:#a1abb1;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    padding-top: 1px;\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"QProgressBar{\n"
"    color: #000000;\n"
"    background-color: #d0d6da;\n"
"    border-style: none;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 5px;\n"
"    background-color: rgb(115, 127, 133);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    font-size:12px;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"    font-size:12px;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"    width: 20px;\n"
"    border-style: 0px solid;\n"
"    border-radius: 1px;\n"
"    background: #d0d6da;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"    width: 20px;\n"
"    border-style: solid;\n"
"    border-radius: 1px;\n"
"    background: #d0d6da;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow {\n"
"    image: url(\'//firma.local/dfs/Laufwerk-Z/Daten - Intern/Kosten/09 SQL Preisdatenbank/07_Python Oberfläche/qss/up-arrow.png\');\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow {\n"
"    image: url(\'//firma.local/dfs/Laufwerk-Z/Daten - Intern/Kosten/09 SQL Preisdatenbank/07_Python Oberfläche/qss/down-arrow.png\');\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QLabel#lblTitle {\n"
"    font-size:18px;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size:12px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"    font-size:12px;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background: #d0d6da;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: #e7eaec;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(\'//firma.local/dfs/Laufwerk-Z/Daten - Intern/Kosten/09 SQL Preisdatenbank/07_Python Oberfläche/qss/down-arrow.png\');\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView:enabled {\n"
"    color: #000000;\n"
"    background: #e7eaec;\n"
"    selection-color: #000000;\n"
"    selection-background-color: #d0d6da;\n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_navigationbar {\n"
"    color: #000000;\n"
"    background-color: #b8c0c6;\n"
"}\n"
"\n"
"\n"
"QTableView {\n"
"    font-size:12px;\n"
"    background: #ffffff;\n"
"    border-style: none;\n"
"    gridline-color: #737f86;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    color: #000000;\n"
"    background: #d0d6da;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #b8c0c6;\n"
"    padding: 2px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #737f86;\n"
"    border-right: 1px solid #737f86;    \n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #737f86;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #737f86;\n"
"    border-right: 1px solid #737f86;\n"
"}\n"
"\n"
"\n"
"QListView{\n"
"    font-size:12px;\n"
"    color: #000000;\n"
"    border: 0px solid;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QListView::item \n"
"{\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    border: 1px solid #d0d6da;\n"
"    border-radius: 2px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #d0d6da;\n"
"    border-radius: 2px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #d0d6da;\n"
"    border-radius: 2px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"\n"
"QListView::item:hover \n"
"{\n"
"    background-color: #d0d6da;\n"
"    margin: 0px;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*STYLESHEET FÜR QFrame*/\n"
"\n"
"QFrame#fraSideMenu, QFrame#fraTable, QFrame#fraTitle, QFrame#fraFooter {\n"
"    border-radius: 20px;\n"
"    background: #e7eaec;\n"
"}\n"
"\n"
"/*STYLESHEET FÜR QGridLayout*/\n"
"\n"
"QGridLayout {\n"
"    border-radius: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/*STYLESHEET FÜR QLabel*/\n"
"\n"
"QLabel {\n"
"    border-radius: 0px;\n"
"    background: #e7eaec;\n"
"}\n"
"\n"
"/*STYLESHEET FÜR QComboBox*/\n"
"\n"
"QComboBox {\n"
"    font-size:12px;\n"
"    border: solid;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: #ffffff;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: #ffffff;\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: #ffffff;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background: #d0d6da;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: #e7eaec;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down:on {\n"
"    background:#a1abb1;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(\'//firma.local/dfs/Laufwerk-Z/Daten - Intern/Kosten/09 SQL Preisdatenbank/07_Python Oberfläche/qss/down-arrow.png\');\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #d0d6da;\n"
"    border-radius: 0px;\n"
"    background: #ffffff;\n"
"    selection-color: #000000;\n"
"    selection-background-color: #d0d6da;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(KennwerteBau)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fraSideMenu = QtWidgets.QFrame(self.centralwidget)
        self.fraSideMenu.setMinimumSize(QtCore.QSize(330, 300))
        self.fraSideMenu.setMaximumSize(QtCore.QSize(330, 5000))
        self.fraSideMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraSideMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraSideMenu.setObjectName("fraSideMenu")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fraSideMenu)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblLabel4 = QtWidgets.QLabel(self.fraSideMenu)
        self.lblLabel4.setMinimumSize(QtCore.QSize(150, 20))
        self.lblLabel4.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel4.setFont(font)
        self.lblLabel4.setObjectName("lblLabel4")
        self.gridLayout_2.addWidget(self.lblLabel4, 4, 0, 1, 1)
        self.prgDatenImport = QtWidgets.QProgressBar(self.fraSideMenu)
        self.prgDatenImport.setMinimumSize(QtCore.QSize(200, 20))
        self.prgDatenImport.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.prgDatenImport.setFont(font)
        self.prgDatenImport.setMaximum(1000)
        self.prgDatenImport.setProperty("value", 0)
        self.prgDatenImport.setAlignment(QtCore.Qt.AlignCenter)
        self.prgDatenImport.setObjectName("prgDatenImport")
        self.gridLayout_2.addWidget(self.prgDatenImport, 8, 0, 1, 2)
        self.cmdStartQuery = QtWidgets.QPushButton(self.fraSideMenu)
        self.cmdStartQuery.setMinimumSize(QtCore.QSize(145, 25))
        self.cmdStartQuery.setMaximumSize(QtCore.QSize(145, 25))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.cmdStartQuery.setFont(font)
        self.cmdStartQuery.setStyleSheet("")
        self.cmdStartQuery.setObjectName("cmdStartQuery")
        self.gridLayout_2.addWidget(self.cmdStartQuery, 7, 1, 1, 1)
        self.lblLabel3 = QtWidgets.QLabel(self.fraSideMenu)
        self.lblLabel3.setMinimumSize(QtCore.QSize(0, 20))
        self.lblLabel3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel3.setFont(font)
        self.lblLabel3.setObjectName("lblLabel3")
        self.gridLayout_2.addWidget(self.lblLabel3, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.txtSearchProj = QtWidgets.QLineEdit(self.fraSideMenu)
        self.txtSearchProj.setMinimumSize(QtCore.QSize(150, 25))
        self.txtSearchProj.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.txtSearchProj.setFont(font)
        self.txtSearchProj.setObjectName("txtSearchProj")
        self.gridLayout_2.addWidget(self.txtSearchProj, 1, 0, 1, 2)
        self.cboKategorie = QtWidgets.QComboBox(self.fraSideMenu)
        self.cboKategorie.setMinimumSize(QtCore.QSize(111, 25))
        self.cboKategorie.setMaximumSize(QtCore.QSize(145, 25))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.cboKategorie.setFont(font)
        self.cboKategorie.setStyleSheet("")
        self.cboKategorie.setEditable(False)
        self.cboKategorie.setObjectName("cboKategorie")
        self.gridLayout_2.addWidget(self.cboKategorie, 5, 0, 1, 1)
        self.txtSearchGZ = QtWidgets.QLineEdit(self.fraSideMenu)
        self.txtSearchGZ.setMinimumSize(QtCore.QSize(145, 25))
        self.txtSearchGZ.setMaximumSize(QtCore.QSize(145, 25))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.txtSearchGZ.setFont(font)
        self.txtSearchGZ.setText("")
        self.txtSearchGZ.setObjectName("txtSearchGZ")
        self.gridLayout_2.addWidget(self.txtSearchGZ, 5, 1, 1, 1)
        self.lblLabel1 = QtWidgets.QLabel(self.fraSideMenu)
        self.lblLabel1.setMinimumSize(QtCore.QSize(300, 20))
        self.lblLabel1.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel1.setFont(font)
        self.lblLabel1.setToolTipDuration(0)
        self.lblLabel1.setObjectName("lblLabel1")
        self.gridLayout_2.addWidget(self.lblLabel1, 0, 0, 1, 2)
        self.cboKennwerte = QtWidgets.QComboBox(self.fraSideMenu)
        self.cboKennwerte.setMinimumSize(QtCore.QSize(111, 25))
        self.cboKennwerte.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.cboKennwerte.setFont(font)
        self.cboKennwerte.setStyleSheet("")
        self.cboKennwerte.setEditable(False)
        self.cboKennwerte.setObjectName("cboKennwerte")
        self.gridLayout_2.addWidget(self.cboKennwerte, 3, 0, 1, 2)
        self.lblLabel4_2 = QtWidgets.QLabel(self.fraSideMenu)
        self.lblLabel4_2.setMinimumSize(QtCore.QSize(150, 20))
        self.lblLabel4_2.setMaximumSize(QtCore.QSize(300, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel4_2.setFont(font)
        self.lblLabel4_2.setObjectName("lblLabel4_2")
        self.gridLayout_2.addWidget(self.lblLabel4_2, 2, 0, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.fraSideMenu, 1, 0, 1, 1)
        self.fraTable = QtWidgets.QFrame(self.centralwidget)
        self.fraTable.setMinimumSize(QtCore.QSize(400, 300))
        self.fraTable.setMaximumSize(QtCore.QSize(16777215, 5000))
        self.fraTable.setObjectName("fraTable")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.fraTable)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblLabel3_2 = QtWidgets.QLabel(self.fraTable)
        self.lblLabel3_2.setMinimumSize(QtCore.QSize(145, 20))
        self.lblLabel3_2.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel3_2.setFont(font)
        self.lblLabel3_2.setObjectName("lblLabel3_2")
        self.gridLayout_4.addWidget(self.lblLabel3_2, 1, 0, 1, 1)
        self.cmdDetail = QtWidgets.QPushButton(self.fraTable)
        self.cmdDetail.setMinimumSize(QtCore.QSize(145, 25))
        self.cmdDetail.setMaximumSize(QtCore.QSize(145, 25))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.cmdDetail.setFont(font)
        self.cmdDetail.setStyleSheet("")
        self.cmdDetail.setObjectName("cmdDetail")
        self.gridLayout_4.addWidget(self.cmdDetail, 3, 0, 1, 1)
        self.lblMedian = QtWidgets.QLabel(self.fraTable)
        self.lblMedian.setMinimumSize(QtCore.QSize(145, 20))
        self.lblMedian.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblMedian.setFont(font)
        self.lblMedian.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMedian.setObjectName("lblMedian")
        self.gridLayout_4.addWidget(self.lblMedian, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 4, 1, 1)
        self.lbl3Best = QtWidgets.QLabel(self.fraTable)
        self.lbl3Best.setMinimumSize(QtCore.QSize(145, 20))
        self.lbl3Best.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lbl3Best.setFont(font)
        self.lbl3Best.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl3Best.setObjectName("lbl3Best")
        self.gridLayout_4.addWidget(self.lbl3Best, 2, 1, 1, 1)
        self.lblMittelwert = QtWidgets.QLabel(self.fraTable)
        self.lblMittelwert.setMinimumSize(QtCore.QSize(145, 20))
        self.lblMittelwert.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblMittelwert.setFont(font)
        self.lblMittelwert.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMittelwert.setObjectName("lblMittelwert")
        self.gridLayout_4.addWidget(self.lblMittelwert, 2, 0, 1, 1)
        self.lblLabel3_5 = QtWidgets.QLabel(self.fraTable)
        self.lblLabel3_5.setMinimumSize(QtCore.QSize(145, 20))
        self.lblLabel3_5.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel3_5.setFont(font)
        self.lblLabel3_5.setObjectName("lblLabel3_5")
        self.gridLayout_4.addWidget(self.lblLabel3_5, 1, 3, 1, 1)
        self.lblBillig = QtWidgets.QLabel(self.fraTable)
        self.lblBillig.setMinimumSize(QtCore.QSize(145, 20))
        self.lblBillig.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblBillig.setFont(font)
        self.lblBillig.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblBillig.setObjectName("lblBillig")
        self.gridLayout_4.addWidget(self.lblBillig, 2, 2, 1, 1)
        self.grdKennwerteDetail = QtWidgets.QTableWidget(self.fraTable)
        self.grdKennwerteDetail.setMinimumSize(QtCore.QSize(400, 250))
        self.grdKennwerteDetail.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.grdKennwerteDetail.setFont(font)
        self.grdKennwerteDetail.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.grdKennwerteDetail.setAutoFillBackground(False)
        self.grdKennwerteDetail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grdKennwerteDetail.setLineWidth(0)
        self.grdKennwerteDetail.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.grdKennwerteDetail.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.grdKennwerteDetail.setRowCount(0)
        self.grdKennwerteDetail.setColumnCount(0)
        self.grdKennwerteDetail.setObjectName("grdKennwerteDetail")
        self.grdKennwerteDetail.horizontalHeader().setCascadingSectionResizes(True)
        self.grdKennwerteDetail.horizontalHeader().setMinimumSectionSize(20)
        self.grdKennwerteDetail.horizontalHeader().setSortIndicatorShown(True)
        self.grdKennwerteDetail.horizontalHeader().setStretchLastSection(True)
        self.grdKennwerteDetail.verticalHeader().setVisible(False)
        self.grdKennwerteDetail.verticalHeader().setDefaultSectionSize(20)
        self.grdKennwerteDetail.verticalHeader().setMinimumSectionSize(20)
        self.gridLayout_4.addWidget(self.grdKennwerteDetail, 4, 0, 1, 5)
        self.lblLabel3_3 = QtWidgets.QLabel(self.fraTable)
        self.lblLabel3_3.setMinimumSize(QtCore.QSize(145, 20))
        self.lblLabel3_3.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel3_3.setFont(font)
        self.lblLabel3_3.setObjectName("lblLabel3_3")
        self.gridLayout_4.addWidget(self.lblLabel3_3, 1, 1, 1, 1)
        self.lblLabel3_4 = QtWidgets.QLabel(self.fraTable)
        self.lblLabel3_4.setMinimumSize(QtCore.QSize(145, 20))
        self.lblLabel3_4.setMaximumSize(QtCore.QSize(145, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblLabel3_4.setFont(font)
        self.lblLabel3_4.setObjectName("lblLabel3_4")
        self.gridLayout_4.addWidget(self.lblLabel3_4, 1, 2, 1, 1)
        self.grdKennwerte = QtWidgets.QTableWidget(self.fraTable)
        self.grdKennwerte.setMinimumSize(QtCore.QSize(400, 250))
        self.grdKennwerte.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.grdKennwerte.setFont(font)
        self.grdKennwerte.setAutoFillBackground(False)
        self.grdKennwerte.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.grdKennwerte.setLineWidth(0)
        self.grdKennwerte.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.grdKennwerte.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.grdKennwerte.setRowCount(0)
        self.grdKennwerte.setColumnCount(0)
        self.grdKennwerte.setObjectName("grdKennwerte")
        self.grdKennwerte.horizontalHeader().setCascadingSectionResizes(True)
        self.grdKennwerte.horizontalHeader().setMinimumSectionSize(20)
        self.grdKennwerte.horizontalHeader().setSortIndicatorShown(True)
        self.grdKennwerte.horizontalHeader().setStretchLastSection(True)
        self.grdKennwerte.verticalHeader().setVisible(False)
        self.grdKennwerte.verticalHeader().setDefaultSectionSize(20)
        self.grdKennwerte.verticalHeader().setMinimumSectionSize(20)
        self.gridLayout_4.addWidget(self.grdKennwerte, 0, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.fraTable, 1, 1, 1, 1)
        self.fraFooter = QtWidgets.QFrame(self.centralwidget)
        self.fraFooter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraFooter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraFooter.setObjectName("fraFooter")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.fraFooter)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lblLabel11 = QtWidgets.QLabel(self.fraFooter)
        self.lblLabel11.setMaximumSize(QtCore.QSize(95, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.lblLabel11.setFont(font)
        self.lblLabel11.setObjectName("lblLabel11")
        self.gridLayout_9.addWidget(self.lblLabel11, 0, 0, 1, 1)
        self.lblProgrammname = QtWidgets.QLabel(self.fraFooter)
        self.lblProgrammname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblProgrammname.setFont(font)
        self.lblProgrammname.setObjectName("lblProgrammname")
        self.gridLayout_9.addWidget(self.lblProgrammname, 0, 1, 1, 1)
        self.lblLabel12 = QtWidgets.QLabel(self.fraFooter)
        self.lblLabel12.setMaximumSize(QtCore.QSize(95, 20))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        self.lblLabel12.setFont(font)
        self.lblLabel12.setObjectName("lblLabel12")
        self.gridLayout_9.addWidget(self.lblLabel12, 1, 0, 1, 1)
        self.lblVersion = QtWidgets.QLabel(self.fraFooter)
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion.setFont(font)
        self.lblVersion.setObjectName("lblVersion")
        self.gridLayout_9.addWidget(self.lblVersion, 1, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.fraFooter, 2, 0, 1, 2)
        self.fraTitle = QtWidgets.QFrame(self.centralwidget)
        self.fraTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTitle.setObjectName("fraTitle")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.fraTitle)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lblTitle = QtWidgets.QLabel(self.fraTitle)
        self.lblTitle.setMinimumSize(QtCore.QSize(200, 30))
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("segoe ui")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("")
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout_7.addWidget(self.lblTitle, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.fraTitle, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        KennwerteBau.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KennwerteBau)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 21))
        self.menubar.setObjectName("menubar")
        KennwerteBau.setMenuBar(self.menubar)

        self.retranslateUi(KennwerteBau)
        QtCore.QMetaObject.connectSlotsByName(KennwerteBau)

    def retranslateUi(self, KennwerteBau):
        _translate = QtCore.QCoreApplication.translate
        KennwerteBau.setWindowTitle(_translate("KennwerteBau", "MainWindow"))
        self.lblLabel4.setText(_translate("KennwerteBau", "Projektkategorie:"))
        self.cmdStartQuery.setText(_translate("KennwerteBau", "Ausführen"))
        self.lblLabel3.setText(_translate("KennwerteBau", "GZ:"))
        self.lblLabel1.setToolTip(_translate("KennwerteBau", "<html><head/><body><p>Durch das setzen von &quot;/&quot; können mehrere Teilbegriffe gesucht werden.</p></body></html>"))
        self.lblLabel1.setText(_translate("KennwerteBau", "Projektbezeichnung:"))
        self.lblLabel4_2.setText(_translate("KennwerteBau", "Kennwert:"))
        self.lblLabel3_2.setText(_translate("KennwerteBau", "MW KW Mittelwert:"))
        self.cmdDetail.setText(_translate("KennwerteBau", "Details"))
        self.lblMedian.setText(_translate("KennwerteBau", "0"))
        self.lbl3Best.setText(_translate("KennwerteBau", "0"))
        self.lblMittelwert.setText(_translate("KennwerteBau", "0"))
        self.lblLabel3_5.setText(_translate("KennwerteBau", "MW KW Median:"))
        self.lblBillig.setText(_translate("KennwerteBau", "0"))
        self.grdKennwerteDetail.setSortingEnabled(True)
        self.lblLabel3_3.setText(_translate("KennwerteBau", "MW KW 3Bestbieter:"))
        self.lblLabel3_4.setText(_translate("KennwerteBau", "MW KW Billigstbieter:"))
        self.grdKennwerte.setSortingEnabled(True)
        self.lblLabel11.setText(_translate("KennwerteBau", "Programmname:"))
        self.lblProgrammname.setText(_translate("KennwerteBau", "Version"))
        self.lblLabel12.setText(_translate("KennwerteBau", "Version:"))
        self.lblVersion.setText(_translate("KennwerteBau", "Version"))
        self.lblTitle.setText(_translate("KennwerteBau", "Dateiname"))
