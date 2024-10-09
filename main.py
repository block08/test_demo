#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cv2
import pygame
import sys
import game_functions as gf
from Button import Button
from Calculate_pixel_difference import calculate_pixel_difference, calculate_pixel_difference2, \
    calculate_pixel_difference3
from Deviation_area import deviation_area1, deviation_area2, deviation_area3
from game_stats import GameStats
from level import Level
from settings import *
import random

# 设置所画图的参数
dots_time = []
green = (0, 255, 0)
black = (0, 0, 0)
grey = (128, 128, 128)


class Game:

    def __init__(self):

        # 初始化

        pygame.init()

        settings = Settings()

        stats = GameStats(settings)

        # 设置屏幕

        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        # 设置字体&字号
        self.font = pygame.font.Font('./font/STXINGKA.TTF', 40)

        # 设置标题

        pygame.display.set_caption('Examination')

        # 创建时钟，为以后得到dt使用

        self.clock = pygame.time.Clock()

        self.screen.fill('white')

        # 创建关卡对象Level,该类在level.py文件中

        self.level = Level()

    def run(self):
        global paused, t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8
        settings = Settings()
        stats = GameStats(settings)
        t1, t2, t3, t4, t5, t6, t7, t8, t9 = [None] * 9  # 初始化 t1 到 t9
        timestamp1, timestamp2, timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8 = [
                                                                                                             None] * 8  # 初始化 timestamp1 到 timestamp
        with open('config.txt', 'w') as f:
            f.truncate(0)
        with open('config.txt', 'w') as f:
            f.write('1')

        # 呈现指导语
        instruction = pygame.image.load('pic/1.jpg')
        instruction_size = instruction.get_rect()
        self.screen.blit(instruction, (instruction_size[2] / 2, instruction_size[3] / 2))
        pygame.display.update()

        wait = True
        while wait:  # 等待按键
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        wait = False
                        self.screen.fill('white')
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                    sys.exit()
        numbers = random.sample(range(1, 9), 8)
        # 被试1参与实验

        # 注视点
        self.screen.fill((255, 255, 255))
        line_length = 20  # 十字线的长度
        # 画垂直线
        pygame.draw.line(self.screen, green, (910, 540), (1010, 540), line_length)
        # 画水平线
        pygame.draw.line(self.screen, green, (960, 490), (960, 590), line_length)
        pygame.display.update()
        start_ticks = pygame.time.get_ticks()
        running = True
        countdown_time = 1
        paused = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                        sys.exit()
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            remaining_time = max(0, countdown_time - elapsed_time)
            if remaining_time == 0:
                running = False
                self.screen.fill('white')
        running1 = True
        while running1:
            # 按键检测
            for event in pygame.event.get():

                """如果按下的是右上角的红叉，就退出程序"""

                if event.type == pygame.QUIT:
                    # 退出pygame

                    pygame.quit()

                    # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错

                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                        sys.exit()

            dt = self.clock.tick(60) / 1000
            # 设置按钮
            user_button = Button(settings, self.screen, '被试A', 0, 0)
            paint_button = Button(settings, self.screen, '暂停', 0, 970)
            next_button = Button(settings, self.screen, '绘图', 860, 970)
            step_button = Button(settings, self.screen, "", 1720, 970)
            exit_button = Button(settings, self.screen, '设置速度', 1720, 0)
            mouse_pos = pygame.mouse.get_pos()
            paint_button.check_hover(mouse_pos)
            next_button.check_hover(mouse_pos)
            exit_button.check_hover(mouse_pos)

            # 按钮功能绑定
            (paused, t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3,
             timestamp4, timestamp5, timestamp6, timestamp7, timestamp8) = (
                gf.check_events(self, stats, paint_button, next_button,
                                exit_button, numbers, paused, t1, t2, t3,
                                t4, t5, t6, t7, t8, t9, timestamp1, timestamp2,
                                timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8))

            if paused:
                print(paused)
                paint_button.text = "继续"
                step_button.text = "已暂停"
                gf.update_screen(user_button)
                gf.update_screen(paint_button)
                gf.update_screen(next_button)
                gf.update_screen(exit_button)
                gf.update_screen(step_button)
                pygame.display.update()

            elif not paused:
                for i in range(1, 9):
                    if stats.game_score == i:
                        step_button.text = f"{i} / 8"
                if 0 < stats.game_score < 8:
                    next_button.text = "下一张"
                if stats.game_score == 8:
                    next_button.text = "完成"
                gf.update_screen(user_button)
                gf.update_screen(paint_button)
                gf.update_screen(next_button)
                gf.update_screen(exit_button)
                gf.update_screen(step_button)
                # 更新画面，一定要写在while循环的最后
                self.level.run(dt, stats, numbers, self.screen)

                pygame.display.update()
                if stats.game_score == 9:
                    font = pygame.font.Font('./font/STXINGKA.TTF', 100)  # 设置字体大小为100

                    # 渲染“计算中”文本
                    text_surface = font.render("计算中...", True, black)

                    # 获取文本的宽度和高度
                    text_rect = text_surface.get_rect()

                    # 计算文本在屏幕中央的位置
                    text_rect.center = (960, 540)
                    self.screen.fill('white')
                    self.screen.blit(text_surface, text_rect)
                    pygame.display.update()

                    dataloading(t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4,
                                timestamp5, timestamp6, timestamp7, timestamp8)
                    with open(f"./Behavioral_data/name.txt", "r") as file:
                        time = file.read()
                    with open(f"./Behavioral_data/subA/Behavioral_data{time}.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        data = [
                            f"图像 1  {lines[0].strip()} {lines[8].strip()}",
                            f"图像 2  {lines[1].strip()} {lines[9].strip()}",
                            f"图像 3  {lines[2].strip()} {lines[10].strip()}",
                            f"图像 4  {lines[3].strip()} {lines[11].strip()}",
                            f"图像 5  {lines[4].strip()} {lines[12].strip()}",
                            f"图像 6  {lines[5].strip()} {lines[13].strip()}",
                            f"图像 7  {lines[6].strip()} {lines[14].strip()}",
                            f"图像 8  {lines[7].strip()} {lines[15].strip()}"
                        ]
                    with open(f"./Behavioral_data/name.txt", "r") as file:
                        pass
                    self.screen.fill('white')
                    draw_data(self, self.screen, data)
                    pygame.display.update()
                    stats.game_score += 1
                if stats.game_score == 10:
                    next_button.text = "结束"
                gf.update_screen(next_button)
                if stats.game_score == 11:
                    self.screen.fill('white')
                    break

        numbers2 = random.sample(range(1, 9), 8)

        # 被试2参与实验

        self.screen.fill('white')
        # 注视点
        self.screen.fill((255, 255, 255))
        line_length = 20  # 十字线的长度
        # 画垂直线
        pygame.draw.line(self.screen, green, (910, 540), (1010, 540), line_length)
        # 画水平线
        pygame.draw.line(self.screen, green, (960, 490), (960, 590), line_length)
        pygame.display.update()
        start_ticks = pygame.time.get_ticks()
        running2 = True
        countdown_time = 2

        while running2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running2 = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                        sys.exit()
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            remaining_time = max(0, countdown_time - elapsed_time)
            if remaining_time == 0:
                running2 = False
                self.screen.fill('white')
        with open('config.txt', 'w') as f:
            f.truncate(0)
        with open('config.txt', 'w') as f:
            f.write('2')
        running3 = True
        while running3:
            # 按键检测

            for event in pygame.event.get():

                """如果按下的是右上角的红叉，就退出程序"""

                if event.type == pygame.QUIT:
                    # 退出pygame

                    pygame.quit()

                    # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错

                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                        sys.exit()

            dt = self.clock.tick(60) / 1000

            # 设置按钮
            user_button2 = Button(settings, self.screen, '被试B', 0, 0)
            paint_button2 = Button(settings, self.screen, '暂停', 0, 970)
            next_button2 = Button(settings, self.screen, '绘图', 860, 970)
            step_button2 = Button(settings, self.screen, "", 1720, 970)
            exit_button2 = Button(settings, self.screen, '设置速度', 1720, 0)
            mouse_pos = pygame.mouse.get_pos()
            paint_button2.check_hover(mouse_pos)
            next_button2.check_hover(mouse_pos)
            exit_button2.check_hover(mouse_pos)
            # 按钮功能绑定
            (paused, t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3,
             timestamp4, timestamp5, timestamp6, timestamp7, timestamp8) = (
                gf.check_events(self, stats, paint_button2, next_button2,
                                exit_button2, numbers2, paused, t1, t2, t3,
                                t4, t5, t6, t7, t8, t9, timestamp1, timestamp2,
                                timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8))

            if paused:
                print(paused)
                paint_button2.text = "继续"
                step_button2.text = "已暂停"
                gf.update_screen(user_button2)
                gf.update_screen(paint_button2)
                gf.update_screen(next_button2)
                gf.update_screen(exit_button2)
                gf.update_screen(step_button2)
                pygame.display.update()

            elif not paused:
                for i in range(1, 9):
                    if stats.game_score == i + 11:
                        step_button2.text = f"{i} / 8"
                if 11 < stats.game_score < 19:
                    next_button2.text = "下一张"
                if stats.game_score == 19:
                    next_button2.text = "完成"

                gf.update_screen(user_button2)
                gf.update_screen(paint_button2)
                gf.update_screen(next_button2)
                gf.update_screen(exit_button2)
                gf.update_screen(step_button2)
                # 更新画面，一定要写在while循环的最后
                self.level.run2(dt, stats, numbers2, self.screen)

                pygame.display.update()
                if stats.game_score == 20:
                    font = pygame.font.Font('./font/STXINGKA.TTF', 100)  # 设置字体大小为100

                    # 渲染“计算中”文本
                    text_surface = font.render("计算中...", True, black)

                    # 获取文本的宽度和高度
                    text_rect = text_surface.get_rect()

                    # 计算文本在屏幕中央的位置
                    text_rect.center = (960, 540)
                    self.screen.fill('white')
                    self.screen.blit(text_surface, text_rect)
                    pygame.display.update()

                    dataloading2(t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4,
                                timestamp5, timestamp6, timestamp7, timestamp8)
                    with open(f"./Behavioral_data/name.txt", "r") as file:
                        time = file.read()
                    with open(f"./Behavioral_data/subB/Behavioral_data{time}.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        data = [
                            f"图像 1  {lines[0].strip()} {lines[8].strip()}",
                            f"图像 2  {lines[1].strip()} {lines[9].strip()}",
                            f"图像 3  {lines[2].strip()} {lines[10].strip()}",
                            f"图像 4  {lines[3].strip()} {lines[11].strip()}",
                            f"图像 5  {lines[4].strip()} {lines[12].strip()}",
                            f"图像 6  {lines[5].strip()} {lines[13].strip()}",
                            f"图像 7  {lines[6].strip()} {lines[14].strip()}",
                            f"图像 8  {lines[7].strip()} {lines[15].strip()}"
                        ]
                    with open(f"./Behavioral_data/name.txt", "r") as file:
                        pass
                    self.screen.fill('white')
                    draw_data(self, self.screen, data)
                    pygame.display.update()
                    stats.game_score += 1
                if stats.game_score == 21:
                    next_button2.text = "结束"

                gf.update_screen(next_button2)
                if stats.game_score == 22:
                    self.screen.fill('white')
                    break



        numbers3 = random.sample(range(1, 9), 8)

        # 合作行为

        self.screen.fill('white')
        # 注视点
        self.screen.fill((255, 255, 255))
        line_length = 20  # 十字线的长度
        # 画垂直线
        pygame.draw.line(self.screen, green, (910, 540), (1010, 540), line_length)
        # 画水平线
        pygame.draw.line(self.screen, green, (960, 490), (960, 590), line_length)
        pygame.display.update()
        start_ticks = pygame.time.get_ticks()
        running4 = True
        countdown_time = 1
        while running4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running4 = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                        sys.exit()
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            remaining_time = max(0, countdown_time - elapsed_time)
            if remaining_time == 0:
                running4 = False
                self.screen.fill('white')
        with open('config.txt', 'w') as f:
            f.truncate(0)
        with open('config.txt', 'w') as f:
            f.write('3')
        running5 = True
        while running5:
            # 按键检测

            for event in pygame.event.get():

                """如果按下的是右上角的红叉，就退出程序"""

                if event.type == pygame.QUIT:
                    # 退出pygame

                    pygame.quit()

                    # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错

                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                        sys.exit()

            dt = self.clock.tick(60) / 1000
            # 设置按钮

            # 设置按钮
            user_button3 = Button(settings, self.screen, '被试A+B', 0, 0)
            paint_button3 = Button(settings, self.screen, '暂停', 0, 970)
            next_button3 = Button(settings, self.screen, '绘图', 860, 970)
            step_button3 = Button(settings, self.screen, "", 1720, 970)
            exit_button3 = Button(settings, self.screen, '设置速度', 1720, 0)
            mouse_pos = pygame.mouse.get_pos()
            paint_button3.check_hover(mouse_pos)
            next_button3.check_hover(mouse_pos)
            exit_button3.check_hover(mouse_pos)
            # 按钮功能绑定
            (paused, t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3,
             timestamp4, timestamp5, timestamp6, timestamp7, timestamp8) = (
                gf.check_events(self, stats, paint_button3, next_button3,
                                exit_button3, numbers3, paused, t1, t2, t3,
                                t4, t5, t6, t7, t8, t9, timestamp1, timestamp2,
                                timestamp3, timestamp4, timestamp5, timestamp6, timestamp7, timestamp8))

            if paused:
                paint_button3.text = "继续"
                step_button3.text = "已暂停"
                gf.update_screen(user_button3)
                gf.update_screen(paint_button3)
                gf.update_screen(next_button3)
                gf.update_screen(exit_button3)
                gf.update_screen(step_button3)
                pygame.display.update()

            elif not paused:
                for i in range(1, 9):
                    if stats.game_score == i + 22:
                        step_button3.text = f"{i} / 8"
                if 22 < stats.game_score < 30:
                    next_button3.text = "下一张"
                if stats.game_score == 30:
                    next_button3.text = "完成"

                gf.update_screen(user_button3)
                gf.update_screen(paint_button3)
                gf.update_screen(next_button3)
                gf.update_screen(exit_button3)
                gf.update_screen(step_button3)
                # 更新画面，一定要写在while循环的最后
                self.level.run3(dt, stats, numbers3, self.screen)
                pygame.display.update()

                if stats.game_score == 31:
                    font = pygame.font.Font('./font/STXINGKA.TTF', 100)  # 设置字体大小为100

                    # 渲染“计算中”文本
                    text_surface = font.render("计算中...", True, black)

                    # 获取文本的宽度和高度
                    text_rect = text_surface.get_rect()

                    # 计算文本在屏幕中央的位置
                    text_rect.center = (960, 540)
                    self.screen.fill('white')
                    self.screen.blit(text_surface, text_rect)
                    pygame.display.update()

                    dataloading3(t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4,
                                 timestamp5, timestamp6, timestamp7, timestamp8)
                    with open(f"./Behavioral_data/name.txt", "r") as file:
                        time = file.read()
                    with open(f"./Behavioral_data/subA+B/Behavioral_data{time}.txt", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        data = [
                            f"图像 1  {lines[0].strip()} {lines[8].strip()}",
                            f"图像 2  {lines[1].strip()} {lines[9].strip()}",
                            f"图像 3  {lines[2].strip()} {lines[10].strip()}",
                            f"图像 4  {lines[3].strip()} {lines[11].strip()}",
                            f"图像 5  {lines[4].strip()} {lines[12].strip()}",
                            f"图像 6  {lines[5].strip()} {lines[13].strip()}",
                            f"图像 7  {lines[6].strip()} {lines[14].strip()}",
                            f"图像 8  {lines[7].strip()} {lines[15].strip()}"
                        ]
                    with open(f"./Behavioral_data/name.txt", "r") as file:
                        pass
                    self.screen.fill('white')
                    draw_data(self, self.screen, data)
                    pygame.display.update()
                    stats.game_score += 1
                if stats.game_score == 32:
                    next_button3.text = "结束"
                    

                gf.update_screen(next_button3)
                if stats.game_score == 33:
                    self.screen.fill('white')
                    break
        self.screen.fill('white')
        instruction = pygame.image.load('pic/2.jpg')
        instruction_size = instruction.get_rect()
        self.screen.blit(instruction, (instruction_size[2] / 2, instruction_size[3] / 2))
        pygame.display.update()
        wait = True
        while wait:  # 等待按键
            exit_button = Button(settings, self.screen, '退出', 1720, 0)
            gf.update_screen(exit_button)
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.QUIT:
                    pygame.quit()

                    # 退出python程序，不捕获异常,不加上这一句也能退出，但是会在中断报错
                    sys.exit()
def draw_data(self, screen, data):
    # 逐行绘制数据
    for i, text in enumerate(data):
        font = pygame.font.SysFont('Arial', 50)
        # 渲染文本
        data_surface = self.font.render(text, True, black)
        # 绘制文本到屏幕上，x = 50, y = 50 + 40 * i
        screen.blit(data_surface, (50, 50 + i * 100))



def dataloading(t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4, timestamp5,
                timestamp6, timestamp7, timestamp8):
    image = cv2.imread('./output_image/post_screenshot-1.png')
    image1 = cv2.imread('./output_image/pre_screenshot0.png')
    image1_1 = cv2.imread('./output_image/post_screenshot0.png')
    image2 = cv2.imread('./output_image/pre_screenshot1.png')
    image2_1 = cv2.imread('./output_image/post_screenshot1.png')
    image3 = cv2.imread('./output_image/pre_screenshot2.png')
    image3_1 = cv2.imread('./output_image/post_screenshot2.png')
    image4 = cv2.imread('./output_image/pre_screenshot3.png')
    image4_1 = cv2.imread('./output_image/post_screenshot3.png')
    image5 = cv2.imread('./output_image/pre_screenshot4.png')
    image5_1 = cv2.imread('./output_image/post_screenshot4.png')
    image6 = cv2.imread('./output_image/pre_screenshot5.png')
    image6_1 = cv2.imread('./output_image/post_screenshot5.png')
    image7 = cv2.imread('./output_image/pre_screenshot6.png')
    image7_1 = cv2.imread('./output_image/post_screenshot6.png')
    image8 = cv2.imread('./output_image/pre_screenshot7.png')
    image8_1 = cv2.imread('./output_image/post_screenshot7.png')
    calculate_pixel_difference(image, image1, image1_1, t1, t2, timestamp1)
    calculate_pixel_difference(image, image2, image2_1, t2, t3, timestamp2)
    calculate_pixel_difference(image, image3, image3_1, t3, t4, timestamp3)
    calculate_pixel_difference(image, image4, image4_1, t4, t5, timestamp4)
    calculate_pixel_difference(image, image5, image5_1, t5, t6, timestamp5)
    calculate_pixel_difference(image, image6, image6_1, t6, t7, timestamp6)
    calculate_pixel_difference(image, image7, image7_1, t7, t8, timestamp7)
    calculate_pixel_difference(image, image8, image8_1, t8, t9, timestamp8)
    pygameimage1 = cv2.imread('./output_image/post_screenshot0.png')
    pygameimage2 = cv2.imread('./output_image/post_screenshot1.png')
    pygameimage3 = cv2.imread('./output_image/post_screenshot2.png')
    pygameimage4 = cv2.imread('./output_image/post_screenshot3.png')
    pygameimage5 = cv2.imread('./output_image/post_screenshot4.png')
    pygameimage6 = cv2.imread('./output_image/post_screenshot5.png')
    pygameimage7 = cv2.imread('./output_image/post_screenshot6.png')
    pygameimage8 = cv2.imread('./output_image/post_screenshot7.png')
    deviation_area1(pygameimage1)
    deviation_area1(pygameimage2)
    deviation_area1(pygameimage3)
    deviation_area1(pygameimage4)
    deviation_area1(pygameimage5)
    deviation_area1(pygameimage6)
    deviation_area1(pygameimage7)
    deviation_area1(pygameimage8)


def dataloading2(t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4, timestamp5,
                 timestamp6, timestamp7, timestamp8):
    image = cv2.imread('./output2_image/post_screenshot-1.png')
    image1 = cv2.imread('./output2_image/pre_screenshot0.png')
    image1_1 = cv2.imread('./output2_image/post_screenshot0.png')
    image2 = cv2.imread('./output2_image/pre_screenshot1.png')
    image2_1 = cv2.imread('./output2_image/post_screenshot1.png')
    image3 = cv2.imread('./output2_image/pre_screenshot2.png')
    image3_1 = cv2.imread('./output2_image/post_screenshot2.png')
    image4 = cv2.imread('./output2_image/pre_screenshot3.png')
    image4_1 = cv2.imread('./output2_image/post_screenshot3.png')
    image5 = cv2.imread('./output2_image/pre_screenshot4.png')
    image5_1 = cv2.imread('./output2_image/post_screenshot4.png')
    image6 = cv2.imread('./output2_image/pre_screenshot5.png')
    image6_1 = cv2.imread('./output2_image/post_screenshot5.png')
    image7 = cv2.imread('./output2_image/pre_screenshot6.png')
    image7_1 = cv2.imread('./output2_image/post_screenshot6.png')
    image8 = cv2.imread('./output2_image/pre_screenshot7.png')
    image8_1 = cv2.imread('./output2_image/post_screenshot7.png')
    calculate_pixel_difference2(image, image1, image1_1, t1, t2, timestamp1)
    calculate_pixel_difference2(image, image2, image2_1, t2, t3, timestamp2)
    calculate_pixel_difference2(image, image3, image3_1, t3, t4, timestamp3)
    calculate_pixel_difference2(image, image4, image4_1, t4, t5, timestamp4)
    calculate_pixel_difference2(image, image5, image5_1, t5, t6, timestamp5)
    calculate_pixel_difference2(image, image6, image6_1, t6, t7, timestamp6)
    calculate_pixel_difference2(image, image7, image7_1, t7, t8, timestamp7)
    calculate_pixel_difference2(image, image8, image8_1, t8, t9, timestamp8)
    pygameimage1 = cv2.imread('./output2_image/post_screenshot0.png')
    pygameimage2 = cv2.imread('./output2_image/post_screenshot1.png')
    pygameimage3 = cv2.imread('./output2_image/post_screenshot2.png')
    pygameimage4 = cv2.imread('./output2_image/post_screenshot3.png')
    pygameimage5 = cv2.imread('./output2_image/post_screenshot4.png')
    pygameimage6 = cv2.imread('./output2_image/post_screenshot5.png')
    pygameimage7 = cv2.imread('./output2_image/post_screenshot6.png')
    pygameimage8 = cv2.imread('./output2_image/post_screenshot7.png')
    deviation_area2(pygameimage1)
    deviation_area2(pygameimage2)
    deviation_area2(pygameimage3)
    deviation_area2(pygameimage4)
    deviation_area2(pygameimage5)
    deviation_area2(pygameimage6)
    deviation_area2(pygameimage7)
    deviation_area2(pygameimage8)


def dataloading3(t1, t2, t3, t4, t5, t6, t7, t8, t9, timestamp1, timestamp2, timestamp3, timestamp4, timestamp5,
                timestamp6, timestamp7, timestamp8):
    image = cv2.imread('./output3_image/post_screenshot-1.png')
    image1 = cv2.imread('./output3_image/pre_screenshot0.png')
    image1_1 = cv2.imread('./output3_image/post_screenshot0.png')
    image2 = cv2.imread('./output3_image/pre_screenshot1.png')
    image2_1 = cv2.imread('./output3_image/post_screenshot1.png')
    image3 = cv2.imread('./output3_image/pre_screenshot2.png')
    image3_1 = cv2.imread('./output3_image/post_screenshot2.png')
    image4 = cv2.imread('./output3_image/pre_screenshot3.png')
    image4_1 = cv2.imread('./output3_image/post_screenshot3.png')
    image5 = cv2.imread('./output3_image/pre_screenshot4.png')
    image5_1 = cv2.imread('./output3_image/post_screenshot4.png')
    image6 = cv2.imread('./output3_image/pre_screenshot5.png')
    image6_1 = cv2.imread('./output3_image/post_screenshot5.png')
    image7 = cv2.imread('./output3_image/pre_screenshot6.png')
    image7_1 = cv2.imread('./output3_image/post_screenshot6.png')
    image8 = cv2.imread('./output3_image/pre_screenshot7.png')
    image8_1 = cv2.imread('./output3_image/post_screenshot7.png')
    calculate_pixel_difference3(image, image1, image1_1, t1, t2, timestamp1)
    calculate_pixel_difference3(image, image2, image2_1, t2, t3, timestamp2)
    calculate_pixel_difference3(image, image3, image3_1, t3, t4, timestamp3)
    calculate_pixel_difference3(image, image4, image4_1, t4, t5, timestamp4)
    calculate_pixel_difference3(image, image5, image5_1, t5, t6, timestamp5)
    calculate_pixel_difference3(image, image6, image6_1, t6, t7, timestamp6)
    calculate_pixel_difference3(image, image7, image7_1, t7, t8, timestamp7)
    calculate_pixel_difference3(image, image8, image8_1, t8, t9, timestamp8)
    pygameimage1 = cv2.imread('./output3_image/post_screenshot0.png')
    pygameimage2 = cv2.imread('./output3_image/post_screenshot1.png')
    pygameimage3 = cv2.imread('./output3_image/post_screenshot2.png')
    pygameimage4 = cv2.imread('./output3_image/post_screenshot3.png')
    pygameimage5 = cv2.imread('./output3_image/post_screenshot4.png')
    pygameimage6 = cv2.imread('./output3_image/post_screenshot5.png')
    pygameimage7 = cv2.imread('./output3_image/post_screenshot6.png')
    pygameimage8 = cv2.imread('./output3_image/post_screenshot7.png')
    deviation_area3(pygameimage1)
    deviation_area3(pygameimage2)
    deviation_area3(pygameimage3)
    deviation_area3(pygameimage4)
    deviation_area3(pygameimage5)
    deviation_area3(pygameimage6)
    deviation_area3(pygameimage7)
    deviation_area3(pygameimage8)


if __name__ == '__main__':
    game = Game()
    game.run()
