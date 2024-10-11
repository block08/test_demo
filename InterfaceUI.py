# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.resize(1816, 1290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 240, 1481, 831))
        self.frame.setMinimumSize(QtCore.QSize(1481, 831))
        self.frame.setStyleSheet("#frame{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:none;\n"
"font: 20pt \"幼圆\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/地球.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px\n"
"\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon1)
        self.pushButton_logout.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout_3.addWidget(self.pushButton_logout)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/minimize (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("#frame_6{\n"
"    \n"
"    background-color: rgb(34, 92, 102);\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 50pt \"幼圆\";\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(17, 48, 53);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_exercise = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_exercise.setFont(font)
        self.pushButton_exercise.setObjectName("pushButton_exercise")
        self.verticalLayout_2.addWidget(self.pushButton_exercise)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_main = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_main.setObjectName("pushButton_main")
        self.verticalLayout_2.addWidget(self.pushButton_main)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_highestscore = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_highestscore.setObjectName("pushButton_highestscore")
        self.verticalLayout_2.addWidget(self.pushButton_highestscore)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("#frame_7{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom-right-radius:20px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.page_home)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 30pt \"幼圆\";\n"
"border:1px solid blue;\n"
"border-radius:5px")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_home)
        self.page_exercise = QtWidgets.QWidget()
        self.page_exercise.setObjectName("page_exercise")
        self.run_exercise = QtWidgets.QPushButton(self.page_exercise)
        self.run_exercise.setGeometry(QtCore.QRect(520, 350, 101, 101))
        self.run_exercise.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    padding-bottom:20px\n"
"\n"
"}")
        self.run_exercise.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_exercise.setIcon(icon4)
        self.run_exercise.setIconSize(QtCore.QSize(160, 160))
        self.run_exercise.setObjectName("run_exercise")
        self.label_2 = QtWidgets.QLabel(self.page_exercise)
        self.label_2.setGeometry(QtCore.QRect(300, 220, 511, 71))
        self.label_2.setStyleSheet("font-size: 50px")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_exercise)
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.run_main_test = QtWidgets.QPushButton(self.page_main)
        self.run_main_test.setGeometry(QtCore.QRect(520, 350, 101, 101))
        self.run_main_test.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    padding-bottom:20px\n"
"\n"
"}")
        self.run_main_test.setText("")
        self.run_main_test.setIcon(icon4)
        self.run_main_test.setIconSize(QtCore.QSize(160, 160))
        self.run_main_test.setObjectName("run_main_test")
        self.label_3 = QtWidgets.QLabel(self.page_main)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 591, 101))
        self.label_3.setStyleSheet("font-size: 50px")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_main)
        self.label_4.setGeometry(QtCore.QRect(270, 150, 511, 101))
        self.label_4.setStyleSheet("font-size: 50px")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.page_main)
        self.comboBox.setGeometry(QtCore.QRect(830, 175, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxCount(60)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.page_main)
        self.label_5.setGeometry(QtCore.QRect(940, 150, 61, 101))
        self.label_5.setStyleSheet("font-size: 50px")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_main)
        self.page_highestscore = QtWidgets.QWidget()
        self.page_highestscore.setObjectName("page_highestscore")
        self.stackedWidget.addWidget(self.page_highestscore)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "user"))
        self.pushButton_exercise.setText(_translate("MainWindow", "练习"))
        self.pushButton_main.setText(_translate("MainWindow", "正式实验"))
        self.pushButton_highestscore.setText(_translate("MainWindow", "最高纪录"))
        self.label.setText(_translate("MainWindow", "实现引导语"))
        self.label_2.setText(_translate("MainWindow", "点击按钮进行练习实验"))
        self.label_3.setText(_translate("MainWindow", "2、点击按钮进行正式实验"))
        self.label_4.setText(_translate("MainWindow", "1、选择每人绘图数量："))
        self.comboBox.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox.setItemText(1, _translate("MainWindow", "20"))
        self.comboBox.setItemText(2, _translate("MainWindow", "30"))
        self.label_5.setText(_translate("MainWindow", "张"))
import resouce_rc
