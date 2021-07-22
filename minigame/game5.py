import itertools

import pygame
from scene import Scene


class Game5(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        w, h = screen.get_size()
        self.normal_rect = pygame.Rect(w * 0.32, h * 0.3, w * 0.28, h * 0.6)
        self.normal = pygame.image.load("assets/perso_idle.png")
        self.crouch_rect = pygame.Rect(w * 0.32, h * 0.4, w * 0.28, h * 0.5)
        self.crouch = pygame.image.load("assets/perso_accroupi.png")
        self.jump_rect = pygame.Rect(w * 0.32, h * 0.2, w * 0.22, h * 0.7)
        self.jump = pygame.image.load("assets/perso_vol.png")
        self.total_bar = 100
        self.bar = 0
        self.sayen = itertools.cycle([pygame.image.load("assets/f1.png"),
                                      pygame.image.load("assets/f2.png"),
                                      pygame.image.load("assets/f3.png")])
        self.act_sa = next(self.sayen)
        self.timer = 0
        self.bg = pygame.image.load('assets/map_depart.png')
        self.bg = pygame.transform.scale(self.bg, (int(self.screen.get_width()), int(self.bg.get_height() *
                                                   ((self.screen.get_width()) / (self.bg.get_width())))))
        self.bg_pos = pygame.Rect(0, 0, 0, 0)
        self.bg_pos.y = self.screen.get_height() - self.bg.get_height()

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.bar < 100:
                        self.bar += 15

    def update(self):
        if self.bar < 100:
            self.bar = max(self.bar - 1, 0)
        else:
            self.bar = 100
            self.bg_pos.y += 20
            if self.bg_pos.y >= 0:
                self.running = False

        self.timer += 1
        if self.timer % 10 == 0:
            self.act_sa = next(self.sayen)

    def draw(self):
        sw, sh = self.screen.get_size()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, self.bg_pos)
        x, y, w, h = pygame.Rect(sw * 0.9, sh * 0.3, sw * 0.05, sh * 0.4)
        pygame.draw.rect(self.screen, (255, 0, 0), (x + 2, y + 2 +
                                                    (h - 2) - (h - 2) * self.bar / self.total_bar, w - 2,
                                                    (h - 2) * self.bar / self.total_bar))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (x, y, w, h), 5)

        if self.bar < 10:
            self.screen.blit(pygame.transform.scale(self.normal, self.normal_rect.size), self.normal_rect)
        elif self.bar < 100:
            self.screen.blit(pygame.transform.scale(self.crouch, self.crouch_rect.size), self.crouch_rect)
            self.screen.blit(pygame.transform.scale(self.act_sa,
                                                    (int(sw * 0.4), int(sh * 0.65))),
                             (sw * 0.25, sh * 0.3))
        else:
            self.screen.blit(pygame.transform.scale(self.jump, self.jump_rect.size), self.jump_rect)
