from scene import Scene
from image_handler import ImageHandler
import pygame
from minigame.game1 import Game1
from minigame.game2 import Game2
from minigame.game3 import Game3
from minigame.game4 import Game4
from minigame.game5 import Game5
from minigame.game6 import Game6


class Game(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.image_handler = ImageHandler(screen)
        self.menu = pygame.transform.scale(pygame.image.load("assets/menu.png"), screen.get_size())
        w, h = screen.get_size()
        self.button_rect = pygame.Rect(w * 0.55, h * 0.6, w*0.2, h*0.2)
        self.play = False
        self.anim = False
        self.opacity = 0
        self.foo = 0
        self.surf = pygame.Surface((w * 0.28, h * 0.39))

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play:
                    if event.button == 1:
                        if self.image_handler.index <= 41:
                            self.image_handler.index += 1
                        if self.image_handler.index == 6:  # Coupe patate
                            Game1(self.screen).run()
                        if self.image_handler.index == 13:  # Réveille
                            Game2(self.screen).run()
                        if self.image_handler.index == 25:  # le choix
                            Game3(self.screen).run()
                        if self.image_handler.index == 40:  # Coupe racine
                            Game4(self.screen).run()
                        if self.image_handler.index == 41:  # Coupe racine
                            Game5(self.screen).run()
                            Game6(self.screen).run()

                else:
                    if event.button == 1:
                        self.anim = True

    def update(self):
        if self.anim:
            if self.foo >= 350:
                self.play = True
            else:
                self.opacity = min(self.opacity + 2, 255)
                self.foo += 2

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.play:
            self.image_handler.draw()
        else:
            self.screen.blit(self.menu, (0, 0))
            self.surf.set_alpha(self.opacity)
            self.screen.blit(self.surf, (self.screen.get_width() - self.surf.get_width(),
                                         0))
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    game = Game(win)
    game.run()
    pygame.quit()

