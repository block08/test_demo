#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget

import InterfaceUI
import sqlite3


import main
import main_simulation

class Interfacewindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = InterfaceUI.Ui_MainWindow()
        self.ui.setupUi(self)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


    def run(self):

        def btn1_clicked():
            InterfaceUi.stackedWidget.setCurrentIndex(1)

        def btn2_clicked():
            InterfaceUi.stackedWidget.setCurrentIndex(2)

        def btn3_clicked():
            InterfaceUi.stackedWidget.setCurrentIndex(3)

        app = QApplication(sys.argv)
        win = Interfacewindow()
        InterfaceUi = InterfaceUI.Ui_MainWindow()
        InterfaceUi.setupUi(win)
        InterfaceUi.stackedWidget.setCurrentIndex(0)

        InterfaceUi.pushButton_exercise.clicked.connect(btn1_clicked)
        InterfaceUi.pushButton_main.clicked.connect(btn2_clicked)
        InterfaceUi.pushButton_highestscore.clicked.connect(btn3_clicked)


        win.show()

