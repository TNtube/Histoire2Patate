import pygame
import json


pygame.font.init()

with open("text.json", "r") as file:
    text_list = json.load(file)["text"]


class TextHandler:
    def __init__(self, screen: pygame.Surface, index, pos):
        self.screen = screen
        self.pos = pygame.Rect(pos)
        self.text_pos = (self.pos.x + self.pos.w * 0.05, self.pos.y + self.pos.h * 0.1)
        self.text_list = text_list
        self._index = index
        self.actual_text = self.text_list[self._index]

        self.font = pygame.font.Font("assets/PIXELMIX.TTF", int(screen.get_width()*0.02))
        self.act_text_ind = 0
        self.update_text = True
        self.render_txt = ""
        self.all_text = False

    def draw(self):
        length = 5  # NOMBRE DE LETTRE PAR LIGNE
        # pygame.draw.rect(self.screen, (255, 255, 255), self.pos, 5)
        for i in range(len(self.render_txt.split()) // length + 1):
            text = self.render_txt.split()[i * length:i * length + length]
            surf = self.font.render(" ".join(text), True, (255, 255, 255))
            self.screen.blit(surf, (self.text_pos[0], self.text_pos[1] + i * self.pos.h * 0.20))

    def update(self):
        if self.act_text_ind // 3 >= len(self.actual_text) or self.all_text:
            self.update_text = False
            self.all_text = True
        if self.all_text:
            self.render_txt = self.actual_text
        if self.update_text:
            self.render_txt = self.actual_text[:self.act_text_ind // 3 + 1]
            self.act_text_ind += 1

    """def next_text(self):
        self._index += 1
        self.actual_text = self.text_list[self._index % len(self.text_list)]
        self.act_text_ind = 0
        self.update_text = True
        self.render_txt = ""
        self.all_text = False"""
