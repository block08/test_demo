#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from pygame import time
import InterfaceUI
import main_simulation
from check_serial_connection import check_serial_connection


class Interfacewindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = InterfaceUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.run_exercise.clicked.connect(self.go_main_exercise)
        self.ui.run_main_test.clicked.connect(self.go_main)
        self.ui.pushButton_exercise.clicked.connect(self.go_exercise)
        self.ui.pushButton_main.clicked.connect(self.go_main_test)
        self.ui.pushButton_highestscore.clicked.connect(self.go_highestscore)


    def go_main_exercise(self):
        serial_name = 'COM3'
        if check_serial_connection(serial_name):
            ser_flag = 0
        else:
            ser_flag = 1
        if ser_flag == 0:
            game = main.Game()
            game.run()
        elif ser_flag == 1:
            game = main_simulation.Game()
            game.run()

    def go_main(self):
        painting_number = self.ui.comboBox.currentText()
        serial_name = 'COM3'
        if check_serial_connection(serial_name):
            ser_flag = 0
        else:
            ser_flag = 1
        with open(f"./setting_parameter/painting_number.txt", "w", encoding='utf-8') as file:
            file.write(painting_number)
        time.delay(500)
        with open(f"./setting_parameter/painting_number.txt", "r", encoding='utf-8') as file:
            number = int(file.read())
        if ser_flag == 0:
            if number == 10:
                print(number)
            elif number == 20:
                print(number)
            else:
                game = main_30.Game()
                game.run()
        elif ser_flag == 1:
            if number == 10:
                print(number)
            elif number == 20:
                print(number)
            else:
                game = main_simulation.Game()
                game.run()
    def go_exercise(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def go_main_test(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def go_highestscore(self):
        self.ui.stackedWidget.setCurrentIndex(3)

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

        serial_name = 'COM3'
        if check_serial_connection(serial_name):
            ser_flag = 0
        else:
            ser_flag = 1
        app = QApplication(sys.argv)
        win = Interfacewindow()
        InterfaceUi = InterfaceUI.Ui_MainWindow()
        InterfaceUi.setupUi(win)
        InterfaceUi.stackedWidget.setCurrentIndex(0)

        InterfaceUi.pushButton_exercise.clicked.connect(btn1_clicked)
        InterfaceUi.pushButton_main.clicked.connect(btn2_clicked)
        InterfaceUi.pushButton_highestscore.clicked.connect(btn3_clicked)
        win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Interfacewindow().run()
    sys.exit(app.exec_())