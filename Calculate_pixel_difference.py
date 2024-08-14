# -*- coding: utf-8 -*-


import cv2
import numpy as np




def save_cropped_image(frame, x, y, width, height, filename):
    # 裁剪指定区域
    roi = frame[y:y+height, x:x+width]
    return roi


def calculate_pixel_difference(origin_image, image1, image2, t1, t2, timestamp):
    x, y, width, height = 0, 50, 1920, 920
    origin_image = save_cropped_image(origin_image, x, y, width, height, timestamp)
    image1 = save_cropped_image(image1, x, y, width, height, timestamp)
    image2 = save_cropped_image(image2, x, y, width, height, timestamp)
    # 确保两幅图片的尺寸相同
    gray_origin_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    _, binary_origin_image = cv2.threshold(gray_origin_image, 0, 255, cv2.THRESH_BINARY)
    change = abs(image2 - image1 - origin_image)
    gray_image = cv2.cvtColor(change, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)
    binary_total_image = np.sum(binary_origin_image == 0)
    binary_pixel = np.sum(binary_image == 0)
    diff_percentage = binary_pixel / binary_total_image * 100
    t = t2 - t1

    with open(f"./Behavioral_data/name.txt", "r") as file:
        time = file.read()
    with open(f"./Behavioral_data/subA/Behavioral_data{time}.txt", "a", encoding="utf-8") as f:
        # 输出结果
        f.write(f"有效像素: {binary_pixel}   总像素: {binary_total_image}   百分比：{diff_percentage:.2f}%   绘图时长：{t} \n")
def calculate_pixel_difference2(origin_image, image1, image2, t1, t2, timestamp):
    x, y, width, height = 0, 50, 1920, 920
    origin_image = save_cropped_image(origin_image, x, y, width, height, timestamp)
    image1 = save_cropped_image(image1, x, y, width, height, timestamp)
    image2 = save_cropped_image(image2, x, y, width, height, timestamp)
    # 确保两幅图片的尺寸相同
    gray_origin_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    _, binary_origin_image = cv2.threshold(gray_origin_image, 0, 255, cv2.THRESH_BINARY)
    change = abs(image2 - image1 - origin_image)
    gray_image = cv2.cvtColor(change, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)
    binary_total_image = np.sum(binary_origin_image == 0)
    binary_pixel = np.sum(binary_image == 0)
    diff_percentage = binary_pixel / binary_total_image * 100
    t = t2 - t1

    with open(f"./Behavioral_data/name.txt", "r") as file:
        time = file.read()
    with open(f"./Behavioral_data/subB/Behavioral_data{time}.txt", "a", encoding="utf-8") as f:
        # 输出结果
        f.write(f"有效像素: {binary_pixel}   总像素: {binary_total_image}   百分比：{diff_percentage:.2f}%   绘图时长：{t} \n")
def calculate_pixel_difference3(origin_image, image1, image2, t1, t2, timestamp):
    x, y, width, height = 0, 50, 1920, 920
    origin_image = save_cropped_image(origin_image, x, y, width, height, timestamp)
    image1 = save_cropped_image(image1, x, y, width, height, timestamp)
    image2 = save_cropped_image(image2, x, y, width, height, timestamp)
    # 确保两幅图片的尺寸相同
    gray_origin_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    _, binary_origin_image = cv2.threshold(gray_origin_image, 0, 255, cv2.THRESH_BINARY)
    change = abs(image2 - image1 - origin_image)
    gray_image = cv2.cvtColor(change, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)
    binary_total_image = np.sum(binary_origin_image == 0)
    binary_pixel = np.sum(binary_image == 0)
    diff_percentage = binary_pixel / binary_total_image * 100
    t = t2 - t1

    with open(f"./Behavioral_data/name.txt", "r") as file:
        time = file.read()
    with open(f"./Behavioral_data/subA+B/Behavioral_data{time}.txt", "a", encoding="utf-8") as f:
        # 输出结果
        f.write(f"有效像素: {binary_pixel}   总像素: {binary_total_image}   百分比：{diff_percentage:.2f}%   绘图时长：{t} \n")