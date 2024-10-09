#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

import pygame
from psychopy.visual.movies import players

from player import Player, EndPoint

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
linewidth = 4

def is_fully_inside(inner_rect, outer_rect):
    """检查 inner_rect 是否完全在 outer_rect 内部"""
    return outer_rect.contains(inner_rect)

class Level:

    def __init__(self):
        # get the display surface

        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.all_sprites0 = pygame.sprite.Group()
        self.all_sprites1 = pygame.sprite.Group()
        self.all_sprites2 = pygame.sprite.Group()
        self.all_sprites3 = pygame.sprite.Group()
        self.all_sprites4 = pygame.sprite.Group()
        self.all_sprites5 = pygame.sprite.Group()
        self.all_sprites6 = pygame.sprite.Group()
        self.all_sprites7 = pygame.sprite.Group()

        self.end_sprites0 = pygame.sprite.Group()
        self.end_sprites1 = pygame.sprite.Group()
        self.end_sprites2 = pygame.sprite.Group()
        self.end_sprites3 = pygame.sprite.Group()
        self.end_sprites4 = pygame.sprite.Group()
        self.end_sprites5 = pygame.sprite.Group()
        self.end_sprites6 = pygame.sprite.Group()
        self.end_sprites7 = pygame.sprite.Group()
    def setup0(self, x, y):
        self.player = Player((x, y), self.all_sprites0)
    def setup1(self, x, y):
        self.player = Player((x, y), self.all_sprites1)

    def setup2(self, x, y):
        self.player = Player((x, y), self.all_sprites2)

    def setup3(self, x, y):
        self.player = Player((x, y), self.all_sprites3)

    def setup4(self, x, y):
        self.player = Player((x, y), self.all_sprites4)

    def setup5(self, x, y):
        self.player = Player((x, y), self.all_sprites5)

    def setup6(self, x, y):
        self.player = Player((x, y), self.all_sprites6)

    def setup7(self, x, y):
        self.player = Player((x, y), self.all_sprites7)


    def setup_endpoint0(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites0)
    def setup_endpoint1(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites1)
    def setup_endpoint2(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites2)
    def setup_endpoint3(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites3)
    def setup_endpoint4(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites4)
    def setup_endpoint5(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites5)
    def setup_endpoint6(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites6)
    def setup_endpoint7(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites7)

    def run(self, dt, stats, numbers, screen):
        if stats.game_score <= 8:
            index = stats.game_score
            sprite_group = getattr(self, f'all_sprites{numbers[index-1]-1}')
            sprite_end_group = getattr(self, f'end_sprites{numbers[index - 1] - 1}')
            sprite_group.draw(self.display_surface)
            sprite_end_group.draw(self.display_surface)
            sprite_group.update(dt)

            if pygame.sprite.groupcollide(self.all_sprites0, self.end_sprites0, False, False):
                for sprite_end in self.end_sprites0:
                    for sprite_in in self.all_sprites0:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites0.empty()
            if pygame.sprite.groupcollide(self.all_sprites1, self.end_sprites1, False, False):
                for sprite_end in self.end_sprites1:
                    for sprite_in in self.all_sprites1:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites1.empty()
            if pygame.sprite.groupcollide(self.all_sprites2, self.end_sprites2, False, False):
                for sprite_end in self.end_sprites2:
                    for sprite_in in self.all_sprites2:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites2.empty()
            if pygame.sprite.groupcollide(self.all_sprites3, self.end_sprites3, False, False):
                for sprite_end in self.end_sprites3:
                    for sprite_in in self.all_sprites3:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites3.empty()
            if pygame.sprite.groupcollide(self.all_sprites4, self.end_sprites4, False, False):
                for sprite_end in self.end_sprites4:
                    for sprite_in in self.all_sprites4:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites4.empty()
            if pygame.sprite.groupcollide(self.all_sprites5, self.end_sprites5, False, False):
                for sprite_end in self.end_sprites5:
                    for sprite_in in self.all_sprites5:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites5.empty()
            if pygame.sprite.groupcollide(self.all_sprites6, self.end_sprites6, False, False):
                for sprite_end in self.end_sprites6:
                    for sprite_in in self.all_sprites6:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites6.empty()
            if pygame.sprite.groupcollide(self.all_sprites7, self.end_sprites7, False, False):
                for sprite_end in self.end_sprites7:
                    for sprite_in in self.all_sprites7:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites7.empty()


    def run2(self, dt, stats, numbers, screen):
        if 11 < stats.game_score <= 19:
            index = stats.game_score - 11
            sprite_group = getattr(self, f'all_sprites{numbers[index - 1] - 1}')
            sprite_end_group = getattr(self, f'end_sprites{numbers[index - 1] - 1}')
            sprite_group.draw(self.display_surface)
            sprite_end_group.draw(self.display_surface)
            sprite_group.update(dt)
            if pygame.sprite.groupcollide(self.all_sprites0, self.end_sprites0, False, False):
                for sprite_end in self.end_sprites0:
                    for sprite_in in self.all_sprites0:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites0.empty()
            if pygame.sprite.groupcollide(self.all_sprites1, self.end_sprites1, False, False):
                for sprite_end in self.end_sprites1:
                    for sprite_in in self.all_sprites1:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites1.empty()
            if pygame.sprite.groupcollide(self.all_sprites2, self.end_sprites2, False, False):
                for sprite_end in self.end_sprites2:
                    for sprite_in in self.all_sprites2:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites2.empty()
            if pygame.sprite.groupcollide(self.all_sprites3, self.end_sprites3, False, False):
                for sprite_end in self.end_sprites3:
                    for sprite_in in self.all_sprites3:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites3.empty()
            if pygame.sprite.groupcollide(self.all_sprites4, self.end_sprites4, False, False):
                for sprite_end in self.end_sprites4:
                    for sprite_in in self.all_sprites4:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites4.empty()
            if pygame.sprite.groupcollide(self.all_sprites5, self.end_sprites5, False, False):
                for sprite_end in self.end_sprites5:
                    for sprite_in in self.all_sprites5:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites5.empty()
            if pygame.sprite.groupcollide(self.all_sprites6, self.end_sprites6, False, False):
                for sprite_end in self.end_sprites6:
                    for sprite_in in self.all_sprites6:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites6.empty()
            if pygame.sprite.groupcollide(self.all_sprites7, self.end_sprites7, False, False):
                for sprite_end in self.end_sprites7:
                    for sprite_in in self.all_sprites7:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites7.empty()


    def run3(self, dt, stats, numbers, screen):
        if 22 < stats.game_score <= 30:
            index = stats.game_score - 22
            sprite_group = getattr(self, f'all_sprites{numbers[index - 1] - 1}')
            sprite_end_group = getattr(self, f'end_sprites{numbers[index - 1] - 1}')
            sprite_group.draw(self.display_surface)
            sprite_end_group.draw(self.display_surface)
            sprite_group.update(dt)
            if pygame.sprite.groupcollide(self.all_sprites0, self.end_sprites0, False, False):
                for sprite_end in self.end_sprites0:
                    for sprite_in in self.all_sprites0:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites0.empty()
            if pygame.sprite.groupcollide(self.all_sprites1, self.end_sprites1, False, False):
                for sprite_end in self.end_sprites1:
                    for sprite_in in self.all_sprites1:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites1.empty()
            if pygame.sprite.groupcollide(self.all_sprites2, self.end_sprites2, False, False):
                for sprite_end in self.end_sprites2:
                    for sprite_in in self.all_sprites2:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites2.empty()
            if pygame.sprite.groupcollide(self.all_sprites3, self.end_sprites3, False, False):
                for sprite_end in self.end_sprites3:
                    for sprite_in in self.all_sprites3:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites3.empty()
            if pygame.sprite.groupcollide(self.all_sprites4, self.end_sprites4, False, False):
                for sprite_end in self.end_sprites4:
                    for sprite_in in self.all_sprites4:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites4.empty()
            if pygame.sprite.groupcollide(self.all_sprites5, self.end_sprites5, False, False):
                for sprite_end in self.end_sprites5:
                    for sprite_in in self.all_sprites5:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites5.empty()
            if pygame.sprite.groupcollide(self.all_sprites6, self.end_sprites6, False, False):
                for sprite_end in self.end_sprites6:
                    for sprite_in in self.all_sprites6:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites6.empty()
            if pygame.sprite.groupcollide(self.all_sprites7, self.end_sprites7, False, False):
                for sprite_end in self.end_sprites7:
                    for sprite_in in self.all_sprites7:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites7.empty()



    def drawline(self, screen):
        pygame.draw.line(screen, black, (160, 540), (1760, 540), linewidth)

    def drawrect(self, screen):
        pygame.draw.rect(screen, black, (560, 340, 800, 400), linewidth)

    def drawline2(self, screen):
        pygame.draw.lines(screen, black, False, [(960, 540), (960, 400), (500, 400), (400, 400), (300, 400)],  linewidth)

    def lines1(self, screen):
        pygame.draw.lines(screen, black, False, [(1000, 500), (1000, 150), (100, 150)], linewidth)

    def lines2(self, screen):
        pygame.draw.lines(screen, black, False, [(100, 100), (1500, 100), (1500, 900)], linewidth)

    def drawline_1(self, screen):
        pygame.draw.line(screen, black, (960, 100), (960, 900), linewidth)

    def lines3(self, screen):
        pygame.draw.lines(screen, black, False,[(160, 160), (160, 920), (920, 920)], linewidth)

    def lines4(self, screen):
        pygame.draw.lines(screen, black, False,[(160, 160), (920, 160), (920, 920)], linewidth)


