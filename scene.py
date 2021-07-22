from abc import ABC
import pygame


class Scene(ABC):
    def __init__(self, screen: pygame.Surface):
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.screen = screen

    def set_fps(self, fps: int):
        self.fps = fps

    def handler_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        ...

    def draw(self):
        ...

    def run(self):
        while self.running:
            self.handler_input()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)




