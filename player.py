#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group):

        super().__init__(group)

        # general setup

        # 创建一个矩形来代表玩家

        # 这里的变量名一定要叫image，这是它的父类Sprite的规定

        self.image = pygame.Surface((9, 9))

        self.image.fill('green')

        # 设置坐标

        # 返回值有很多，既包含了距离也包含了大小

        # 大概有x,y,centerx,centery,width,height这六个返回值

        # 参数如果不写，默认为(0,0)，也就是把他的位置设为左上角

        # 这里参数为center = pos，也就是把他的中心放在了pos位置上

        # 这里的变量一定要取名为rect，这是它的父类Sprite的规定

        # 只有这样，才能正确调用 draw函数

        self.rect = self.image.get_rect(center=pos)

        # movement attributes

        self.direction = pygame.math.Vector2()

        self.pos = pygame.math.Vector2(self.rect.center)

        self.key_counts = {
            pygame.K_LEFT: 0,
            pygame.K_RIGHT: 0,
            pygame.K_UP: 0,
            pygame.K_DOWN: 0
        }
        with open('scroll_value.txt', 'r') as f:
            speed = str(f.read().splitlines())
        speed = speed.replace("[", "").replace("]", "").replace("'", "")
        self.speed = int(speed)
        self.status = 0

    def input(self):


        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1

        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1

        elif keys[pygame.K_RIGHT]:
            self.direction.x = +1

        else:
            self.direction.x = 0
        self.display_surface = pygame.display.get_surface()

    def input1(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1

        elif keys[pygame.K_s]:
            self.direction.y = 1

        else:

            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x = -1

        else:
            self.direction.x = 0
        self.display_surface = pygame.display.get_surface()

    def input2(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1

        elif keys[pygame.K_s]:
            self.direction.y = 1

        else:

            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:

            self.direction.x = -1

        else:
            self.direction.x = 0
        self.display_surface = pygame.display.get_surface()

    def move(self, dt):

        self.display_surface = pygame.display.get_surface()

        # normalizing a vector

        # 向量归一化，pygame提供了一个便捷的API

        if self.direction.magnitude() > 0:  # 只有按下按钮移动的时候才能调用，不然会报错

            # magnitude是返回向量的欧几里得距离

            # 向量的存储格式是[x,y],归一化的作用是让x**2 + y**2 = 1

            # 但是没有按下按钮的时候，【0，0】会使数学计算发生错误

            self.direction = self.direction.normalize()

        # horizontal movement

        # 变化的位移 = 方向 * 速度 * 变化的时间

        # 如果不*dt，就是一秒变化的距离，但实际上每一帧都在调用move函数，因此需要乘上一帧所用的时间，才是真正的位移

        self.pos.x += self.direction.x * self.speed * dt

        # rect.centerx 是中心点的x坐标，如果是rect.x就是左上角的x坐标

        self.rect.centerx = self.pos.x

        # vertical movement

        self.pos.y += self.direction.y * self.speed * dt

        self.rect.centery = self.pos.y

    def update(self, dt):

        with open('config.txt', 'r') as f:
            flag = str(f.read().splitlines())
            flag = flag.replace("[", "").replace("]", "").replace("'", "")

        if flag == '1':
            self.input()
            self.move(dt)
        elif flag == '2':
            self.input1()
            self.move(dt)
        elif flag == '3':
            self.input2()
            self.move(dt)


class EndPoint(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((50, 50))

        self.image.fill('red')

        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()

        self.pos = pygame.math.Vector2(self.rect.center)
