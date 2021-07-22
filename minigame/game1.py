import pygame
from scene import Scene


class Game1(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        w, h = screen.get_size()
        self.knife_rect = pygame.Rect(w * 0.2, h * 0.1, w * 0.4, h * 0.1)
        self.knife = pygame.transform.scale(pygame.image.load("assets/couteau.png"), self.knife_rect.size)
        self.follow = False
        self.potato_left_rect = pygame.Rect(w*0.3, h*0.6, w*0.2, h*0.3)
        self.potato_left = pygame.transform.scale(pygame.image.load("assets/patate_corp.png"),
                                                  self.potato_left_rect.size)
        self.potato_right_rect = pygame.Rect(w * 0.445, h * 0.6, w * 0.2, h * 0.3)
        self.potato_right = pygame.transform.scale(pygame.image.load("assets/patate_tete.png"),
                                                   self.potato_right_rect.size)
        self.goal_left = pygame.Rect(w*0.25, h*0.6, w*0.2, h*0.3)
        self.goal_right = pygame.Rect(w * 0.47, h * 0.6, w * 0.2, h * 0.3)
        self.goal_knife = pygame.Rect(w * 0.25, h * 0.8, w * 0.4, h * 0.1)
        self.anim = 0.05
        self.font = pygame.font.Font("assets/PIXELMIX.TTF", int(screen.get_width()*0.02))

        self.batar = self.font.render("batar", True, (255, 255, 255))
        self.osepa = self.font.render("tu vas pas oser...", True, (255, 255, 255))

        self.cutting = False

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not self.cutting:
                        if self.knife_rect.collidepoint(*event.pos):
                            self.follow = True
                    else:
                        if any([self.potato_left_rect == self.goal_left,
                                self.knife_rect == self.goal_knife,
                                self.potato_right_rect == self.goal_right]):
                            self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.follow = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.potato_left, self.potato_left_rect)
        self.screen.blit(self.knife, self.knife_rect)
        if self.cutting:
            if not any([self.potato_left_rect == self.goal_left,
                        self.knife_rect == self.goal_knife,
                        self.potato_right_rect == self.goal_right]):
                self.screen.blit(self.osepa, (self.screen.get_width() * 0.7, self.screen.get_height() * 0.4))
            else:
                self.screen.blit(self.batar, (self.screen.get_width() * 0.75, self.screen.get_height() * 0.7))
        self.screen.blit(self.potato_right, self.potato_right_rect)

    def update(self):
        if self.knife_rect.colliderect(self.potato_left_rect) or self.knife_rect.colliderect(self.potato_right_rect):
            self.cutting = True
        if self.follow and not self.cutting:
            self.knife_rect.center = pygame.mouse.get_pos()
        if self.cutting:
            self.potato_left_rect.x += (self.goal_left.x - self.potato_left_rect.x) * self.anim
            self.potato_right_rect.x += (self.goal_right.x - self.potato_right_rect.x) * self.anim
            self.potato_left_rect.y += (self.goal_left.y - self.potato_left_rect.y) * self.anim
            self.potato_right_rect.y += (self.goal_right.y - self.potato_right_rect.y) * self.anim
            self.knife_rect.x += (self.goal_knife.x - self.knife_rect.x) * self.anim
            self.knife_rect.y += (self.goal_knife.y - self.knife_rect.y) * self.anim
