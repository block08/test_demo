#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget
import login
import sqlite3
import time

import main
import main_simulation
from check_serial_connection import check_serial_connection
from export_csv import export_to_csv


class TableWidget1(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和尺寸
        self.setWindowTitle("被试人员表")
        self.setGeometry(1000, 500, 600, 400)

        # 创建QTableView和QStandardItemModel
        self.table_view = QTableView()
        self.model = QStandardItemModel(0, 4)
        self.model.setHorizontalHeaderLabels(['序号', 'id', '性别', '惯用手'])

        # 加载SQLite数据库中的数据
        self.load_data()

        # 设置模型到QTableView
        self.table_view.setModel(self.model)

        # 设置表格属性
        self.table_view.setColumnWidth(0, 50)  # 设置复选框列的宽度
        self.table_view.setColumnWidth(1, 170)  # 设置复选框列的宽度
        self.table_view.setColumnWidth(2, 170)  # 设置复选框列的宽度
        self.table_view.setColumnWidth(3, 170)  # 设置复选框列的宽度
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSelectionMode(QTableView.SingleSelection)

        # 添加按钮
        self.button = QPushButton("选择账号")
        self.button.clicked.connect(self.get_selected_id)

        # 布局管理
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.button)

        self.setLayout(layout)  # 使用布局管理器

    def load_data(self):
        conn = sqlite3.connect("./user_account/Experimenter.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()

        for row in rows:
            # 创建带复选框的项目
            checkbox_item = QStandardItem()
            checkbox_item.setCheckable(True)
            checkbox_item.setEditable(False)
            checkbox_item.setCheckState(Qt.Unchecked)  # 默认不选中

            # 添加行数据
            id_item = QStandardItem(str(row[0]))
            sexy_item = QStandardItem(row[1])
            hand_prefere = QStandardItem(row[2])

            # 设置不可编辑
            id_item.setEditable(False)
            sexy_item.setEditable(False)
            hand_prefere.setEditable(False)

            # 插入到模型中
            self.model.appendRow([checkbox_item, id_item, sexy_item, hand_prefere])

        # 连接复选框点击事件
        self.table_view.clicked.connect(self.handle_checkbox_click)

        conn.close()

    def handle_checkbox_click(self, index):
        # 获取被点击的复选框项
        if index.column() == 0:  # 确保只处理复选框列
            clicked_item = self.model.item(index.row(), 0)

            # 如果复选框被勾选，则取消其他行的复选框勾选
            if clicked_item.checkState() == Qt.Checked:
                for row in range(self.model.rowCount()):
                    if row != index.row():
                        checkbox_item = self.model.item(row, 0)
                        checkbox_item.setCheckState(Qt.Unchecked)
            else:
                clicked_item.setCheckState(Qt.Checked)  # 点击后自动勾选

    def get_selected_id(self):

        selected_row = None

        # 查找选中的复选框
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)  # 复选框列
            if item.checkState() == Qt.Checked:
                selected_row = row
                break

        if selected_row is not None:

            id_data = self.model.item(selected_row, 1).text()
            sex_data = self.model.item(selected_row, 2).text()
            hand_data = self.model.item(selected_row, 3).text()
            loginUi.lineEdit_2.setText(id_data)
            if sex_data == "男":
                clicked_colorchange1()
            elif sex_data == "女":
                clicked_colorchange2()
            if hand_data == "左手":
                clicked_colorchange3()
            elif hand_data == "右手":
                clicked_colorchange4()
            QMessageBox.information(self, "选择账号", f"选择用户为: {id_data}")
            self.close()

        else:
            QMessageBox.warning(self, "没选择", "没有选择框被选中")


