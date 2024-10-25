import random

import pygame


from level import Level
import time



global t, timestamp

def case_1(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline1(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup0(490, 120)
    self.level.setup_endpoint0(490, 885)
    return t, timestamp


def case_2(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline2(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup1(165, 650)
    self.level.setup_endpoint1(1640, 650)
    return t, timestamp


def case_3(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline3(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup2(710, 500)
    self.level.setup_endpoint2(1350, 200)
    return t, timestamp


def case_4(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline4(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup3(405, 485)
    self.level.setup_endpoint3(405, 635)
    return t, timestamp


def case_5(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline5(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup4(730, 910)
    self.level.setup_endpoint4(1065, 910)
    return t, timestamp


def case_6(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline6(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup5(1720, 360)
    self.level.setup_endpoint5(1320, 760)
    return t, timestamp


def case_7(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t= pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline7(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup6(390, 940)
    self.level.setup_endpoint6(885, 920)
    return t, timestamp


def case_8(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline8(self.screen)
    pygame.image.save(self.screen, f"./output_image/pre_screenshot{gamescore}.png")
    self.level.setup7(250, 555)
    self.level.setup_endpoint7(1690, 555)
    return t, timestamp

def case2_1(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline1(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup0(490, 120)
    self.level.setup_endpoint0(490, 885)
    return t, timestamp


def case2_2(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline2(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup1(165, 650)
    self.level.setup_endpoint1(1640, 650)
    return t, timestamp


def case2_3(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline3(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup2(710, 500)
    self.level.setup_endpoint2(1350, 200)
    return t, timestamp


def case2_4(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline4(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup3(405, 485)
    self.level.setup_endpoint3(405, 635)
    return t, timestamp


def case2_5(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline5(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup4(730, 910)
    self.level.setup_endpoint4(1065, 910)
    return t, timestamp


def case2_6(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline6(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup5(1720, 360)
    self.level.setup_endpoint5(1320, 760)
    return t, timestamp


def case2_7(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t= pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline7(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup6(390, 940)
    self.level.setup_endpoint6(885, 920)
    return t, timestamp


def case2_8(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output2_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline8(self.screen)
    pygame.image.save(self.screen, f"./output2_image/pre_screenshot{gamescore}.png")
    self.level.setup7(250, 555)
    self.level.setup_endpoint7(1690, 555)
    return t, timestamp
def case3_1(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline1(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup0(490, 120)
    self.level.setup_endpoint0(490, 885)
    return t, timestamp


def case3_2(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline2(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup1(165, 650)
    self.level.setup_endpoint1(1640, 650)
    return t, timestamp


def case3_3(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline3(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup2(710, 500)
    self.level.setup_endpoint2(1350, 200)
    return t, timestamp


def case3_4(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline4(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup3(405, 485)
    self.level.setup_endpoint3(405, 635)
    return t, timestamp


def case3_5(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline5(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup4(730, 910)
    self.level.setup_endpoint4(1065, 910)
    return t, timestamp


def case3_6(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t=pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline6(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup5(1720, 360)
    self.level.setup_endpoint5(1320, 760)
    return t, timestamp


def case3_7(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t= pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline7(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup6(390, 940)
    self.level.setup_endpoint6(885, 920)
    return t, timestamp


def case3_8(self, gamescore):
    this_level = Level()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    t = pygame.time.get_ticks() / 1000
    pygame.image.save(self.screen, f"./output3_image/post_screenshot{gamescore-1}.png")
    self.screen.fill((255, 255, 255))
    this_level.drawline8(self.screen)
    pygame.image.save(self.screen, f"./output3_image/pre_screenshot{gamescore}.png")
    self.level.setup7(250, 555)
    self.level.setup_endpoint7(1690, 555)
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

