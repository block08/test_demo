# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        MainWindow.resize(1785, 1304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 400, 370, 511))
        self.label.setStyleSheet("border-image: url(:/images/images/astronaut.jpg);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1110, 400, 501, 511))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1150, 470, 431, 44))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"    border:none;\n"
"}\n"
"#pushButton_5{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_5:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton_5:press{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"#pushButton_5:focus{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    border:none;\n"
"}\n"
"#pushButton{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}\n"
"#pushButton:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton:press{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"#pushButton:focus{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"    border:none;\n"
"}\n"
"#pushButton_2{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_2:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton_2:press{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"#pushButton_2:focus{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1550, 410, 41, 41))
        self.pushButton_4.setStyleSheet("#pushButton_4:hover{\n"
"    padding-bottom:10px\n"
"\n"
"}\n"
"\n"
"#pushButton_4{\n"
"    border:none;\n"
"\n"
"}\n"
"")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1500, 410, 41, 41))
        self.pushButton_7.setStyleSheet("#pushButton_7:hover{\n"
"    padding-bottom:10px\n"
"\n"
"}\n"
"\n"
"#pushButton_7{\n"
"    border:none;\n"
"\n"
"}\n"
"")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/minimize (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(1150, 530, 430, 360))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_22 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 270, 411, 51))
        self.pushButton_22.setStyleSheet("#pushButton_22{\n"
"    background-color:rgb(0,0,0);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(0,0,0);\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_22:hover{\n"
"    background-color:rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#pushButton_22:press{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(50, 170, 361, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_23 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_23.setStyleSheet("#pushButton_23{\n"
"    border:none;\n"
"}\n"
"#pushButton_23{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_6.addWidget(self.pushButton_23)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pB_w3_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pB_w3_1.setStyleSheet("#pB_w3_1{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w3_1:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w3_1.setObjectName("pB_w3_1")
        self.horizontalLayout_6.addWidget(self.pB_w3_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.pB_w3_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pB_w3_2.setStyleSheet("#pB_w3_2:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pB_w3_2{\n"
"    font: 13pt \"微软雅黑\";\n"
"}")
        self.pB_w3_2.setObjectName("pB_w3_2")
        self.horizontalLayout_6.addWidget(self.pB_w3_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(50, 220, 361, 42))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_26 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_26.setStyleSheet("#pushButton_26{\n"
"    border:none;\n"
"}\n"
"#pushButton_26{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_7.addWidget(self.pushButton_26)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.pB_w3_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pB_w3_3.setStyleSheet("#pB_w3_3{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w3_3:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w3_3.setObjectName("pB_w3_3")
        self.horizontalLayout_7.addWidget(self.pB_w3_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.pB_w3_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pB_w3_4.setStyleSheet("#pB_w3_4{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w3_4:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w3_4.setObjectName("pB_w3_4")
        self.horizontalLayout_7.addWidget(self.pB_w3_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 100, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(1150, 530, 430, 360))
        self.widget_2.setObjectName("widget_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 270, 411, 51))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    background-color:rgb(0,0,0);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(0,0,0);\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_3:hover{\n"
"    background-color:rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#pushButton_3:press{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 170, 361, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_12.setStyleSheet("#pushButton_12{\n"
"    border:none;\n"
"}\n"
"#pushButton_12{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_2.addWidget(self.pushButton_12)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pB_w2_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pB_w2_1.setStyleSheet("#pB_w2_1{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w2_1:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w2_1.setObjectName("pB_w2_1")
        self.horizontalLayout_2.addWidget(self.pB_w2_1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pB_w2_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pB_w2_2.setStyleSheet("#pB_w2_2{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w2_2:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w2_2.setObjectName("pB_w2_2")
        self.horizontalLayout_2.addWidget(self.pB_w2_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 220, 361, 42))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_13.setStyleSheet("#pushButton_13{\n"
"    border:none;\n"
"}\n"
"#pushButton_13{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.pB_w2_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pB_w2_3.setStyleSheet("#pB_w2_3{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w2_3:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w2_3.setObjectName("pB_w2_3")
        self.horizontalLayout_3.addWidget(self.pB_w2_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.pB_w2_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pB_w2_4.setStyleSheet("#pB_w2_4{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w2_4:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w2_4.setObjectName("pB_w2_4")
        self.horizontalLayout_3.addWidget(self.pB_w2_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.pB_w2_s = QtWidgets.QPushButton(self.widget_2)
        self.pB_w2_s.setGeometry(QtCore.QRect(340, 70, 75, 41))
        self.pB_w2_s.setStyleSheet("")
        self.pB_w2_s.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/放大镜.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_w2_s.setIcon(icon2)
        self.pB_w2_s.setObjectName("pB_w2_s")
        self.widget_1 = QtWidgets.QWidget(self.centralwidget)
        self.widget_1.setGeometry(QtCore.QRect(1150, 530, 430, 360))
        self.widget_1.setObjectName("widget_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius:8px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_1)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 270, 411, 51))
        self.pushButton_14.setStyleSheet("#pushButton_14{\n"
"    background-color:rgb(0,0,0);\n"
"    color:rgb(255,255,255);\n"
"    border:3px solid rgb(0,0,0);\n"
"    border-radius:8px\n"
"}\n"
"#pushButton_14:hover{\n"
"    background-color:rgb(255,255,255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"#pushButton_14:press{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget_1)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 170, 361, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_15.setStyleSheet("#pushButton_15{\n"
"    border:none;\n"
"}\n"
"#pushButton_15{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.pB_w1_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pB_w1_1.setStyleSheet("#pB_w1_1{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w1_1:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w1_1.setObjectName("pB_w1_1")
        self.horizontalLayout_4.addWidget(self.pB_w1_1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.pB_w1_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pB_w1_2.setStyleSheet("#pB_w1_2{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w1_2:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w1_2.setObjectName("pB_w1_2")
        self.horizontalLayout_4.addWidget(self.pB_w1_2)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.widget_1)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(50, 220, 361, 42))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_18.setStyleSheet("#pushButton_18{\n"
"    border:none;\n"
"}\n"
"#pushButton_18{\n"
"    font: 13pt \"微软雅黑\";\n"
"    background-color:rgb(255,255,255);\n"
"    color:rgb(0,0,0);\n"
"\n"
"    border-radius:8px\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_5.addWidget(self.pushButton_18)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.pB_w1_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pB_w1_3.setStyleSheet("#pB_w1_3{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w1_3:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w1_3.setObjectName("pB_w1_3")
        self.horizontalLayout_5.addWidget(self.pB_w1_3)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.pB_w1_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pB_w1_4.setStyleSheet("#pB_w1_4{\n"
"    font: 13pt \"微软雅黑\";\n"
"\n"
"}\n"
"#pB_w1_4:hover{\n"
"    background-color:rgb(0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pB_w1_4.setObjectName("pB_w1_4")
        self.horizontalLayout_5.addWidget(self.pB_w1_4)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.pB_w1_s = QtWidgets.QPushButton(self.widget_1)
        self.pB_w1_s.setGeometry(QtCore.QRect(340, 70, 75, 41))
        self.pB_w1_s.setStyleSheet("")
        self.pB_w1_s.setText("")
        self.pB_w1_s.setIcon(icon2)
        self.pB_w1_s.setObjectName("pB_w1_s")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton_7.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "直接登录"))
        self.pushButton.setText(_translate("MainWindow", "账号登录"))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "账号格式：任务编号(14)+自身代号(02)"))
        self.pushButton_22.setText(_translate("MainWindow", "注册"))
        self.pushButton_23.setText(_translate("MainWindow", "性别："))
        self.pB_w3_1.setText(_translate("MainWindow", "男"))
        self.pB_w3_2.setText(_translate("MainWindow", "女"))
        self.pushButton_26.setText(_translate("MainWindow", "惯用手"))
        self.pB_w3_3.setText(_translate("MainWindow", "左手"))
        self.pB_w3_4.setText(_translate("MainWindow", "右手"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "确认账号"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "人员二：任务编号(14)+自身代号(02)"))
        self.pushButton_3.setText(_translate("MainWindow", "登录"))
        self.pushButton_12.setText(_translate("MainWindow", "性别："))
        self.pB_w2_1.setText(_translate("MainWindow", "男"))
        self.pB_w2_2.setText(_translate("MainWindow", "女"))
        self.pushButton_13.setText(_translate("MainWindow", "惯用手"))
        self.pB_w2_3.setText(_translate("MainWindow", "左手"))
        self.pB_w2_4.setText(_translate("MainWindow", "右手"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "人员一：任务编号(14)+自身代号(01)"))
        self.pushButton_14.setText(_translate("MainWindow", "下一步"))
        self.pushButton_15.setText(_translate("MainWindow", "性别："))
        self.pB_w1_1.setText(_translate("MainWindow", "男"))
        self.pB_w1_2.setText(_translate("MainWindow", "女"))
        self.pushButton_18.setText(_translate("MainWindow", "惯用手"))
        self.pB_w1_3.setText(_translate("MainWindow", "左手"))
        self.pB_w1_4.setText(_translate("MainWindow", "右手"))
import resouce_rc