class TableWidget2(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和尺寸
        self.setWindowTitle("被试人员表")
        self.setGeometry(1000, 500, 600, 400)

        # 创建QTableView和QStandardItemModel
        self.table_view = QTableView()
        self.model = QStandardItemModel(0, 4)
        self.model.setHorizontalHeaderLabels(['序号', 'id', '性别', '惯用手'])

        # 加载SQLite数据库中的数据
        self.load_data()

        # 设置模型到QTableView
        self.table_view.setModel(self.model)

        # 设置表格属性
        self.table_view.setColumnWidth(0, 50)  # 设置复选框列的宽度
        self.table_view.setColumnWidth(1, 170)  # 设置复选框列的宽度
        self.table_view.setColumnWidth(2, 170)  # 设置复选框列的宽度
        self.table_view.setColumnWidth(3, 170)  # 设置复选框列的宽度
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSelectionMode(QTableView.SingleSelection)

        # 添加按钮
        self.button = QPushButton("选择账号")
        self.button.clicked.connect(self.get_selected_id)

        # 布局管理
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.button)

        self.setLayout(layout)  # 使用布局管理器

    def load_data(self):
        conn = sqlite3.connect("./user_account/Experimenter.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()

        for row in rows:
            # 创建带复选框的项目
            checkbox_item = QStandardItem()
            checkbox_item.setCheckable(True)
            checkbox_item.setEditable(False)
            checkbox_item.setCheckState(Qt.Unchecked)  # 默认不选中

            # 添加行数据
            id_item = QStandardItem(str(row[0]))
            sexy_item = QStandardItem(row[1])
            hand_prefere = QStandardItem(row[2])

            # 设置不可编辑
            id_item.setEditable(False)
            sexy_item.setEditable(False)
            hand_prefere.setEditable(False)

            # 插入到模型中
            self.model.appendRow([checkbox_item, id_item, sexy_item, hand_prefere])

        # 连接复选框点击事件
        self.table_view.clicked.connect(self.handle_checkbox_click)

        conn.close()

    def handle_checkbox_click(self, index):
        # 获取被点击的复选框项
        if index.column() == 0:  # 确保只处理复选框列
            clicked_item = self.model.item(index.row(), 0)

            # 如果复选框被勾选，则取消其他行的复选框勾选
            if clicked_item.checkState() == Qt.Checked:
                for row in range(self.model.rowCount()):
                    if row != index.row():
                        checkbox_item = self.model.item(row, 0)
                        checkbox_item.setCheckState(Qt.Unchecked)
            else:
                clicked_item.setCheckState(Qt.Checked)  # 点击后自动勾选

    def get_selected_id(self):
        selected_row = None

        # 查找选中的复选框
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)  # 复选框列
            if item.checkState() == Qt.Checked:
                selected_row = row
                break

        if selected_row is not None:

            id_data = self.model.item(selected_row, 1).text()
            sex_data = self.model.item(selected_row, 2).text()
            hand_data = self.model.item(selected_row, 3).text()
            loginUi.lineEdit.setText(id_data)
            if sex_data == "男":
                clicked_colorchange5()
            elif sex_data == "女":
                clicked_colorchange6()
            if hand_data == "左手":
                clicked_colorchange7()
            elif hand_data == "右手":
                clicked_colorchange8()

            QMessageBox.information(self, "选择账号", f"选择用户为: {id_data}")
            self.close()

        else:
            QMessageBox.warning(self, "没选择", "没有选择框被选中")

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter = 0  # 计数器初始化

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
    def select_user1(self):
        self.widget = TableWidget1()
        self.widget.show()
    def select_user2(self):
        self.widget = TableWidget2()
        self.widget.show()




