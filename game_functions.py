#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import pygame
import tkinter as tk
from psychopy import core

from paint import random_painting, random_painting2, random_painting3
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
def check_events(self, stats, button1, button2, button4, numbers, paused, t1, t2, t3, t4, t5, t6, t7, t8, t9,
                 timestamp1, timestamp2, timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8):
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

                    t9 = globalClock.getTime()
                    pygame.image.save(self.screen, "./output_image/post_screenshot7.png")
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 10:
                    serial_marker(bytes([0b00001010]))
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 11:
                    serial_marker(bytes([0b00001011]))
                    t1, timestamp1 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 12:
                    serial_marker(bytes([0b00001100]))
                    t2, timestamp2 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 13:
                    serial_marker(bytes([0b00001101]))
                    t3, timestamp3 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 14:
                    serial_marker(bytes([0b00001110]))
                    t4, timestamp4 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 15:
                    serial_marker(bytes([0b00001111]))
                    t5, timestamp5 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 16:
                    serial_marker(bytes([0b00010000]))
                    t6, timestamp6 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 17:
                    serial_marker(bytes([0b00010001]))
                    t7, timestamp7 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 18:
                    serial_marker(bytes([0b00010010]))
                    t8, timestamp8 = random_painting2(numbers[stats.game_score - 11], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 19:
                    serial_marker(bytes([0b00010011]))
                    t9 = globalClock.getTime()
                    pygame.image.save(self.screen, "./output2_image/post_screenshot7.png")
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 21:
                    serial_marker(bytes([0b00010100]))
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 22:
                    serial_marker(bytes([0b00010101]))
                    t1, timestamp1 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 23:
                    serial_marker(bytes([0b00010110]))
                    t2, timestamp2 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 24:
                    serial_marker(bytes([0b00010111]))
                    t3, timestamp3 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 25:
                    serial_marker(bytes([0b00011000]))
                    t4, timestamp4 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 26:
                    serial_marker(bytes([0b00011001]))
                    t5, timestamp5 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 27:
                    serial_marker(bytes([0b00011010]))
                    t6, timestamp6 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 28:
                    serial_marker(bytes([0b00011011]))
                    t7, timestamp7 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 29:
                    serial_marker(bytes([0b00011100]))
                    t8, timestamp8 = random_painting3(numbers[stats.game_score - 22], self, stats.game_score)
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 30:
                    serial_marker(bytes([0b00011101]))
                    t9 = globalClock.getTime()
                    pygame.image.save(self.screen, "./output3_image/post_screenshot7.png")
                    stats.game_score = stats.game_score + 1
                elif stats.game_score == 32:
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
    return paused, t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8


# 更新屏幕上的图像，并切换到新屏幕
def update_screen(button):
    button.draw_button()
# 让最近绘制的屏幕可见
