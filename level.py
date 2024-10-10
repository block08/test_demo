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
        self.all_sprites8 = pygame.sprite.Group()
        self.all_sprites9 = pygame.sprite.Group()
        self.all_sprites10 = pygame.sprite.Group()
        self.all_sprites11 = pygame.sprite.Group()
        self.all_sprites12 = pygame.sprite.Group()
        self.all_sprites13 = pygame.sprite.Group()
        self.all_sprites14 = pygame.sprite.Group()
        self.all_sprites15 = pygame.sprite.Group()
        self.all_sprites16 = pygame.sprite.Group()
        self.all_sprites17 = pygame.sprite.Group()
        self.all_sprites18 = pygame.sprite.Group()
        self.all_sprites19 = pygame.sprite.Group()
        self.all_sprites20 = pygame.sprite.Group()
        self.all_sprites21 = pygame.sprite.Group()
        self.all_sprites22 = pygame.sprite.Group()
        self.all_sprites23 = pygame.sprite.Group()
        self.all_sprites24 = pygame.sprite.Group()
        self.all_sprites25 = pygame.sprite.Group()
        self.all_sprites26 = pygame.sprite.Group()
        self.all_sprites27 = pygame.sprite.Group()
        self.all_sprites28 = pygame.sprite.Group()
        self.all_sprites29 = pygame.sprite.Group()

        self.end_sprites0 = pygame.sprite.Group()
        self.end_sprites1 = pygame.sprite.Group()
        self.end_sprites2 = pygame.sprite.Group()
        self.end_sprites3 = pygame.sprite.Group()
        self.end_sprites4 = pygame.sprite.Group()
        self.end_sprites5 = pygame.sprite.Group()
        self.end_sprites6 = pygame.sprite.Group()
        self.end_sprites7 = pygame.sprite.Group()
        self.end_sprites8 = pygame.sprite.Group()
        self.end_sprites9 = pygame.sprite.Group()
        self.end_sprites10 = pygame.sprite.Group()
        self.end_sprites11 = pygame.sprite.Group()
        self.end_sprites12 = pygame.sprite.Group()
        self.end_sprites13 = pygame.sprite.Group()
        self.end_sprites14 = pygame.sprite.Group()
        self.end_sprites15 = pygame.sprite.Group()
        self.end_sprites16 = pygame.sprite.Group()
        self.end_sprites17 = pygame.sprite.Group()
        self.end_sprites18 = pygame.sprite.Group()
        self.end_sprites19 = pygame.sprite.Group()
        self.end_sprites20 = pygame.sprite.Group()
        self.end_sprites21 = pygame.sprite.Group()
        self.end_sprites22 = pygame.sprite.Group()
        self.end_sprites23 = pygame.sprite.Group()
        self.end_sprites24 = pygame.sprite.Group()
        self.end_sprites25 = pygame.sprite.Group()
        self.end_sprites26 = pygame.sprite.Group()
        self.end_sprites27 = pygame.sprite.Group()
        self.end_sprites28 = pygame.sprite.Group()
        self.end_sprites29 = pygame.sprite.Group()
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
    def setup8(self, x, y):
        self.player = Player((x, y), self.all_sprites8)
    def setup9(self, x, y):
        self.player = Player((x, y), self.all_sprites9)
    def setup10(self, x, y):
        self.player = Player((x, y), self.all_sprites10)
    def setup11(self, x, y):
        self.player = Player((x, y), self.all_sprites11)
    def setup12(self, x, y):
        self.player = Player((x, y), self.all_sprites12)
    def setup13(self, x, y):
        self.player = Player((x, y), self.all_sprites13)
    def setup14(self, x, y):
        self.player = Player((x, y), self.all_sprites14)
    def setup15(self, x, y):
        self.player = Player((x, y), self.all_sprites15)
    def setup16(self, x, y):
        self.player = Player((x, y), self.all_sprites16)
    def setup17(self, x, y):
        self.player = Player((x, y), self.all_sprites17)
    def setup18(self, x, y):
        self.player = Player((x, y), self.all_sprites18)
    def setup19(self, x, y):
        self.player = Player((x, y), self.all_sprites19)
    def setup20(self, x, y):
        self.player = Player((x, y), self.all_sprites20)
    def setup21(self, x, y):
        self.player = Player((x, y), self.all_sprites21)
    def setup22(self, x, y):
        self.player = Player((x, y), self.all_sprites22)
    def setup23(self, x, y):
        self.player = Player((x, y), self.all_sprites23)
    def setup24(self, x, y):
        self.player = Player((x, y), self.all_sprites24)
    def setup25(self, x, y):
        self.player = Player((x, y), self.all_sprites25)
    def setup26(self, x, y):
        self.player = Player((x, y), self.all_sprites26)
    def setup27(self, x, y):
        self.player = Player((x, y), self.all_sprites27)
    def setup28(self, x, y):
        self.player = Player((x, y), self.all_sprites28)
    def setup29(self, x, y):
        self.player = Player((x, y), self.all_sprites29)



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
    def setup_endpoint8(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites8)
    def setup_endpoint9(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites9)
    def setup_endpoint10(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites10)
    def setup_endpoint11(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites11)
    def setup_endpoint12(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites12)
    def setup_endpoint13(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites13)
    def setup_endpoint14(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites14)
    def setup_endpoint15(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites15)
    def setup_endpoint16(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites16)
    def setup_endpoint17(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites17)
    def setup_endpoint18(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites18)
    def setup_endpoint19(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites19)
    def setup_endpoint20(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites20)
    def setup_endpoint21(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites21)
    def setup_endpoint22(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites22)
    def setup_endpoint23(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites23)
    def setup_endpoint24(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites24)
    def setup_endpoint25(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites25)
    def setup_endpoint26(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites26)
    def setup_endpoint27(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites27)
    def setup_endpoint28(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites28)
    def setup_endpoint29(self, x, y):
        self.endpoint = EndPoint((x, y), self.end_sprites29)

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
    def run_30(self, dt, stats, numbers, screen):
        if stats.game_score <= 30:
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
            if pygame.sprite.groupcollide(self.all_sprites8, self.end_sprites8, False, False):
                for sprite_end in self.end_sprites8:
                    for sprite_in in self.all_sprites8:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites8.empty()
            if pygame.sprite.groupcollide(self.all_sprites9, self.end_sprites9, False, False):
                for sprite_end in self.end_sprites9:
                    for sprite_in in self.all_sprites9:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites9.empty()
                self.all_sprites9.empty()
            if pygame.sprite.groupcollide(self.all_sprites10, self.end_sprites10, False, False):
                for sprite_end in self.end_sprites10:
                    for sprite_in in self.all_sprites10:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites10.empty()
                self.all_sprites10.empty()
            if pygame.sprite.groupcollide(self.all_sprites11, self.end_sprites11, False, False):
                for sprite_end in self.end_sprites11:
                    for sprite_in in self.all_sprites11:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites11.empty()
                self.all_sprites11.empty()
            if pygame.sprite.groupcollide(self.all_sprites12, self.end_sprites12, False, False):
                for sprite_end in self.end_sprites12:
                    for sprite_in in self.all_sprites12:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites12.empty()
                self.all_sprites12.empty()
            if pygame.sprite.groupcollide(self.all_sprites13, self.end_sprites13, False, False):
                for sprite_end in self.end_sprites13:
                    for sprite_in in self.all_sprites13:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites13.empty()
                self.all_sprites13.empty()
            if pygame.sprite.groupcollide(self.all_sprites14, self.end_sprites14, False, False):
                for sprite_end in self.end_sprites14:
                    for sprite_in in self.all_sprites14:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites14.empty()
                self.all_sprites14.empty()
            if pygame.sprite.groupcollide(self.all_sprites15, self.end_sprites15, False, False):
                for sprite_end in self.end_sprites15:
                    for sprite_in in self.all_sprites15:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites15.empty()
                self.all_sprites15.empty()
            if pygame.sprite.groupcollide(self.all_sprites16, self.end_sprites16, False, False):
                for sprite_end in self.end_sprites16:
                    for sprite_in in self.all_sprites16:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites16.empty()
                self.all_sprites16.empty()
            if pygame.sprite.groupcollide(self.all_sprites17, self.end_sprites17, False, False):
                for sprite_end in self.end_sprites17:
                    for sprite_in in self.all_sprites17:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites17.empty()
                self.all_sprites17.empty()
            if pygame.sprite.groupcollide(self.all_sprites18, self.end_sprites18, False, False):
                for sprite_end in self.end_sprites18:
                    for sprite_in in self.all_sprites18:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites18.empty()
                self.all_sprites18.empty()
            if pygame.sprite.groupcollide(self.all_sprites19, self.end_sprites19, False, False):
                for sprite_end in self.end_sprites19:
                    for sprite_in in self.all_sprites19:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites19.empty()
                self.all_sprites19.empty()
            if pygame.sprite.groupcollide(self.all_sprites20, self.end_sprites20, False, False):
                for sprite_end in self.end_sprites20:
                    for sprite_in in self.all_sprites20:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites20.empty()
                self.all_sprites20.empty()
            if pygame.sprite.groupcollide(self.all_sprites21, self.end_sprites21, False, False):
                for sprite_end in self.end_sprites21:
                    for sprite_in in self.all_sprites21:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites21.empty()
                self.all_sprites21.empty()
            if pygame.sprite.groupcollide(self.all_sprites22, self.end_sprites22, False, False):
                for sprite_end in self.end_sprites22:
                    for sprite_in in self.all_sprites22:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites22.empty()
                self.all_sprites22.empty()
            if pygame.sprite.groupcollide(self.all_sprites23, self.end_sprites23, False, False):
                for sprite_end in self.end_sprites23:
                    for sprite_in in self.all_sprites23:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites23.empty()
                self.all_sprites23.empty()
            if pygame.sprite.groupcollide(self.all_sprites24, self.end_sprites24, False, False):
                for sprite_end in self.end_sprites24:
                    for sprite_in in self.all_sprites24:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites24.empty()
                self.all_sprites24.empty()
            if pygame.sprite.groupcollide(self.all_sprites25, self.end_sprites25, False, False):
                for sprite_end in self.end_sprites25:
                    for sprite_in in self.all_sprites25:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites25.empty()
                self.all_sprites25.empty()
            if pygame.sprite.groupcollide(self.all_sprites26, self.end_sprites26, False, False):
                for sprite_end in self.end_sprites26:
                    for sprite_in in self.all_sprites26:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites26.empty()
                self.all_sprites26.empty()
            if pygame.sprite.groupcollide(self.all_sprites27, self.end_sprites27, False, False):
                for sprite_end in self.end_sprites27:
                    for sprite_in in self.all_sprites27:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites27.empty()
                self.all_sprites27.empty()
            if pygame.sprite.groupcollide(self.all_sprites28, self.end_sprites28, False, False):
                for sprite_end in self.end_sprites28:
                    for sprite_in in self.all_sprites28:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites28.empty()
                self.all_sprites28.empty()
            if pygame.sprite.groupcollide(self.all_sprites29, self.end_sprites29, False, False):
                for sprite_end in self.end_sprites29:
                    for sprite_in in self.all_sprites29:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites29.empty()
                self.all_sprites29.empty()

    def run2_30(self, dt, stats, numbers, screen):
        if stats.game_score <= 30:
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
            if pygame.sprite.groupcollide(self.all_sprites8, self.end_sprites8, False, False):
                for sprite_end in self.end_sprites8:
                    for sprite_in in self.all_sprites8:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites8.empty()
            if pygame.sprite.groupcollide(self.all_sprites9, self.end_sprites9, False, False):
                for sprite_end in self.end_sprites9:
                    for sprite_in in self.all_sprites9:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites9.empty()
                self.all_sprites9.empty()
            if pygame.sprite.groupcollide(self.all_sprites10, self.end_sprites10, False, False):
                for sprite_end in self.end_sprites10:
                    for sprite_in in self.all_sprites10:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites10.empty()
                self.all_sprites10.empty()
            if pygame.sprite.groupcollide(self.all_sprites11, self.end_sprites11, False, False):
                for sprite_end in self.end_sprites11:
                    for sprite_in in self.all_sprites11:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites11.empty()
                self.all_sprites11.empty()
            if pygame.sprite.groupcollide(self.all_sprites12, self.end_sprites12, False, False):
                for sprite_end in self.end_sprites12:
                    for sprite_in in self.all_sprites12:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites12.empty()
                self.all_sprites12.empty()
            if pygame.sprite.groupcollide(self.all_sprites13, self.end_sprites13, False, False):
                for sprite_end in self.end_sprites13:
                    for sprite_in in self.all_sprites13:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites13.empty()
                self.all_sprites13.empty()
            if pygame.sprite.groupcollide(self.all_sprites14, self.end_sprites14, False, False):
                for sprite_end in self.end_sprites14:
                    for sprite_in in self.all_sprites14:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites14.empty()
                self.all_sprites14.empty()
            if pygame.sprite.groupcollide(self.all_sprites15, self.end_sprites15, False, False):
                for sprite_end in self.end_sprites15:
                    for sprite_in in self.all_sprites15:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites15.empty()
                self.all_sprites15.empty()
            if pygame.sprite.groupcollide(self.all_sprites16, self.end_sprites16, False, False):
                for sprite_end in self.end_sprites16:
                    for sprite_in in self.all_sprites16:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites16.empty()
                self.all_sprites16.empty()
            if pygame.sprite.groupcollide(self.all_sprites17, self.end_sprites17, False, False):
                for sprite_end in self.end_sprites17:
                    for sprite_in in self.all_sprites17:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites17.empty()
                self.all_sprites17.empty()
            if pygame.sprite.groupcollide(self.all_sprites18, self.end_sprites18, False, False):
                for sprite_end in self.end_sprites18:
                    for sprite_in in self.all_sprites18:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites18.empty()
                self.all_sprites18.empty()
            if pygame.sprite.groupcollide(self.all_sprites19, self.end_sprites19, False, False):
                for sprite_end in self.end_sprites19:
                    for sprite_in in self.all_sprites19:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites19.empty()
                self.all_sprites19.empty()
            if pygame.sprite.groupcollide(self.all_sprites20, self.end_sprites20, False, False):
                for sprite_end in self.end_sprites20:
                    for sprite_in in self.all_sprites20:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites20.empty()
                self.all_sprites20.empty()
            if pygame.sprite.groupcollide(self.all_sprites21, self.end_sprites21, False, False):
                for sprite_end in self.end_sprites21:
                    for sprite_in in self.all_sprites21:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites21.empty()
                self.all_sprites21.empty()
            if pygame.sprite.groupcollide(self.all_sprites22, self.end_sprites22, False, False):
                for sprite_end in self.end_sprites22:
                    for sprite_in in self.all_sprites22:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites22.empty()
                self.all_sprites22.empty()
            if pygame.sprite.groupcollide(self.all_sprites23, self.end_sprites23, False, False):
                for sprite_end in self.end_sprites23:
                    for sprite_in in self.all_sprites23:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites23.empty()
                self.all_sprites23.empty()
            if pygame.sprite.groupcollide(self.all_sprites24, self.end_sprites24, False, False):
                for sprite_end in self.end_sprites24:
                    for sprite_in in self.all_sprites24:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites24.empty()
                self.all_sprites24.empty()
            if pygame.sprite.groupcollide(self.all_sprites25, self.end_sprites25, False, False):
                for sprite_end in self.end_sprites25:
                    for sprite_in in self.all_sprites25:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites25.empty()
                self.all_sprites25.empty()
            if pygame.sprite.groupcollide(self.all_sprites26, self.end_sprites26, False, False):
                for sprite_end in self.end_sprites26:
                    for sprite_in in self.all_sprites26:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites26.empty()
                self.all_sprites26.empty()
            if pygame.sprite.groupcollide(self.all_sprites27, self.end_sprites27, False, False):
                for sprite_end in self.end_sprites27:
                    for sprite_in in self.all_sprites27:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites27.empty()
                self.all_sprites27.empty()
            if pygame.sprite.groupcollide(self.all_sprites28, self.end_sprites28, False, False):
                for sprite_end in self.end_sprites28:
                    for sprite_in in self.all_sprites28:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites28.empty()
                self.all_sprites28.empty()
            if pygame.sprite.groupcollide(self.all_sprites29, self.end_sprites29, False, False):
                for sprite_end in self.end_sprites29:
                    for sprite_in in self.all_sprites29:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites29.empty()
                self.all_sprites29.empty()

    def run3_30(self, dt, stats, numbers, screen):
        if stats.game_score <= 30:
            index = stats.game_score
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
            if pygame.sprite.groupcollide(self.all_sprites8, self.end_sprites8, False, False):
                for sprite_end in self.end_sprites8:
                    for sprite_in in self.all_sprites8:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                self.all_sprites8.empty()
            if pygame.sprite.groupcollide(self.all_sprites9, self.end_sprites9, False, False):
                for sprite_end in self.end_sprites9:
                    for sprite_in in self.all_sprites9:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites9.empty()
                self.all_sprites9.empty()
            if pygame.sprite.groupcollide(self.all_sprites10, self.end_sprites10, False, False):
                for sprite_end in self.end_sprites10:
                    for sprite_in in self.all_sprites10:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites10.empty()
                self.all_sprites10.empty()
            if pygame.sprite.groupcollide(self.all_sprites11, self.end_sprites11, False, False):
                for sprite_end in self.end_sprites11:
                    for sprite_in in self.all_sprites11:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites11.empty()
                self.all_sprites11.empty()
            if pygame.sprite.groupcollide(self.all_sprites12, self.end_sprites12, False, False):
                for sprite_end in self.end_sprites12:
                    for sprite_in in self.all_sprites12:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites12.empty()
                self.all_sprites12.empty()
            if pygame.sprite.groupcollide(self.all_sprites13, self.end_sprites13, False, False):
                for sprite_end in self.end_sprites13:
                    for sprite_in in self.all_sprites13:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites13.empty()
                self.all_sprites13.empty()
            if pygame.sprite.groupcollide(self.all_sprites14, self.end_sprites14, False, False):
                for sprite_end in self.end_sprites14:
                    for sprite_in in self.all_sprites14:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites14.empty()
                self.all_sprites14.empty()
            if pygame.sprite.groupcollide(self.all_sprites15, self.end_sprites15, False, False):
                for sprite_end in self.end_sprites15:
                    for sprite_in in self.all_sprites15:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites15.empty()
                self.all_sprites15.empty()
            if pygame.sprite.groupcollide(self.all_sprites16, self.end_sprites16, False, False):
                for sprite_end in self.end_sprites16:
                    for sprite_in in self.all_sprites16:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites16.empty()
                self.all_sprites16.empty()
            if pygame.sprite.groupcollide(self.all_sprites17, self.end_sprites17, False, False):
                for sprite_end in self.end_sprites17:
                    for sprite_in in self.all_sprites17:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites17.empty()
                self.all_sprites17.empty()
            if pygame.sprite.groupcollide(self.all_sprites18, self.end_sprites18, False, False):
                for sprite_end in self.end_sprites18:
                    for sprite_in in self.all_sprites18:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites18.empty()
                self.all_sprites18.empty()
            if pygame.sprite.groupcollide(self.all_sprites19, self.end_sprites19, False, False):
                for sprite_end in self.end_sprites19:
                    for sprite_in in self.all_sprites19:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites19.empty()
                self.all_sprites19.empty()
            if pygame.sprite.groupcollide(self.all_sprites20, self.end_sprites20, False, False):
                for sprite_end in self.end_sprites20:
                    for sprite_in in self.all_sprites20:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites20.empty()
                self.all_sprites20.empty()
            if pygame.sprite.groupcollide(self.all_sprites21, self.end_sprites21, False, False):
                for sprite_end in self.end_sprites21:
                    for sprite_in in self.all_sprites21:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites21.empty()
                self.all_sprites21.empty()
            if pygame.sprite.groupcollide(self.all_sprites22, self.end_sprites22, False, False):
                for sprite_end in self.end_sprites22:
                    for sprite_in in self.all_sprites22:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites22.empty()
                self.all_sprites22.empty()
            if pygame.sprite.groupcollide(self.all_sprites23, self.end_sprites23, False, False):
                for sprite_end in self.end_sprites23:
                    for sprite_in in self.all_sprites23:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites23.empty()
                self.all_sprites23.empty()
            if pygame.sprite.groupcollide(self.all_sprites24, self.end_sprites24, False, False):
                for sprite_end in self.end_sprites24:
                    for sprite_in in self.all_sprites24:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites24.empty()
                self.all_sprites24.empty()
            if pygame.sprite.groupcollide(self.all_sprites25, self.end_sprites25, False, False):
                for sprite_end in self.end_sprites25:
                    for sprite_in in self.all_sprites25:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites25.empty()
                self.all_sprites25.empty()
            if pygame.sprite.groupcollide(self.all_sprites26, self.end_sprites26, False, False):
                for sprite_end in self.end_sprites26:
                    for sprite_in in self.all_sprites26:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites26.empty()
                self.all_sprites26.empty()
            if pygame.sprite.groupcollide(self.all_sprites27, self.end_sprites27, False, False):
                for sprite_end in self.end_sprites27:
                    for sprite_in in self.all_sprites27:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites27.empty()
                self.all_sprites27.empty()
            if pygame.sprite.groupcollide(self.all_sprites28, self.end_sprites28, False, False):
                for sprite_end in self.end_sprites28:
                    for sprite_in in self.all_sprites28:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites28.empty()
                self.all_sprites28.empty()
            if pygame.sprite.groupcollide(self.all_sprites29, self.end_sprites29, False, False):
                for sprite_end in self.end_sprites29:
                    for sprite_in in self.all_sprites29:
                        pygame.draw.line(screen, black, sprite_in.rect.center, sprite_end.rect.center, 5)
                        self.all_sprites29.empty()
                self.all_sprites29.empty()

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


