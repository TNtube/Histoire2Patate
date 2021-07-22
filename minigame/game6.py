import itertools
import random

import pygame
from scene import Scene


colors = itertools.cycle(['green', 'blue', 'purple', 'pink', 'red', 'orange', 'brown'])


def change_color(img, col):
    img = img.copy()
    for i in range(img.get_width()):
        for j in range(img.get_height()):
            if img.get_at((i, j)) != pygame.color.Color("black"):
                col.a = img.get_at((i, j)).a
                img.set_at((i, j), col)
    return img


class Game6(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        w, h = screen.get_size()
        self.enemy = pygame.transform.scale(pygame.image.load("assets/alien_minijeu.png"),
                                            (int(w * 0.1), int(h * 0.1)))
        self.enemies = []
        self.timer = 0
        self.player_rect = pygame.Rect(w * 0.45, h * 0.68, w * 0.1, h * 0.31)
        self.player = pygame.transform.scale(pygame.image.load("assets/perso_vol.png"), self.player_rect.size)
        self.proj = pygame.image.load("assets/projectile.png")
        self.proj = pygame.transform.scale(self.proj, (self.proj.get_width() * 3, self.proj.get_height() * 3))
        self.all_proj = []
        self.bg = pygame.image.load('assets/milieu__extension_map_minijeu.png')
        self.bg = pygame.transform.scale(self.bg, (int(self.screen.get_width()), int(self.bg.get_height() *
                                                                                     ((self.screen.get_width()) / (
                                                                                         self.bg.get_width())))))
        self.bg_pos = pygame.Rect(0, 0, 0, 0)
        self.bg_pos.y = self.screen.get_height() - self.bg.get_height()
        self.win = 10

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.all_proj.append(
                        [pygame.Rect(self.player_rect.x + self.player_rect.w // 4,
                                     self.player_rect.y + self.player_rect.w // 2,
                                     self.proj.get_width(), self.proj.get_height()),
                         True]
                    )

    def update(self):
        w, h = self.screen.get_size()
        self.timer += 1
        if self.timer % 90 == 0:
            self.enemies.append([pygame.Rect(random.randint(0, int(self.screen.get_width() * 0.8)),
                                             0, int(w * 0.1), int(h * 0.1)),
                                 True, change_color(self.enemy, pygame.Color(next(colors)))])
        m_pos = pygame.mouse.get_pos()
        self.player_rect.x -= (self.player_rect.x + self.player_rect.w // 2 - m_pos[0]) * 0.2

        for element in self.enemies:
            element[0].y += 10
        for proj in self.all_proj:
            proj[0].y -= 20
            for element in self.enemies:
                if proj[0].colliderect(element[0]) and element[1] and proj[1]:
                    self.win -= 1
                    proj[1] = False
                    element[1] = False

        if self.bg_pos.y >= 0:
            self.bg_pos.y = self.screen.get_height() - self.bg.get_height()
        self.bg_pos.y += 30
        if not self.win:
            self.running = False

    def draw(self):
        w, h = self.screen.get_size()
        self.screen.blit(self.bg, self.bg_pos)
        self.screen.blit(self.player, self.player_rect)
        for element in self.enemies:
            if element[1]:
                self.screen.blit(element[2], element[0])

        for proj in self.all_proj:
            if proj[1]:
                self.screen.blit(self.proj, proj[0])
