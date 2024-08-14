import random

import pygame
from psychopy import core

from level import Level
import time

globalClock = (core.Clock())

global t, timestamp

def case_1(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup0(160, 540)
    self.level.setup_endpoint0(1760, 540)
    return t, timestamp


def case_2(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawrect(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup1(560, 340)
    self.level.setup_endpoint1(560, 350)
    return t, timestamp


def case_3(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline2(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup2(960, 540)
    self.level.setup_endpoint2(300, 400)
    return t, timestamp


def case_4(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines1(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup3(1000, 500)
    self.level.setup_endpoint3(100, 150)
    return t, timestamp


def case_5(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines2(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup4(100, 100)
    self.level.setup_endpoint4(1500, 900)
    return t, timestamp


def case_6(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline_1(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup5(960, 100)
    self.level.setup_endpoint5(960, 900)
    return t, timestamp


def case_7(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t= globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines3(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup6(160, 160)
    self.level.setup_endpoint6(920, 920)
    return t, timestamp


def case_8(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup7(160, 160)
    self.level.setup_endpoint7(920, 920)
    return t, timestamp

def case2_1(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup0(160, 540)
    self.level.setup_endpoint0(1760, 540)
    return t, timestamp


def case2_2(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawrect(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup1(560, 340)
    self.level.setup_endpoint1(560, 350)
    return t, timestamp


def case2_3(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline2(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup2(960, 540)
    self.level.setup_endpoint2(300, 400)
    return t, timestamp


def case2_4(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines1(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup3(1000, 500)
    self.level.setup_endpoint3(100, 150)
    return t, timestamp


def case2_5(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines2(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup4(100, 100)
    self.level.setup_endpoint4(1500, 900)
    return t, timestamp


def case2_6(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline_1(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup5(960, 100)
    self.level.setup_endpoint5(960, 900)
    return t, timestamp


def case2_7(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t= globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines3(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup6(160, 160)
    self.level.setup_endpoint6(920, 920)
    return t, timestamp


def case2_8(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup7(160, 160)
    self.level.setup_endpoint7(920, 920)
    return t, timestamp
def case3_1(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup0(160, 540)
    self.level.setup_endpoint0(1760, 540)
    return t, timestamp


def case3_2(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawrect(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup1(560, 340)
    self.level.setup_endpoint1(560, 350)
    return t, timestamp


def case3_3(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline2(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup2(960, 540)
    self.level.setup_endpoint2(300, 400)
    return t, timestamp


def case3_4(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines1(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup3(1000, 500)
    self.level.setup_endpoint3(100, 150)
    return t, timestamp


def case3_5(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines2(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup4(100, 100)
    self.level.setup_endpoint4(1500, 900)
    return t, timestamp


def case3_6(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline_1(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup5(960, 100)
    self.level.setup_endpoint5(960, 900)
    return t, timestamp


def case3_7(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t= globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines3(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup6(160, 160)
    self.level.setup_endpoint6(920, 920)
    return t, timestamp


def case3_8(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup7(160, 160)
    self.level.setup_endpoint7(920, 920)
    return t, timestamp





def random_painting(number, self, gamescore):
    global t, timestamp
    if gamescore == 0:
        if number == 1:
            t,timestamp = case_1(self, gamescore)
        elif number == 2:
            t,timestamp = case_2(self, gamescore)
        elif number == 3:
            t,timestamp = case_3(self, gamescore)
        elif number == 4:
            t,timestamp = case_4(self, gamescore)
        elif number == 5:
            t,timestamp = case_5(self, gamescore)
        elif number == 6:
            t,timestamp = case_6(self, gamescore)
        elif number == 7:
            t,timestamp = case_7(self, gamescore)
        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
    elif gamescore == 1:
        if number == 1:
            t,timestamp = case_1(self, gamescore)

        elif number == 2:
            t,timestamp = case_2(self, gamescore)

        elif number == 3:
            t,timestamp = case_3(self, gamescore)

        elif number == 4:
            t,timestamp = case_4(self, gamescore)

        elif number == 5:
            t,timestamp = case_5(self, gamescore)

        elif number == 6:
            t,timestamp = case_6(self, gamescore)

        elif number == 7:
            t,timestamp = case_7(self, gamescore)

        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
    elif gamescore == 2:
        if number == 1:
            t,timestamp = case_1(self, gamescore)

        elif number == 2:
            t,timestamp = case_2(self, gamescore)

        elif number == 3:
            t,timestamp = case_3(self, gamescore)

        elif number == 4:
            t,timestamp = case_4(self, gamescore)

        elif number == 5:
            t,timestamp = case_5(self, gamescore)

        elif number == 6:
            t,timestamp = case_6(self, gamescore)

        elif number == 7:
            t,timestamp = case_7(self, gamescore)

        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
    elif gamescore == 3:
        if number == 1:
            t,timestamp = case_1(self, gamescore)

        elif number == 2:
            t,timestamp = case_2(self, gamescore)

        elif number == 3:
            t,timestamp = case_3(self, gamescore)

        elif number == 4:
            t,timestamp = case_4(self, gamescore)

        elif number == 5:
            t,timestamp = case_5(self, gamescore)

        elif number == 6:
            t,timestamp = case_6(self, gamescore)

        elif number == 7:
            t,timestamp = case_7(self, gamescore)

        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
    elif gamescore == 4:
        if number == 1:
            t,timestamp = case_1(self, gamescore)

        elif number == 2:
            t,timestamp = case_2(self, gamescore)

        elif number == 3:
            t,timestamp = case_3(self, gamescore)

        elif number == 4:
            t,timestamp = case_4(self, gamescore)

        elif number == 5:
            t,timestamp = case_5(self, gamescore)

        elif number == 6:
            t,timestamp = case_6(self, gamescore)

        elif number == 7:
            t,timestamp = case_7(self, gamescore)

        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
    elif gamescore == 5:
        if number == 1:
            t,timestamp = case_1(self, gamescore)

        elif number == 2:
            t,timestamp = case_2(self, gamescore)

        elif number == 3:
            t,timestamp = case_3(self, gamescore)

        elif number == 4:
            t,timestamp = case_4(self, gamescore)

        elif number == 5:
            t,timestamp = case_5(self, gamescore)

        elif number == 6:
            t,timestamp = case_6(self, gamescore)

        elif number == 7:
            t,timestamp = case_7(self, gamescore)

        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
    elif gamescore == 6:
        if number == 1:
            t,timestamp = case_1(self, gamescore)

        elif number == 2:
            t,timestamp = case_2(self, gamescore)

        elif number == 3:
            t,timestamp = case_3(self, gamescore)

        elif number == 4:
            t,timestamp = case_4(self, gamescore)

        elif number == 5:
            t,timestamp = case_5(self, gamescore)

        elif number == 6:
            t,timestamp = case_6(self, gamescore)

        elif number == 7:
            t,timestamp = case_7(self, gamescore)

        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
    elif gamescore == 7:
        if number == 1:
            t,timestamp = case_1(self, gamescore)

        elif number == 2:
            t,timestamp = case_2(self, gamescore)

        elif number == 3:
            t,timestamp = case_3(self, gamescore)

        elif number == 4:
            t,timestamp = case_4(self, gamescore)

        elif number == 5:
            t,timestamp = case_5(self, gamescore)

        elif number == 6:
            t,timestamp = case_6(self, gamescore)

        elif number == 7:
            t,timestamp = case_7(self, gamescore)

        elif number == 8:
            t,timestamp = case_8(self, gamescore)
        return t, timestamp
def random_painting2(number, self, gamescore):
    global t, timestamp
    gamescore = gamescore - 11
    if gamescore == 0:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)
        elif number == 2:
            t,timestamp = case2_2(self, gamescore)
        elif number == 3:
            t,timestamp = case2_3(self, gamescore)
        elif number == 4:
            t,timestamp = case2_4(self, gamescore)
        elif number == 5:
            t,timestamp = case2_5(self, gamescore)
        elif number == 6:
            t,timestamp = case2_6(self, gamescore)
        elif number == 7:
            t,timestamp = case2_7(self, gamescore)
        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
    elif gamescore == 1:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)

        elif number == 2:
            t,timestamp = case2_2(self, gamescore)

        elif number == 3:
            t,timestamp = case2_3(self, gamescore)

        elif number == 4:
            t,timestamp = case2_4(self, gamescore)

        elif number == 5:
            t,timestamp = case2_5(self, gamescore)

        elif number == 6:
            t,timestamp = case2_6(self, gamescore)

        elif number == 7:
            t,timestamp = case2_7(self, gamescore)

        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
    elif gamescore == 2:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)

        elif number == 2:
            t,timestamp = case2_2(self, gamescore)

        elif number == 3:
            t,timestamp = case2_3(self, gamescore)

        elif number == 4:
            t,timestamp = case2_4(self, gamescore)

        elif number == 5:
            t,timestamp = case2_5(self, gamescore)

        elif number == 6:
            t,timestamp = case2_6(self, gamescore)

        elif number == 7:
            t,timestamp = case2_7(self, gamescore)

        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
    elif gamescore == 3:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)

        elif number == 2:
            t,timestamp = case2_2(self, gamescore)

        elif number == 3:
            t,timestamp = case2_3(self, gamescore)

        elif number == 4:
            t,timestamp = case2_4(self, gamescore)

        elif number == 5:
            t,timestamp = case2_5(self, gamescore)

        elif number == 6:
            t,timestamp = case2_6(self, gamescore)

        elif number == 7:
            t,timestamp = case2_7(self, gamescore)

        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
    elif gamescore == 4:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)

        elif number == 2:
            t,timestamp = case2_2(self, gamescore)

        elif number == 3:
            t,timestamp = case2_3(self, gamescore)

        elif number == 4:
            t,timestamp = case2_4(self, gamescore)

        elif number == 5:
            t,timestamp = case2_5(self, gamescore)

        elif number == 6:
            t,timestamp = case2_6(self, gamescore)

        elif number == 7:
            t,timestamp = case2_7(self, gamescore)

        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
    elif gamescore == 5:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)

        elif number == 2:
            t,timestamp = case2_2(self, gamescore)

        elif number == 3:
            t,timestamp = case2_3(self, gamescore)

        elif number == 4:
            t,timestamp = case2_4(self, gamescore)

        elif number == 5:
            t,timestamp = case2_5(self, gamescore)

        elif number == 6:
            t,timestamp = case2_6(self, gamescore)

        elif number == 7:
            t,timestamp = case2_7(self, gamescore)

        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
    elif gamescore == 6:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)

        elif number == 2:
            t,timestamp = case2_2(self, gamescore)

        elif number == 3:
            t,timestamp = case2_3(self, gamescore)

        elif number == 4:
            t,timestamp = case2_4(self, gamescore)

        elif number == 5:
            t,timestamp = case2_5(self, gamescore)

        elif number == 6:
            t,timestamp = case2_6(self, gamescore)

        elif number == 7:
            t,timestamp = case2_7(self, gamescore)

        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
    elif gamescore == 7:
        if number == 1:
            t,timestamp = case2_1(self, gamescore)

        elif number == 2:
            t,timestamp = case2_2(self, gamescore)

        elif number == 3:
            t,timestamp = case2_3(self, gamescore)

        elif number == 4:
            t,timestamp = case2_4(self, gamescore)

        elif number == 5:
            t,timestamp = case2_5(self, gamescore)

        elif number == 6:
            t,timestamp = case2_6(self, gamescore)

        elif number == 7:
            t,timestamp = case2_7(self, gamescore)

        elif number == 8:
            t,timestamp = case2_8(self, gamescore)
        return t, timestamp
def random_painting3(number, self, gamescore):
    global t, timestamp
    gamescore = gamescore - 22
    if gamescore == 0:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)
        elif number == 2:
            t,timestamp = case3_2(self, gamescore)
        elif number == 3:
            t,timestamp = case3_3(self, gamescore)
        elif number == 4:
            t,timestamp = case3_4(self, gamescore)
        elif number == 5:
            t,timestamp = case3_5(self, gamescore)
        elif number == 6:
            t,timestamp = case3_6(self, gamescore)
        elif number == 7:
            t,timestamp = case3_7(self, gamescore)
        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp
    elif gamescore == 1:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)

        elif number == 2:
            t,timestamp = case3_2(self, gamescore)

        elif number == 3:
            t,timestamp = case3_3(self, gamescore)

        elif number == 4:
            t,timestamp = case3_4(self, gamescore)

        elif number == 5:
            t,timestamp = case3_5(self, gamescore)

        elif number == 6:
            t,timestamp = case3_6(self, gamescore)

        elif number == 7:
            t,timestamp = case3_7(self, gamescore)

        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp
    elif gamescore == 2:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)

        elif number == 2:
            t,timestamp = case3_2(self, gamescore)

        elif number == 3:
            t,timestamp = case3_3(self, gamescore)

        elif number == 4:
            t,timestamp = case3_4(self, gamescore)

        elif number == 5:
            t,timestamp = case3_5(self, gamescore)

        elif number == 6:
            t,timestamp = case3_6(self, gamescore)

        elif number == 7:
            t,timestamp = case3_7(self, gamescore)

        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp
    elif gamescore == 3:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)

        elif number == 2:
            t,timestamp = case3_2(self, gamescore)

        elif number == 3:
            t,timestamp = case3_3(self, gamescore)

        elif number == 4:
            t,timestamp = case3_4(self, gamescore)

        elif number == 5:
            t,timestamp = case3_5(self, gamescore)

        elif number == 6:
            t,timestamp = case3_6(self, gamescore)

        elif number == 7:
            t,timestamp = case3_7(self, gamescore)

        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp
    elif gamescore == 4:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)

        elif number == 2:
            t,timestamp = case3_2(self, gamescore)

        elif number == 3:
            t,timestamp = case3_3(self, gamescore)

        elif number == 4:
            t,timestamp = case3_4(self, gamescore)

        elif number == 5:
            t,timestamp = case3_5(self, gamescore)

        elif number == 6:
            t,timestamp = case3_6(self, gamescore)

        elif number == 7:
            t,timestamp = case3_7(self, gamescore)

        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp
    elif gamescore == 5:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)

        elif number == 2:
            t,timestamp = case3_2(self, gamescore)

        elif number == 3:
            t,timestamp = case3_3(self, gamescore)

        elif number == 4:
            t,timestamp = case3_4(self, gamescore)

        elif number == 5:
            t,timestamp = case3_5(self, gamescore)

        elif number == 6:
            t,timestamp = case3_6(self, gamescore)

        elif number == 7:
            t,timestamp = case3_7(self, gamescore)

        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp
    elif gamescore == 6:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)

        elif number == 2:
            t,timestamp = case3_2(self, gamescore)

        elif number == 3:
            t,timestamp = case3_3(self, gamescore)

        elif number == 4:
            t,timestamp = case3_4(self, gamescore)

        elif number == 5:
            t,timestamp = case3_5(self, gamescore)

        elif number == 6:
            t,timestamp = case3_6(self, gamescore)

        elif number == 7:
            t,timestamp = case3_7(self, gamescore)

        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp
    elif gamescore == 7:
        if number == 1:
            t,timestamp = case3_1(self, gamescore)

        elif number == 2:
            t,timestamp = case3_2(self, gamescore)

        elif number == 3:
            t,timestamp = case3_3(self, gamescore)

        elif number == 4:
            t,timestamp = case3_4(self, gamescore)

        elif number == 5:
            t,timestamp = case3_5(self, gamescore)

        elif number == 6:
            t,timestamp = case3_6(self, gamescore)

        elif number == 7:
            t,timestamp = case3_7(self, gamescore)

        elif number == 8:
            t,timestamp = case3_8(self, gamescore)
        return t, timestamp