if __name__ == '__main__':
    pB1_1 = False
    pB1_2 = False
    pB2_1 = False
    pB2_2 = False
    pB3_1 = False
    pB3_2 = False



    def change_widget2():
        loginUi.widget_2.show()
        loginUi.widget_3.hide()
        loginUi.widget_1.hide()


    def change_widget3():
        loginUi.widget_2.hide()
        loginUi.widget_3.show()
        loginUi.widget_1.hide()


    def change_widget1():
        loginUi.widget_2.hide()
        loginUi.widget_3.hide()
        loginUi.widget_1.show()


    def btn_clicked():
        global flag1, flag2  # 使用全局变量
        # 从界面获取输入
        user_id = loginUi.lineEdit_2.text()  # 获取被试编号
        gender = ""
        hand_preference = ""

        # 根据 flag1 和 flag2 的值确定性别和惯用手
        if flag1 == 1:
            gender = "男"
        elif flag1 == 2:
            gender = "女"

        if flag2 == 1:
            hand_preference = "左手"
        elif flag2 == 2:
            hand_preference = "右手"

        # 检查是否有被试编号输入
        if not user_id:
            QMessageBox.warning(None, "警告", "被试编号不能为空！", QMessageBox.Ok)
            return

        # 检查性别和惯用手是否选择
        if flag1 not in [1, 2]:
            QMessageBox.warning(None, "警告", "性别不能为空！", QMessageBox.Ok)
            return

        if flag2 not in [1, 2]:
            QMessageBox.warning(None, "警告", "惯用手不能为空！", QMessageBox.Ok)
            return

        # 连接数据库并查询用户信息
        try:
            conn = sqlite3.connect("./user_account/Experimenter.db")
            cursor = conn.cursor()
            sql = 'select id, 性别, 惯用手 from user where id = ? and 性别 = ? and 惯用手 = ?;'
            cursor.execute(sql, (user_id, gender, hand_preference))
            data = cursor.fetchall()

            if data:  # 如果账号存在
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                # 插入数据到输出数据库
                conn_output = sqlite3.connect("./output_data/output_subInfo.db")
                cursor_output = conn_output.cursor()

                cursor_output.execute('''
                    CREATE TABLE IF NOT EXISTS data (
                    登录时间 timestamp TEXT NOT NULL,
                    被试编号 FLOAT NOT NULL, 
                    性别 TEXT NOT NULL, 
                    惯用手 TEXT NOT NULL 
                    )
                ''')

                sql_insert = 'INSERT INTO data(登录时间, 被试编号, 性别, 惯用手) VALUES(?,?,?,?)'
                cursor_output.execute(sql_insert, (timestamp, user_id, gender, hand_preference))

                conn_output.commit()

                # 切换界面
                loginUi.widget_1.hide()
                loginUi.widget_2.show()
                loginUi.widget_3.hide()
            else:
                QMessageBox.warning(None, "警告", "您的登录账号错误或者性别或惯用手不匹配！", QMessageBox.Ok)

        except Exception as e:
            QMessageBox.critical(None, "错误", f"数据库操作失败: {e}", QMessageBox.Ok)

        finally:
            # 确保数据库连接关闭
            cursor.close()
            conn.close()
            if 'cursor_output' in locals():
                cursor_output.close()
                conn_output.close()


    def btn_clicked1():
        global flag3, flag4
        # 从界面获取输入
        user_id = loginUi.lineEdit.text()  # 获取被试编号
        gender = ""
        hand_preference = ""

        # 根据 flag3 和 flag4 的值确定性别和惯用手
        if flag3 == 1:
            gender = "男"
        elif flag3 == 2:
            gender = "女"

        if flag4 == 1:
            hand_preference = "左手"
        elif flag4 == 2:
            hand_preference = "右手"

        # 检查是否有被试编号输入
        if not user_id:
            QMessageBox.warning(None, "警告", "被试编号不能为空！", QMessageBox.Ok)
            return

        # 检查性别和惯用手是否选择
        if flag3 not in [1, 2]:
            QMessageBox.warning(None, "警告", "性别不能为空！", QMessageBox.Ok)
            return

        if flag4 not in [1, 2]:
            QMessageBox.warning(None, "警告", "惯用手不能为空！", QMessageBox.Ok)
            return

        # 连接数据库并查询用户信息
        try:
            conn = sqlite3.connect("./user_account/Experimenter.db")
            cursor = conn.cursor()
            sql = 'select id, 性别, 惯用手 from user where id = ? and 性别 = ? and 惯用手 = ?;'
            cursor.execute(sql, (user_id, gender, hand_preference))
            data = cursor.fetchall()
            if data:  # 如果账号存在
                if loginUi.lineEdit_2.text() == loginUi.lineEdit.text():
                    QMessageBox.warning(None, "警告", "被试一和被试二不能为同一个人", QMessageBox.Ok)
                else:
                    if ser_flag == 1:
                        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                        # 插入数据到输出数据库
                        conn_output = sqlite3.connect("./output_data/output_subInfo.db")
                        cursor_output = conn_output.cursor()

                        cursor_output.execute('''
                                                    CREATE TABLE IF NOT EXISTS data (
                                                    登录时间 timestamp TEXT NOT NULL,
                                                    被试编号 FLOAT NOT NULL, 
                                                    性别 TEXT NOT NULL, 
                                                    惯用手 TEXT NOT NULL 
                                                    )
                                                ''')

                        sql_insert = 'INSERT INTO data(登录时间, 被试编号, 性别, 惯用手) VALUES(?,?,?,?)'
                        cursor_output.execute(sql_insert, (timestamp, user_id, gender, hand_preference))
                        export_to_csv("./output_data/output_subInfo.db", "data", "./output_data/output_subInfo.csv")
                        conn_output.commit()
                        cursor.close()
                        conn.close()
                        choice = QMessageBox.question(None, "提示", "未检查到串口连接，是否只记录行为学数据的仿真模式",
                                             QMessageBox.Yes | QMessageBox.No)
                        if choice == QMessageBox.Yes:
                            win.close()
                            game = main_simulation.Game()
                            game.run()
                        else:
                            win.close()
                            sys.exit()

                    elif ser_flag == 0:
                        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                        # 插入数据到输出数据库
                        conn_output = sqlite3.connect("./output_data/output_subInfo.db")
                        cursor_output = conn_output.cursor()

                        cursor_output.execute('''
                                                                       CREATE TABLE IF NOT EXISTS data (
                                                                       登录时间 timestamp TEXT NOT NULL,
                                                                       被试编号 FLOAT NOT NULL, 
                                                                       性别 TEXT NOT NULL, 
                                                                       惯用手 TEXT NOT NULL 
                                                                       )
                                                                   ''')

                        sql_insert = 'INSERT INTO data(登录时间, 被试编号, 性别, 惯用手) VALUES(?,?,?,?)'
                        cursor_output.execute(sql_insert, (timestamp, user_id, gender, hand_preference))
                        export_to_csv("./output_data/output_subInfo.db", "data", "./output_data/output_subInfo.csv")
                        conn_output.commit()
                        conn.close()
                        cursor_output.close()
                        conn_output.close()
                        QMessageBox.information(None, "提示", "登录成功", QMessageBox.Ok)
                        win.close()
                        game = main.Game()
                        game.run()
                        win.close()
            else:
                QMessageBox.warning(None, "警告", "您的登录账号错误或者性别或惯用手不匹配！", QMessageBox.Ok)

        except Exception as e:
            QMessageBox.critical(None, "错误", f"数据库操作失败: {e}", QMessageBox.Ok)




    def register_clicked():
        global flag5, flag6
        gender = ""
        hand_preference = ""

        # 性别判断
        if flag5 == 1:
            gender = "男"
        elif flag5 == 2:
            gender = "女"
        else:
            QMessageBox.warning(None, "警告", "性别不能为空！", QMessageBox.Ok)
            return  # 如果性别未选择，直接返回，避免后续代码执行

        # 惯用手判断
        if flag6 == 1:
            hand_preference = "左手"
        elif flag6 == 2:
            hand_preference = "右手"
        else:
            QMessageBox.warning(None, "警告", "惯用手不能为空！", QMessageBox.Ok)
            return  # 如果惯用手未选择，直接返回，避免后续代码执行

        # 获取用户输入的账号和确认账号
        user_id = loginUi.lineEdit_3.text()
        id_confirm = loginUi.lineEdit_4.text()

        if not user_id or not id_confirm:  # 检查账号是否为空
            QMessageBox.warning(None, "警告", "账号不能为空！", QMessageBox.Ok)
            return

        if user_id != id_confirm:  # 检查两次输入的账号是否匹配
            QMessageBox.warning(None, "警告", "两次输入的账号不匹配！", QMessageBox.Ok)
            return

        try:
            conn = sqlite3.connect("./user_account/Experimenter.db")
            cursor = conn.cursor()

            # 查询数据库中是否已经存在相同的账号
            cursor.execute('SELECT id FROM user WHERE id = ?', (user_id,))
            data = cursor.fetchone()

            if data:  # 如果账号已经存在
                QMessageBox.warning(None, "警告", "被试编号已存在", QMessageBox.Ok)
            else:
                # 创建用户表（如果尚不存在）
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user (
                        id INT NOT NULL, 
                        性别 TEXT NOT NULL, 
                        惯用手 TEXT NOT NULL 
                    )
                ''')

                # 插入新用户数据
                sql_insert = 'INSERT INTO user(id, 性别, 惯用手) VALUES(?,?,?)'
                cursor.execute(sql_insert, (user_id, gender, hand_preference))

                conn.commit()
                QMessageBox.information(None, "通知", "注册成功！", QMessageBox.Ok)

        except Exception as e:
            QMessageBox.critical(None, "错误", f"数据库操作失败: {e}", QMessageBox.Ok)

        finally:
            # 确保关闭数据库连接
            cursor.close()
            conn.close()






    def clicked_colorchange1():
        global flag1
        loginUi.pB_w1_1.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        loginUi.pB_w1_2.setStyleSheet(" background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        flag1 = 1



    def clicked_colorchange2():
        global flag1
        loginUi.pB_w1_1.setStyleSheet("	background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        loginUi.pB_w1_2.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        flag1 = 2



    def clicked_colorchange3():
        global flag2
        loginUi.pB_w1_3.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        loginUi.pB_w1_4.setStyleSheet(" background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        flag2 = 1



    def clicked_colorchange4():
        global flag2
        loginUi.pB_w1_3.setStyleSheet("	background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        loginUi.pB_w1_4.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        flag2 = 2


    def clicked_colorchange5():
        global flag3
        loginUi.pB_w2_1.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        loginUi.pB_w2_2.setStyleSheet(" background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        flag3 = 1


    def clicked_colorchange6():
        global flag3
        loginUi.pB_w2_1.setStyleSheet("	background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        loginUi.pB_w2_2.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        flag3 = 2


    def clicked_colorchange7():
        global flag4
        loginUi.pB_w2_3.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        loginUi.pB_w2_4.setStyleSheet(" background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        flag4 = 1


    def clicked_colorchange8():
        global flag4
        loginUi.pB_w2_3.setStyleSheet("	background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        loginUi.pB_w2_4.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        flag4 = 2


    def clicked_colorchange9():
        global flag5
        loginUi.pB_w3_1.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        loginUi.pB_w3_2.setStyleSheet(" background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        flag5 = 1


    def clicked_colorchange10():
        global flag5
        loginUi.pB_w3_1.setStyleSheet("	background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        loginUi.pB_w3_2.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        flag5 = 2


    def clicked_colorchange11():
        global flag6
        loginUi.pB_w3_3.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        loginUi.pB_w3_4.setStyleSheet(" background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        flag6 = 1


    def clicked_colorchange12():
        global flag6
        loginUi.pB_w3_3.setStyleSheet("	background-color:rgb(255,255,255);color: rgb(0, 0, 0);font: 13pt ")
        loginUi.pB_w3_4.setStyleSheet("	background-color:rgb(0,0,0);color: rgb(255, 255, 255);font: 13pt ")
        flag6 = 2

    flag1 = 0
    flag2 = 0
    ti = datetime.datetime.now()
    ti = ti.strftime("%Y_%m_%d_%H_%M_%S")
    with open(f"./Behavioral_data/name.txt", "w") as file:
        file.write(ti)
    serial_name = 'COM3'
    app = QApplication(sys.argv)
    win = LoginWindow()
    loginUi = login.Ui_MainWindow()
    loginUi.setupUi(win)

    if check_serial_connection(serial_name):
        ser_flag = 0
    else:
        ser_flag = 1
    loginUi.widget_3.hide()
    loginUi.widget_2.hide()
    loginUi.pB_w1_s.clicked.connect(win.select_user1)
    loginUi.pB_w2_s.clicked.connect(win.select_user2)
    loginUi.pB_w1_1.clicked.connect(clicked_colorchange1)
    loginUi.pB_w1_2.clicked.connect(clicked_colorchange2)
    loginUi.pB_w1_3.clicked.connect(clicked_colorchange3)
    loginUi.pB_w1_4.clicked.connect(clicked_colorchange4)
    loginUi.pB_w2_1.clicked.connect(clicked_colorchange5)
    loginUi.pB_w2_2.clicked.connect(clicked_colorchange6)
    loginUi.pB_w2_3.clicked.connect(clicked_colorchange7)
    loginUi.pB_w2_4.clicked.connect(clicked_colorchange8)
    loginUi.pB_w3_1.clicked.connect(clicked_colorchange9)
    loginUi.pB_w3_2.clicked.connect(clicked_colorchange10)
    loginUi.pB_w3_3.clicked.connect(clicked_colorchange11)
    loginUi.pB_w3_4.clicked.connect(clicked_colorchange12)
    loginUi.pushButton_14.clicked.connect(btn_clicked)
    loginUi.pushButton_3.clicked.connect(btn_clicked1)
    loginUi.pushButton_2.clicked.connect(change_widget3)
    loginUi.pushButton.clicked.connect(change_widget1)
    loginUi.pushButton_22.clicked.connect(register_clicked)

    win.show()
    sys.exit(app.exec_())
