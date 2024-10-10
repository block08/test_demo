# -*- coding: utf-8 -*-
import sqlite3
import csv


def export_to_txt(database_path, table_name, txt_file_path):
    # 连接到数据库
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 查询所有数据
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # 获取列名
    column_names = [description[0] for description in cursor.description]

    # 将数据写入 CSV 文件
    with open(txt_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)  # 写入列名
        writer.writerows(rows)  # 写入所有数据

    conn.close()
