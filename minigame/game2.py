import pygame
from scene import Scene
import random


class Game2(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        w, h = screen.get_size()
        self.gf_rect = pygame.Rect(w * 0.28, h * 0.2, w * 0.4, h * 0.5)
        self.gf = pygame.transform.scale(pygame.image.load("assets/fille_nrv.png"),
                                         self.gf_rect.size)
        self.opacity = 0.99
        self.font = pygame.font.Font("assets/PIXELMIX.TTF", int(screen.get_width()*0.02))
        self.render_txt = self.font.render("Reveille-toi !!!", True, (255, 255, 255))
        self.popup = []
        self.timer = 0

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for element in self.popup:
                        if pygame.Rect(element[0][0], element[0][1],
                                       self.render_txt.get_width(),
                                       self.render_txt.get_height()).collidepoint(event.pos):
                            element[1] = 0
                            self.opacity -= 0.1

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.gf, self.gf_rect)
        bg = pygame.Surface(self.screen.get_size())
        bg.set_alpha(int(self.opacity * 255))
        self.screen.blit(bg, (0, 0))
        for element in self.popup:
            if element[1] > 0:
                self.screen.blit(self.render_txt, element[0])
                element[1] -= 1

    def update(self):
        self.timer += 1
        if self.timer % 60 == 0 and self.opacity > 0:
            self.popup.append([(random.randint(0, int(self.screen.get_width() * 0.8)),
                                random.randint(0, int(self.screen.get_height() * 0.8))),
                               random.randint(80, 100)])
        if self.opacity <= 0:
            self.running = False



