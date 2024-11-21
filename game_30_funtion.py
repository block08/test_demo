#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import pygame
import tkinter as tk
from psychopy import core
from paint_30 import random_painting, random_painting2, random_painting3
from serial_marker import serial_marker

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
# 滚轮参数
wheel_x = 50
wheel_y = 50
wheel_width = 20
wheel_height = 100
handle_height = 20
handle_y = wheel_y
# 初始化记录变量
current_value = 125
value = 0  # 滚轮数值


# 响应按键
def check_keydown_events(event):
    if event.key == pygame.K_SPACE:
        sys.exit()


globalClock = (core.Clock())
pygame.mixer.init()
click_sound = pygame.mixer.Sound("./sound/click.wav")


# 响应按键和鼠标事件
def check_events(self, stats, button1, button2, button4, numbers, paused, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11,
                 t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31,
                 timestamp1, timestamp2, timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8,
                 timestamp9, timestamp10, timestamp11, timestamp12, timestamp13, timestamp14, timestamp15, timestamp16,
                 timestamp17, timestamp18, timestamp19, timestamp20, timestamp21, timestamp22, timestamp23, timestamp24,
                 timestamp25, timestamp26, timestamp27, timestamp28, timestamp29, timestamp30):
    global this_level
    self.display_surface = pygame.display.get_surface()
    # sprite groups
    self.all_sprites = pygame.sprite.Group()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button1_clicked = button1.rect.collidepoint(mouse_x, mouse_y)
            button2_clicked = button2.rect.collidepoint(mouse_x, mouse_y)
            button4_clicked = button4.rect.collidepoint(mouse_x, mouse_y)
            if button1_clicked:
                serial_marker(bytes([0b11111111]))
                click_sound.play()
                paused = not paused
            if button2_clicked:
                click_sound.play()
                stats.game_active = True
                serial_marker(bytes([0b00000001]))
                if stats.game_score == 0:
                    serial_marker(bytes([0b00000001]))
                    t1, timestamp1 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 1:
                    serial_marker(bytes([0b00000010]))
                    t2, timestamp2 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 2:
                    serial_marker(bytes([0b00000011]))
                    t3, timestamp3 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 3:
                    serial_marker(bytes([0b00000100]))
                    t4, timestamp4 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 4:
                    serial_marker(bytes([0b00000101]))
                    t5, timestamp5 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 5:
                    serial_marker(bytes([0b00000110]))
                    t6, timestamp6 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 6:
                    serial_marker(bytes([0b00000111]))
                    t7, timestamp7 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 7:
                    serial_marker(bytes([0b00001000]))
                    t8, timestamp8 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 8:
                    serial_marker(bytes([0b00001001]))
                    t9, timestamp9 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 9:
                    serial_marker(bytes([0b00001010]))
                    t10, timestamp10 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 10:
                    serial_marker(bytes([0b00001011]))
                    t11, timestamp11 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 11:
                    serial_marker(bytes([0b00001100]))
                    t12, timestamp12 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 12:
                    serial_marker(bytes([0b00001101]))
                    t13, timestamp13 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 13:
                    serial_marker(bytes([0b00001110]))
                    t14, timestamp14 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 14:
                    serial_marker(bytes([0b00001111]))
                    t15, timestamp15 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 15:
                    serial_marker(bytes([0b00010000]))
                    t16, timestamp16 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 16:
                    serial_marker(bytes([0b00010001]))
                    t17, timestamp17 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 17:
                    serial_marker(bytes([0b00010010]))
                    t18, timestamp18 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 18:
                    serial_marker(bytes([0b00010011]))
                    t19, timestamp19 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 19:
                    serial_marker(bytes([0b00010100]))
                    t20, timestamp20 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 20:
                    serial_marker(bytes([0b00010101]))
                    t21, timestamp21 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 21:
                    serial_marker(bytes([0b00010110]))
                    t22, timestamp22 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 22:
                    serial_marker(bytes([0b00010111]))
                    t23, timestamp23 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 23:
                    serial_marker(bytes([0b00011000]))
                    t24, timestamp24 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 24:
                    serial_marker(bytes([0b00011001]))
                    t25, timestamp25 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 25:
                    serial_marker(bytes([0b00011010]))
                    t26, timestamp26 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 26:
                    serial_marker(bytes([0b00011011]))
                    t27, timestamp27 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 27:
                    serial_marker(bytes([0b00011100]))
                    t28, timestamp28 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 28:
                    serial_marker(bytes([0b00011101]))
                    t29, timestamp29 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 29:
                    serial_marker(bytes([0b00011110]))
                    t30, timestamp30 = random_painting(numbers[stats.game_score], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 30:
                    t31 = globalClock.getTime()
                    pygame.image.save(self.screen, "./output_image/post_screenshot29")
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 32:
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 33:
                    serial_marker(bytes([0b00011111]))
                    t1, timestamp1 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 34:
                    serial_marker(bytes([0b00100000]))
                    t2, timestamp2 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 35:
                    serial_marker(bytes([0b00100001]))
                    t3, timestamp3 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 36:
                    serial_marker(bytes([0b00100010]))
                    t4, timestamp4 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 37:
                    serial_marker(bytes([0b00100011]))
                    t5, timestamp5 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 38:
                    serial_marker(bytes([0b00100100]))
                    t6, timestamp6 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 39:
                    serial_marker(bytes([0b00100101]))
                    t7, timestamp7 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 40:
                    serial_marker(bytes([0b00100110]))
                    t8, timestamp8 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 41:
                    serial_marker(bytes([0b00100111]))
                    t9, timestamp9 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 42:
                    serial_marker(bytes([0b00101000]))
                    t10, timestamp10 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 43:
                    serial_marker(bytes([0b00101001]))
                    t11, timestamp11 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 44:
                    serial_marker(bytes([0b00101010]))
                    t12, timestamp12 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 45:
                    serial_marker(bytes([0b00101011]))
                    t13, timestamp13 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 46:
                    serial_marker(bytes([0b00101100]))
                    t14, timestamp14 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 47:
                    serial_marker(bytes([0b00101101]))
                    t15, timestamp15 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 48:
                    serial_marker(bytes([0b00101110]))
                    t16, timestamp16 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 49:
                    serial_marker(bytes([0b00101111]))
                    t17, timestamp17 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 50:
                    serial_marker(bytes([0b00110000]))
                    t18, timestamp18 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 51:
                    serial_marker(bytes([0b00110001]))
                    t19, timestamp19 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 52:
                    serial_marker(bytes([0b00110010]))
                    t20, timestamp20 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 53:
                    serial_marker(bytes([0b00110011]))
                    t21, timestamp21 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 54:
                    serial_marker(bytes([0b00110100]))
                    t22, timestamp22 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 55:
                    serial_marker(bytes([0b00110101]))
                    t23, timestamp23 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 56:
                    serial_marker(bytes([0b00110110]))
                    t24, timestamp24 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 57:
                    serial_marker(bytes([0b00110111]))
                    t25, timestamp25 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 58:
                    serial_marker(bytes([0b00111000]))
                    t26, timestamp26 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 59:
                    serial_marker(bytes([0b00111001]))
                    t27, timestamp27 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 60:
                    serial_marker(bytes([0b00111010]))
                    t28, timestamp28 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 61:
                    serial_marker(bytes([0b00111011]))
                    t29, timestamp29 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 62:
                    serial_marker(bytes([0b00111100]))
                    t30, timestamp30 = random_painting2(numbers[stats.game_score - 33], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 63:
                    t31 = globalClock.getTime()
                    pygame.image.save(self.screen, "./output2_image/post_screenshot29")
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 65:
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 66:
                    serial_marker(bytes([0b00111101]))
                    t1, timestamp1 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 67:
                    serial_marker(bytes([0b00111110]))
                    t2, timestamp2 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 68:
                    serial_marker(bytes([0b00111111]))
                    t3, timestamp3 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 69:
                    serial_marker(bytes([0b01000000]))
                    t4, timestamp4 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 70:
                    serial_marker(bytes([0b01000001]))
                    t5, timestamp5 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 71:
                    serial_marker(bytes([0b01000010]))
                    t6, timestamp6 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 72:
                    serial_marker(bytes([0b01000011]))
                    t7, timestamp7 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 73:
                    serial_marker(bytes([0b01000100]))
                    t8, timestamp8 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 74:
                    serial_marker(bytes([0b01000101]))
                    t9, timestamp9 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 75:
                    serial_marker(bytes([0b01000110]))
                    t10, timestamp10 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 76:
                    serial_marker(bytes([0b01000111]))
                    t11, timestamp11 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 77:
                    serial_marker(bytes([0b01001000]))
                    t12, timestamp12 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 78:
                    serial_marker(bytes([0b01001001]))
                    t13, timestamp13 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 79:
                    serial_marker(bytes([0b01001010]))
                    t14, timestamp14 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 80:
                    serial_marker(bytes([0b01001011]))
                    t15, timestamp15 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 81:
                    serial_marker(bytes([0b01001100]))
                    t16, timestamp16 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 82:
                    serial_marker(bytes([0b01001101]))
                    t17, timestamp17 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 83:
                    serial_marker(bytes([0b01001110]))
                    t18, timestamp18 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 84:
                    serial_marker(bytes([0b01001111]))
                    t19, timestamp19 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 85:
                    serial_marker(bytes([0b01010000]))
                    t20, timestamp20 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 86:
                    serial_marker(bytes([0b01010001]))
                    t21, timestamp21 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 87:
                    serial_marker(bytes([0b01010010]))
                    t22, timestamp22 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 88:
                    serial_marker(bytes([0b01010011]))
                    t23, timestamp23 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 89:
                    serial_marker(bytes([0b01010100]))
                    t24, timestamp24 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 90:
                    serial_marker(bytes([0b01010101]))
                    t25, timestamp25 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 91:
                    serial_marker(bytes([0b01010110]))
                    t26, timestamp26 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 92:
                    serial_marker(bytes([0b01010111]))
                    t27, timestamp27 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 93:
                    serial_marker(bytes([0b01011000]))
                    t28, timestamp28 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 94:
                    serial_marker(bytes([0b01011001]))
                    t29, timestamp29 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 95:
                    serial_marker(bytes([0b01011010]))
                    t30, timestamp30 = random_painting3(numbers[stats.game_score - 66], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 96:
                    t31 = globalClock.getTime()
                    pygame.image.save(self.screen, "./output3_image/post_screenshot29")
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 98:
                    stats.game_score = stats.game_score + 1



            if button4_clicked:
                click_sound.play()

                def update_label(value):
                    """更新标签显示的数值，并记录当前数值"""
                    global current_value
                    current_value = int(value)
                    label.config(text=f"当前数值: {current_value}")

                def save_value():
                    """将当前数值保存到文件"""
                    with open("scroll_value.txt", "w") as file:
                        file.write(str(current_value))
                    root.destroy()  # 关闭窗口

                # 创建主窗口
                root = tk.Tk()
                root.title("画笔速度")
                root.geometry("300x200+1110+610")

                # 创建一个标签，用于显示当前数值
                label = tk.Label(root, text=f"当前数值: {current_value}", font=("Arial", 14))
                label.pack(pady=20)

                # 创建一个滚轮（滑动条），范围为 50 到 200
                scale = tk.Scale(root, from_=50, to=200, orient=tk.HORIZONTAL, length=200, command=update_label)
                scale.set(current_value)  # 设置初始值
                scale.pack(pady=20)

                # 在窗口关闭时保存当前数值
                root.protocol("WM_DELETE_WINDOW", save_value)

                # 运行 Tkinter 主循环
                root.mainloop()
    return paused, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11,t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, timestamp1, timestamp2, timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8, timestamp9, timestamp10, timestamp11, timestamp12, timestamp13, timestamp14, timestamp15, timestamp16,                 timestamp17, timestamp18, timestamp19, timestamp20, timestamp21, timestamp22, timestamp23, timestamp24, timestamp25, timestamp26, timestamp27, timestamp28, timestamp29, timestamp30


# 更新屏幕上的图像，并切换到新屏幕
def update_screen(button):
    button.draw_button()
# 让最近绘制的屏幕可见
