from Space.objects import *
from Space.constants import *


class Engine:
    FPS = FPS
    pg = pygame
    pg.init()
    clock = pg.time.Clock()
    running = True
    objects = []

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))

    def render(self):
        self.screen.fill(BG_COLOR)
        for obj in self.objects:
            obj.render()
        self.pg.display.set_caption(str(self.clock.get_fps()))
        self.pg.display.update()

    def check_input_keys(self):
        for event in self.pg.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = self.pg.key.get_pressed()
        if keys[self.pg.K_ESCAPE]:
            self.running = False
        for obj in self.objects:
            obj.input_keys(keys)

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.check_input_keys()
            self.render()
