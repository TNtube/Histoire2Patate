import pygame
from scene import Scene


class Game3(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        w, h = screen.get_size()
        self.left_rect = pygame.Rect(w * 0.25, h * 0, w * 0.15, h * 0.6)
        self.left = pygame.transform.scale(pygame.image.load("assets/main_gauche.png"), self.left_rect.size)
        self.left = pygame.transform.rotate(self.left, 180)
        self.right_rect = pygame.Rect(w * 0.60, h * 0, w * 0.1, h * 0.6)
        self.right = pygame.transform.scale(pygame.image.load("assets/main_droite.png"), self.left_rect.size)
        self.right = pygame.transform.rotate(self.right, 180)

        self.font = pygame.font.Font("assets/PIXELMIX.TTF", int(screen.get_width()*0.02))
        self.txt_left = self.font.render("tape la", True, (255, 255, 255))
        self.txt_right = self.font.render("va crever", True, (255, 255, 255))

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.left_rect.collidepoint(event.pos):
                        self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.txt_left, (self.screen.get_width() * 0.1, self.screen.get_height() * 0.3))
        self.screen.blit(self.txt_right, (self.screen.get_width() * 0.8, self.screen.get_height() * 0.3))
        self.screen.blit(self.left, self.left_rect)
        self.screen.blit(self.right, self.right_rect)

    def update(self):
        m_pos = pygame.mouse.get_pos()
        if m_pos[1] - self.right_rect.bottom < 100 and m_pos[0] > self.screen.get_width()//2:
            self.right_rect.bottom = m_pos[1] - 50
            self.right_rect.bottom = max(self.right_rect.bottom, 0)
        elif m_pos[0] > self.screen.get_width()//2:
            self.right_rect.bottom = m_pos[1] - 50
            self.right_rect.y = min(self.right_rect.y, 0)
        else:
            self.right_rect.y = 0
        if self.right_rect.y > 0:
            self.right_rect.y = 0

        if m_pos[0] - self.right_rect.x < 100:
            self.right_rect.x = m_pos[0] + 50
        else:
            self.right_rect.x = m_pos[0] - 50
        self.right_rect.x = max(self.screen.get_width() * 0.6, self.right_rect.x)
        if self.right_rect.x > self.screen.get_width() * 0.7:
            self.right_rect.x = self.screen.get_width() * 0.7


