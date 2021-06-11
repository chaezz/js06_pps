# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStatusTip("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1921, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 1919, 540))
        self.image_label.setStyleSheet("")
        self.image_label.setText("")
        self.image_label.setScaledContents(True)
        self.image_label.setObjectName("image_label")
        self.graph_label = QtWidgets.QLabel(self.centralwidget)
        self.graph_label.setGeometry(QtCore.QRect(640, 620, 640, 411))
        self.graph_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.graph_label.setFont(font)
        self.graph_label.setStyleSheet("border: 1px solid black;\n"
"")
        self.graph_label.setText("")
        self.graph_label.setAlignment(QtCore.Qt.AlignCenter)
        self.graph_label.setObjectName("graph_label")
        self.imagelist = QtWidgets.QListWidget(self.centralwidget)
        self.imagelist.setGeometry(QtCore.QRect(0, 620, 640, 201))
        self.imagelist.setMouseTracking(False)
        self.imagelist.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.imagelist.setAutoFillBackground(False)
        self.imagelist.setStyleSheet("")
        self.imagelist.setLineWidth(0)
        self.imagelist.setAutoScrollMargin(1)
        self.imagelist.setProperty("showDropIndicator", False)
        self.imagelist.setDragEnabled(False)
        self.imagelist.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.imagelist.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.imagelist.setIconSize(QtCore.QSize(200, 200))
        self.imagelist.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.imagelist.setMovement(QtWidgets.QListView.Free)
        self.imagelist.setFlow(QtWidgets.QListView.LeftToRight)
        self.imagelist.setUniformItemSizes(False)
        self.imagelist.setWordWrap(True)
        self.imagelist.setSelectionRectVisible(True)
        self.imagelist.setObjectName("imagelist")
        self.extiction_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.extiction_groupbox.setGeometry(QtCore.QRect(0, 830, 640, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.extiction_groupbox.setFont(font)
        self.extiction_groupbox.setStyleSheet("")
        self.extiction_groupbox.setObjectName("extiction_groupbox")
        self.red_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.red_label.setGeometry(QtCore.QRect(40, 50, 61, 21))
        self.red_label.setAlignment(QtCore.Qt.AlignCenter)
        self.red_label.setObjectName("red_label")
        self.green_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.green_label.setGeometry(QtCore.QRect(40, 110, 61, 21))
        self.green_label.setAlignment(QtCore.Qt.AlignCenter)
        self.green_label.setObjectName("green_label")
        self.blue_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.blue_label.setGeometry(QtCore.QRect(40, 170, 61, 21))
        self.blue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blue_label.setObjectName("blue_label")
        self.r_c1_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.r_c1_textbox.setGeometry(QtCore.QRect(160, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.r_c1_textbox.setFont(font)
        self.r_c1_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.r_c1_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.r_c1_textbox.setObjectName("r_c1_textbox")
        self.r_c1_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.r_c1_label.setGeometry(QtCore.QRect(120, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r_c1_label.setFont(font)
        self.r_c1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.r_c1_label.setObjectName("r_c1_label")
        self.r_c2_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.r_c2_textbox.setGeometry(QtCore.QRect(320, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.r_c2_textbox.setFont(font)
        self.r_c2_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.r_c2_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.r_c2_textbox.setObjectName("r_c2_textbox")
        self.r_c2_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.r_c2_label.setGeometry(QtCore.QRect(280, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r_c2_label.setFont(font)
        self.r_c2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.r_c2_label.setObjectName("r_c2_label")
        self.r_alpha_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.r_alpha_textbox.setGeometry(QtCore.QRect(500, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.r_alpha_textbox.setFont(font)
        self.r_alpha_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.r_alpha_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.r_alpha_textbox.setObjectName("r_alpha_textbox")
        self.r_alpha_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.r_alpha_label.setGeometry(QtCore.QRect(450, 50, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r_alpha_label.setFont(font)
        self.r_alpha_label.setAlignment(QtCore.Qt.AlignCenter)
        self.r_alpha_label.setObjectName("r_alpha_label")
        self.g_c2_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.g_c2_textbox.setGeometry(QtCore.QRect(320, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.g_c2_textbox.setFont(font)
        self.g_c2_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g_c2_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g_c2_textbox.setObjectName("g_c2_textbox")
        self.g_alpha_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.g_alpha_label.setGeometry(QtCore.QRect(450, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.g_alpha_label.setFont(font)
        self.g_alpha_label.setAlignment(QtCore.Qt.AlignCenter)
        self.g_alpha_label.setObjectName("g_alpha_label")
        self.g_alpha_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.g_alpha_textbox.setGeometry(QtCore.QRect(500, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.g_alpha_textbox.setFont(font)
        self.g_alpha_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g_alpha_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g_alpha_textbox.setObjectName("g_alpha_textbox")
        self.g_c2_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.g_c2_label.setGeometry(QtCore.QRect(280, 110, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.g_c2_label.setFont(font)
        self.g_c2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.g_c2_label.setObjectName("g_c2_label")
        self.g_c1_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.g_c1_textbox.setGeometry(QtCore.QRect(160, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.g_c1_textbox.setFont(font)
        self.g_c1_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g_c1_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g_c1_textbox.setObjectName("g_c1_textbox")
        self.g_c1_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.g_c1_label.setGeometry(QtCore.QRect(120, 110, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.g_c1_label.setFont(font)
        self.g_c1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.g_c1_label.setObjectName("g_c1_label")
        self.b_c1_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.b_c1_textbox.setGeometry(QtCore.QRect(160, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.b_c1_textbox.setFont(font)
        self.b_c1_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b_c1_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b_c1_textbox.setObjectName("b_c1_textbox")
        self.b_alpha_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.b_alpha_textbox.setGeometry(QtCore.QRect(500, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.b_alpha_textbox.setFont(font)
        self.b_alpha_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b_alpha_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b_alpha_textbox.setObjectName("b_alpha_textbox")
        self.b_alpha_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.b_alpha_label.setGeometry(QtCore.QRect(450, 170, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_alpha_label.setFont(font)
        self.b_alpha_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_alpha_label.setObjectName("b_alpha_label")
        self.b_c2_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.b_c2_label.setGeometry(QtCore.QRect(280, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_c2_label.setFont(font)
        self.b_c2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_c2_label.setObjectName("b_c2_label")
        self.b_c1_label = QtWidgets.QLabel(self.extiction_groupbox)
        self.b_c1_label.setGeometry(QtCore.QRect(120, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b_c1_label.setFont(font)
        self.b_c1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.b_c1_label.setObjectName("b_c1_label")
        self.b_c2_textbox = QtWidgets.QTextEdit(self.extiction_groupbox)
        self.b_c2_textbox.setGeometry(QtCore.QRect(320, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.b_c2_textbox.setFont(font)
        self.b_c2_textbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b_c2_textbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b_c2_textbox.setObjectName("b_c2_textbox")
        self.graph_label_name = QtWidgets.QLabel(self.centralwidget)
        self.graph_label_name.setGeometry(QtCore.QRect(860, 570, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.graph_label_name.setFont(font)
        self.graph_label_name.setStyleSheet("")
        self.graph_label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.graph_label_name.setObjectName("graph_label_name")
        self.targetlist_label_name = QtWidgets.QLabel(self.centralwidget)
        self.targetlist_label_name.setGeometry(QtCore.QRect(240, 570, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.targetlist_label_name.setFont(font)
        self.targetlist_label_name.setStyleSheet("")
        self.targetlist_label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.targetlist_label_name.setObjectName("targetlist_label_name")
        self.time_label_name = QtWidgets.QLabel(self.centralwidget)
        self.time_label_name.setGeometry(QtCore.QRect(1560, 570, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.time_label_name.setFont(font)
        self.time_label_name.setStyleSheet("")
        self.time_label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label_name.setObjectName("time_label_name")
        self.visibility_label_name = QtWidgets.QLabel(self.centralwidget)
        self.visibility_label_name.setGeometry(QtCore.QRect(1300, 630, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.visibility_label_name.setFont(font)
        self.visibility_label_name.setStyleSheet("")
        self.visibility_label_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.visibility_label_name.setObjectName("visibility_label_name")
        self.visibility_value = QtWidgets.QLabel(self.centralwidget)
        self.visibility_value.setGeometry(QtCore.QRect(1430, 700, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.visibility_value.setFont(font)
        self.visibility_value.setStyleSheet("")
        self.visibility_value.setAlignment(QtCore.Qt.AlignCenter)
        self.visibility_value.setObjectName("visibility_value")
        self.pm25_label_name = QtWidgets.QLabel(self.centralwidget)
        self.pm25_label_name.setGeometry(QtCore.QRect(1300, 850, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pm25_label_name.setFont(font)
        self.pm25_label_name.setStyleSheet("")
        self.pm25_label_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pm25_label_name.setObjectName("pm25_label_name")
        self.pm25_value = QtWidgets.QLabel(self.centralwidget)
        self.pm25_value.setGeometry(QtCore.QRect(1430, 900, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pm25_value.setFont(font)
        self.pm25_value.setStyleSheet("")
        self.pm25_value.setAlignment(QtCore.Qt.AlignCenter)
        self.pm25_value.setObjectName("pm25_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setToolTipsVisible(True)
        self.menuFile.setObjectName("menuFile")
        self.menustart = QtWidgets.QMenu(self.menuFile)
        self.menustart.setGeometry(QtCore.QRect(0, 0, 172, 169))
        self.menustart.setStyleSheet("")
        self.menustart.setTearOffEnabled(False)
        self.menustart.setToolTipsVisible(True)
        self.menustart.setObjectName("menustart")
        self.menuMethod = QtWidgets.QMenu(self.menubar)
        self.menuMethod.setObjectName("menuMethod")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setMaximumSize(QtCore.QSize(0, 0))
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionupdate = QtWidgets.QAction(MainWindow)
        self.actionupdate.setObjectName("actionupdate")
        self.actionPNM_9030V = QtWidgets.QAction(MainWindow)
        self.actionPNM_9030V.setObjectName("actionPNM_9030V")
        self.actionQNO_8020R = QtWidgets.QAction(MainWindow)
        self.actionQNO_8020R.setObjectName("actionQNO_8020R")
        self.actionWebcam = QtWidgets.QAction(MainWindow)
        self.actionWebcam.setObjectName("actionWebcam")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionRpi_Telephoto_lens = QtWidgets.QAction(MainWindow)
        self.actionRpi_Telephoto_lens.setObjectName("actionRpi_Telephoto_lens")
        self.actionRpi_noir = QtWidgets.QAction(MainWindow)
        self.actionRpi_noir.setObjectName("actionRpi_noir")
        self.actionImage = QtWidgets.QAction(MainWindow)
        self.actionImage.setEnabled(True)
        self.actionImage.setObjectName("actionImage")
        self.menustart.addSeparator()
        self.menustart.addAction(self.actionPNM_9030V)
        self.menustart.addAction(self.actionQNO_8020R)
        self.menustart.addAction(self.actionWebcam)
        self.menustart.addAction(self.actionRpi_Telephoto_lens)
        self.menustart.addAction(self.actionRpi_noir)
        self.menuFile.addAction(self.menustart.menuAction())
        self.menuFile.addAction(self.actionImage)
        self.menuFile.addAction(self.actionupdate)
        self.menuMethod.addAction(self.actionPrint)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMethod.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ND01"))
        self.extiction_groupbox.setTitle(_translate("MainWindow", "RGB Extinction(소산계수)"))
        self.red_label.setText(_translate("MainWindow", "Red"))
        self.green_label.setText(_translate("MainWindow", "Green"))
        self.blue_label.setText(_translate("MainWindow", "Blue"))
        self.r_c1_label.setText(_translate("MainWindow", "C1"))
        self.r_c2_label.setText(_translate("MainWindow", "C2"))
        self.r_alpha_label.setText(_translate("MainWindow", "Alpha"))
        self.g_alpha_label.setText(_translate("MainWindow", "Alpha"))
        self.g_c2_label.setText(_translate("MainWindow", "C2"))
        self.g_c1_label.setText(_translate("MainWindow", "C1"))
        self.b_alpha_label.setText(_translate("MainWindow", "Alpha"))
        self.b_c2_label.setText(_translate("MainWindow", "C2"))
        self.b_c1_label.setText(_translate("MainWindow", "C1"))
        self.graph_label_name.setText(_translate("MainWindow", "Extinction Graph"))
        self.targetlist_label_name.setText(_translate("MainWindow", "Target List"))
        self.time_label_name.setText(_translate("MainWindow", "Time"))
        self.visibility_label_name.setText(_translate("MainWindow", "Visibility"))
        self.visibility_value.setText(_translate("MainWindow", "0 km"))
        self.pm25_label_name.setText(_translate("MainWindow", "PM2.5"))
        self.pm25_value.setText(_translate("MainWindow", "0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menustart.setTitle(_translate("MainWindow", "Camera"))
        self.menuMethod.setTitle(_translate("MainWindow", "Method"))
        self.actionupdate.setText(_translate("MainWindow", "Update"))
        self.actionPNM_9030V.setText(_translate("MainWindow", "PNM-9030V"))
        self.actionQNO_8020R.setText(_translate("MainWindow", "QNO-8020R"))
        self.actionWebcam.setText(_translate("MainWindow", "Webcam"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionRpi_Telephoto_lens.setText(_translate("MainWindow", "Rpi-Telephoto-lens"))
        self.actionRpi_noir.setText(_translate("MainWindow", "Rpi-Noir"))
        self.actionImage.setText(_translate("MainWindow", "Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
