import cv2
import numpy as np
def deviation_area1(image):
    # 读取图像

    x, y, width, height = 0, 50, 1920, 920
    # 裁剪图像
    image = image[y:y + height, x:x + width]

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 创建掩码，提取绿色区域
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    # 定义红色的HSV范围（注意红色在HSV中有两个范围）
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    # 检测黑色线条
    _, black_mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    # 合并绿色和黑色的掩码
    combined_mask = cv2.bitwise_or(green_mask, red_mask)
    combined_mask = cv2.bitwise_or(combined_mask, black_mask)


    # 查找轮廓
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # 遍历所有轮廓
    for i, contour in enumerate(contours):
        # 创建一个掩码，用于将封闭区域从原始图像中分离出来
        mask = np.zeros_like(combined_mask)
        cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)

        # 使用掩码提取封闭区域
        extracted_image = cv2.bitwise_and(image, image, mask=mask)

        # 提取轮廓的最小矩形区域
        x, y, w, h = cv2.boundingRect(contour)

        # 裁剪出封闭区域（仅裁剪轮廓内的部分，而不是整个矩形）
        cropped_image = extracted_image[y:y + h, x:x + w]

    # 将图像转换为HSV色彩空间
    hsv_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)

    # 定义白色的HSV范围
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])

    # 创建掩码，提取白色区域
    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

    # 计算白色像素的数量
    white_pixel_count = np.sum(white_mask > 0)

    # 输出白色像素的数量
    print(f"白色像素的数量: {white_pixel_count}")

    with open(f"./Behavioral_data/name.txt", "r") as file:
        time = file.read()
    with open(f"./Behavioral_data/subA/Behavioral_data{time}.txt", "a", encoding="utf-8") as f:
        # 输出结果
        f.write(f"偏差像素个数 : {white_pixel_count}\n")


def deviation_area2(image):
    x, y, width, height = 0, 50, 1920, 920
    # 裁剪图像
    image = image[y:y + height, x:x + width]

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 创建掩码，提取绿色区域
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    # 定义红色的HSV范围（注意红色在HSV中有两个范围）
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    # 检测黑色线条
    _, black_mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    # 合并绿色和黑色的掩码
    combined_mask = cv2.bitwise_or(green_mask, red_mask)
    combined_mask = cv2.bitwise_or(combined_mask, black_mask)

    # 查找轮廓
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历所有轮廓
    for i, contour in enumerate(contours):
        # 创建一个掩码，用于将封闭区域从原始图像中分离出来
        mask = np.zeros_like(combined_mask)
        cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)

        # 使用掩码提取封闭区域
        extracted_image = cv2.bitwise_and(image, image, mask=mask)

        # 提取轮廓的最小矩形区域
        x, y, w, h = cv2.boundingRect(contour)

        # 裁剪出封闭区域（仅裁剪轮廓内的部分，而不是整个矩形）
        cropped_image = extracted_image[y:y + h, x:x + w]

    # 将图像转换为HSV色彩空间
    hsv_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)

    # 定义白色的HSV范围
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])

    # 创建掩码，提取白色区域
    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

    # 计算白色像素的数量
    white_pixel_count = np.sum(white_mask > 0)

    # 输出白色像素的数量
    print(f"白色像素的数量: {white_pixel_count}")

    with open(f"./Behavioral_data/name.txt", "r") as file:
        time = file.read()
    with open(f"./Behavioral_data/subB/Behavioral_data{time}.txt", "a", encoding="utf-8") as f:
        # 输出结果
        f.write(f"偏差像素个数 : {white_pixel_count}\n")

def deviation_area3(image):
    # 读取图像
    x, y, width, height = 0, 50, 1920, 920
    # 裁剪图像
    image = image[y:y + height, x:x + width]

    # 将图像转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 创建掩码，提取绿色区域
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
    # 定义红色的HSV范围（注意红色在HSV中有两个范围）
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    # 检测黑色线条
    _, black_mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    # 合并绿色和黑色的掩码
    combined_mask = cv2.bitwise_or(green_mask, red_mask)
    combined_mask = cv2.bitwise_or(combined_mask, black_mask)


    # 查找轮廓
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # 遍历所有轮廓
    for i, contour in enumerate(contours):
        # 创建一个掩码，用于将封闭区域从原始图像中分离出来
        mask = np.zeros_like(combined_mask)
        cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)

        # 使用掩码提取封闭区域
        extracted_image = cv2.bitwise_and(image, image, mask=mask)

        # 提取轮廓的最小矩形区域
        x, y, w, h = cv2.boundingRect(contour)

        # 裁剪出封闭区域（仅裁剪轮廓内的部分，而不是整个矩形）
        cropped_image = extracted_image[y:y + h, x:x + w]

    # 将图像转换为HSV色彩空间
    hsv_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)

    # 定义白色的HSV范围
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])

    # 创建掩码，提取白色区域
    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

    # 计算白色像素的数量
    white_pixel_count = np.sum(white_mask > 0)

    # 输出白色像素的数量
    print(f"白色像素的数量: {white_pixel_count}")

    with open(f"./Behavioral_data/name.txt", "r") as file:
        time = file.read()
    with open(f"./Behavioral_data/subA+B/Behavioral_data{time}.txt", "a", encoding="utf-8") as f:
        # 输出结果
        f.write(f"偏差像素个数 : {white_pixel_count}\n")

