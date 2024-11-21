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

def case_9(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup8(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_10(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup9(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_11(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup10(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_12(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup11(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_13(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup12(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_14(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup13(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_15(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup14(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_16(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup15(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_17(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup16(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_18(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup17(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_19(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup18(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_20(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup19(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_21(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup20(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_22(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup21(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_23(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup22(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_24(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup23(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_25(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup24(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_26(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup25(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_27(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup26(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_28(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup27(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_29(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup28(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case_30(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup29(160, 160)
    self.level.setup_endpoint8(920, 920)
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

def case2_9(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup8(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_10(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup9(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_11(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup10(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_12(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup11(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_13(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup12(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_14(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup13(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_15(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup14(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_16(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup15(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_17(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup16(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_18(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup17(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_19(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup18(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_20(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup19(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_21(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup20(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_22(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup21(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_23(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup22(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_24(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup23(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_25(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup24(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_26(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup25(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_27(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup26(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_28(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup27(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_29(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup28(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case2_30(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup29(160, 160)
    self.level.setup_endpoint8(920, 920)
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

def case3_9(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup8(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_10(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup9(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_11(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup10(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_12(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup11(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_13(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup12(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_14(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup13(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_15(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup14(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_16(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup15(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_17(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup16(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_18(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup17(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_19(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup18(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_20(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup19(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_21(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup20(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_22(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup21(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_23(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup22(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_24(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup23(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_25(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup24(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_26(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup25(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_27(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup26(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_28(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup27(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_29(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup28(160, 160)
    self.level.setup_endpoint8(920, 920)
    return t, timestamp
def case3_30(self,gamescore):
    this_level=Level()
    timestamp= time.strftime('%Y-%m-%d %H:%M:%S')
    t = globalClock.getTime()
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.lines4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup29(160, 160)
    self.level.setup_endpoint8(920, 920)
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
        elif number == 9:
            t,timestamp = case_9(self, gamescore)
        elif number == 10:
            t,timestamp = case_10(self, gamescore)
        elif number == 11:
            t,timestamp = case_11(self, gamescore)
        elif number == 12:
            t,timestamp = case_12(self, gamescore)
        elif number == 13:
            t,timestamp = case_13(self, gamescore)
        elif number == 14:
            t,timestamp = case_14(self, gamescore)
        elif number == 15:
            t,timestamp = case_15(self, gamescore)
        elif number == 16:
            t,timestamp = case_16(self, gamescore)
        elif number == 17:
            t,timestamp = case_17(self, gamescore)
        elif number == 18:
            t,timestamp = case_18(self, gamescore)
        elif number == 19:
            t,timestamp = case_19(self, gamescore)
        elif number == 20:
            t,timestamp = case_20(self, gamescore)
        elif number == 21:
            t,timestamp = case_21(self, gamescore)
        elif number == 22:
            t,timestamp = case_22(self, gamescore)
        elif number == 23:
            t,timestamp = case_23(self, gamescore)
        elif number == 24:
            t,timestamp = case_24(self, gamescore)
        elif number == 25:
            t,timestamp = case_25(self, gamescore)
        elif number == 26:
            t,timestamp = case_26(self, gamescore)
        elif number == 27:
            t,timestamp = case_27(self, gamescore)
        elif number == 28:
            t,timestamp = case_28(self, gamescore)
        elif number == 29:
            t,timestamp = case_29(self, gamescore)
        elif number == 30:
            t,timestamp = case_30(self, gamescore)

        return t, timestamp
    elif gamescore == 1:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 2:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 3:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 4:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 5:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 6:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 7:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 8:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 9:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 10:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 11:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 12:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 13:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 14:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 15:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 16:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 17:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 18:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 19:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 20:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 21:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 22:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 23:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 24:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 25:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 26:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 27:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 28:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 29:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp


def random_painting2(number, self, gamescore):
    global t, timestamp
    gamescore = gamescore - 33
    if gamescore == 0:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)

        return t, timestamp
    elif gamescore == 1:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 2:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 3:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 4:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 5:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 6:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 7:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 8:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 9:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 10:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 11:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 12:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 13:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 14:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 15:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 16:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 17:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 18:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 19:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 20:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 21:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 22:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 23:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 24:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 25:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 26:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 27:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 28:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 29:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp


def random_painting3(number, self, gamescore):
    global t, timestamp
    gamescore = gamescore - 66
    if gamescore == 0:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)

        return t, timestamp
    elif gamescore == 1:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 2:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 3:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 4:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 5:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 6:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 7:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 8:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 9:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 10:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 11:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 12:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 13:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 14:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 15:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 16:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 17:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 18:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 19:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 20:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 21:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 22:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 23:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 24:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 25:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 26:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 27:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 28:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp
    elif gamescore == 29:
        if number == 1:
            t, timestamp = case_1(self, gamescore)
        elif number == 2:
            t, timestamp = case_2(self, gamescore)
        elif number == 3:
            t, timestamp = case_3(self, gamescore)
        elif number == 4:
            t, timestamp = case_4(self, gamescore)
        elif number == 5:
            t, timestamp = case_5(self, gamescore)
        elif number == 6:
            t, timestamp = case_6(self, gamescore)
        elif number == 7:
            t, timestamp = case_7(self, gamescore)
        elif number == 8:
            t, timestamp = case_8(self, gamescore)
        elif number == 9:
            t, timestamp = case_9(self, gamescore)
        elif number == 10:
            t, timestamp = case_10(self, gamescore)
        elif number == 11:
            t, timestamp = case_11(self, gamescore)
        elif number == 12:
            t, timestamp = case_12(self, gamescore)
        elif number == 13:
            t, timestamp = case_13(self, gamescore)
        elif number == 14:
            t, timestamp = case_14(self, gamescore)
        elif number == 15:
            t, timestamp = case_15(self, gamescore)
        elif number == 16:
            t, timestamp = case_16(self, gamescore)
        elif number == 17:
            t, timestamp = case_17(self, gamescore)
        elif number == 18:
            t, timestamp = case_18(self, gamescore)
        elif number == 19:
            t, timestamp = case_19(self, gamescore)
        elif number == 20:
            t, timestamp = case_20(self, gamescore)
        elif number == 21:
            t, timestamp = case_21(self, gamescore)
        elif number == 22:
            t, timestamp = case_22(self, gamescore)
        elif number == 23:
            t, timestamp = case_23(self, gamescore)
        elif number == 24:
            t, timestamp = case_24(self, gamescore)
        elif number == 25:
            t, timestamp = case_25(self, gamescore)
        elif number == 26:
            t, timestamp = case_26(self, gamescore)
        elif number == 27:
            t, timestamp = case_27(self, gamescore)
        elif number == 28:
            t, timestamp = case_28(self, gamescore)
        elif number == 29:
            t, timestamp = case_29(self, gamescore)
        elif number == 30:
            t, timestamp = case_30(self, gamescore)
        return t, timestamp

