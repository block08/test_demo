#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pygame.math import Vector2

# screen

TILE_SIZE = 64


# 储存所设置的类
class Settings():
    # 初始化游戏的静态属性
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1920
        self.screen_height = 1020
        self.bg_color = (230, 230, 230)
