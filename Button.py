import pygame.font

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
light_gray = (170, 170, 170)
green = (0, 255, 0)


class Button:
    # 初始化按钮的属性
    def __init__(self, setting, screen, text,  x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = gray
        self.text = text
        self.text_color = black
        self.hover_color = light_gray
        self.current_color = self.button_color
        self.font = pygame.font.Font('./font/STXINGKA.TTF', 40)
        # 创建按钮的rect的对象，并使其设置在指定位置
        self.rect = pygame.Rect(x, y, self.width, self.height)


    def check_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.button_color

    # 绘制一个用颜色填充的按钮，再绘制文本
    def draw_button(self):

        pygame.draw.rect(self.screen, self.current_color, self.rect, border_radius=8)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

