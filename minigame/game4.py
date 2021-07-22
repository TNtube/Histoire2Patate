import pygame
from scene import Scene


class Game4(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        w, h = screen.get_size()
        self.potato_rect = pygame.Rect(w * 0.3, h * 0.2, w * 0.3, h * 0.7)
        self.potato = pygame.transform.scale(pygame.image.load("assets/patate_corp_stade1.png"), self.potato_rect.size)
        self.tentacles = [
            [pygame.Rect(w * 0.3, h * 0.29, w*0.08, h*0.1), pygame.image.load("assets/racine1.png"), True],
            [pygame.Rect(w * 0.47, h * 0.17, w * 0.04, h * 0.15), pygame.image.load("assets/racine5.png"), True],
            [pygame.Rect(w * 0.47, h * 0.7, w * 0.04, h * 0.1), pygame.image.load("assets/racine2.png"), True],
            [pygame.Rect(w * 0.55, h * 0.6, w * 0.08, h * 0.1), pygame.image.load("assets/racine4.png"), True],
            [pygame.Rect(w * 0.31, h * 0.63, w * 0.08, h * 0.1),
             pygame.transform.rotate(pygame.image.load("assets/racine3.png"), -70), True],
        ]
        self.fall_speed = 0.5
        self.scissors_rect = pygame.Rect(0, 0, w*0.1, h*0.06)
        self.scissors_rect.center = pygame.mouse.get_pos()
        self.scissors = pygame.image.load("assets/tenaille.png")
        self.verif = set()

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(self.verif) == len(self.tentacles):
                        self.running = False
                    for element in self.tentacles:
                        if element[0].collidepoint(event.pos) and element[2]:
                            element[2] = False

    def update(self):
        self.scissors_rect.center = pygame.mouse.get_pos()
        for element, x in zip(self.tentacles, range(len(self.tentacles))):
            if not element[2]:
                element[0].y += 10
                if element[0].y > self.potato_rect.bottom * 0.95:
                    element[0].y = self.potato_rect.bottom * 0.95
                    self.verif.add(x)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.potato, self.potato_rect)
        for element in self.tentacles:
            self.screen.blit(pygame.transform.scale(element[1], element[0].size), element[0])

        self.screen.blit(pygame.transform.scale(self.scissors, self.scissors_rect.size), self.scissors_rect)


