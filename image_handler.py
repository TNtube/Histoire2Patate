import copy
import itertools

import pygame
from text_handler import TextHandler
from unittest import mock
from utils import all_images


class ImageHandler:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.images = []
        for scene in all_images(screen.get_width(), screen.get_height()):
            lst = []
            for data in scene:
                a = pygame.Rect(data["coord1"] if data["coord1"] else (0, 0, 0, 0))
                b = pygame.Rect(data["coord2"] if data["coord2"] else (0, 0, 0, 0))
                lst.append({
                    "coord1": a,
                    "coord2": b,
                    "img": pygame.image.load("assets/" + data["name"] + ".png")
                    if data["name"] else pygame.Surface((1, 1)),
                    "anim": data["anim"],
                    "text": TextHandler(screen, data["txt_ind"],
                                        data["txt_pos"]) if data["txt_pos"] else mock.Mock(),
                    "txt_ind": data["txt_ind"],
                    "name": data["name"]
                })
            self.images.append(lst)

        self.index = 0

        self.choix = [("a mon travail !", "a la piscine !"),
                      ("un super job", "un truc tout pt"),
                      ("je les adore", "je les deteste")]
        self.font = pygame.font.Font("assets/PIXELMIX.TTF", int(screen.get_width() * 0.02))
        self.m = False

    def draw(self):
        w, h = self.screen.get_size()
        for data in self.images[self.index]:
            coord1 = data["coord1"]
            coord2 = data["coord2"]
            coord1.x += (coord2.x - coord1.x) * data["anim"]
            coord1.y += (coord2.y - coord1.y) * data["anim"]
            data["coord1"] = coord1
            img = data["img"]
            text = data["text"]
            ind = data["txt_ind"]
            if data["name"] == "alien_uni":
                img = data["img"] = multicolor(img)
            self.screen.blit(pygame.transform.scale(img, (coord1.w, coord1.h)), coord1)
            text.draw()
            text.update()
            if ind == -1:
                a, b = self.choix[0]
            if ind == -2:
                a, b = self.choix[1]
            if ind == -3:
                a, b = self.choix[2]
            if ind in (-1, -2, -3):
                a = self.font.render(a, True, (255, 255, 255))
                b = self.font.render(b, True, (255, 255, 255))
                self.screen.blit(a, (w * .75, h * .4))
                self.screen.blit(b, (w * .75, h * .5))
                if self.m:
                    pygame.draw.line(self.screen, (255, 255, 255),
                                     (w * .75, h * .45), (w * .75 + a.get_width(), h * .45), 2)
                else:
                    pygame.draw.line(self.screen, (255, 255, 255),
                                     (w * .75, h * .55), (w * .75 + b.get_width(), h * .55), 2)
                self.m = pygame.mouse.get_pos()[1] < self.screen.get_height() * 0.48


colors = itertools.cycle(['green', 'blue', 'purple', 'pink', 'red', 'orange'])
datas = {
    "step": 1,
    "base_color": next(colors),
    "next_color": next(colors),
    "current_color": [x for x in pygame.Color("green")]
}
step_speed = .4
total_step = step_speed * 60


def multicolor(img: pygame.Surface):
    datas["step"] += 1
    if datas["step"] < total_step:
        datas["current_color"] = [x + (((y - x) / total_step) * datas["step"]) for x, y in
                                  zip(pygame.color.Color(datas["base_color"]), pygame.color.Color(datas["next_color"]))]
    else:
        datas["step"] = 1
        datas["base_color"] = datas["next_color"]
        datas["next_color"] = next(colors)

    col = pygame.Color(datas["current_color"])

    for i in range(img.get_width()):
        for j in range(img.get_height()):
            if img.get_at((i, j)) != pygame.color.Color("black"):
                col.a = img.get_at((i, j)).a
                img.set_at((i, j), col)
    return img
