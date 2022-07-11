import pygame
from Space.matrix import *
from Space.constants import SCALE, CUBE_COLOR_1, ROTATE_ANGLE
from Space import constants


class Object4D:
    def __init__(self, engine, object_name):
        self.engine = engine
        self.reference = constants.__dict__[object_name]
        self.vertexes = np.array(self.reference["vertexes"]) * SCALE
        self.vertexes[:, -1] = 1
        self.faces = np.array(self.reference["faces"])
        self.CENTER_W = self.engine.screen.get_width() // 2
        self.CENTER_H = self.engine.screen.get_height() // 2
        self.reset_vertexes()

    def get_object_center(self):
        return [self.vertexes[:, i].mean() for i in range(self.vertexes.shape[1] - 1)]

    def move(self, dx, dy, dz, dw):
        self.vertexes = self.vertexes @ move(dx, dy, dz, dw)

    def rotate(self, axis, a=0.04):
        self.vertexes = self.vertexes @ rotate(axis, a)

    def project(self, dots):
        drawable_dots = []
        M = move(self.CENTER_W, self.CENTER_H, 0, 0)
        for dot in dots:
            a = dot @ P1
            a = a @ P0  # projection
            a /= a[-1]  # normalization
            a = a @ M  # move to screen center
            drawable_dots.append([a[0], a[1]])
        return drawable_dots

    def reset_vertexes(self):
        self.vertexes = np.array(self.reference["vertexes"]) * SCALE
        self.vertexes[:, -1] = 1
        # move to start of global coordinates
        dx, dy, dz, dw = self.get_object_center()
        self.move(-dx, -dy, -dz, -dw)

    def input_keys(self, keys):
        pg = self.engine.pg
        a = -ROTATE_ANGLE if keys[pg.K_MINUS] else ROTATE_ANGLE
        if keys[pg.K_q]:
            self.rotate("xw", a)
        if keys[pg.K_w]:
            self.rotate("yw", a)
        if keys[pg.K_e]:
            self.rotate("zw", a)
        if keys[pg.K_a]:
            self.rotate("xy", a)
        if keys[pg.K_s]:
            self.rotate("xz", a)
        if keys[pg.K_d]:
            self.rotate("yz", a)
        if keys[pg.K_SPACE]:
            self.reset_vertexes()

    def test(self):
        dx, dy, dz, dw = self.get_object_center()
        # print(self.vertexes[0])
        self.move(-dx, -dy, -dz, -dw)
        self.rotate("xw", -0.01)  # standard
        self.rotate("yw", 0.01)  # standard
        self.rotate("zw", 0.01)  # standard
        self.rotate("xy", 0.01)
        self.rotate("xz", 0.01)
        self.rotate("yz", 0.01)
        self.move(dx, dy, dz, -dw)
        self.move(0, 0, 0, 0)

    def render(self):
        dots = self.vertexes.copy()
        # self.test()  # funny math manipulations
        drawable_dots = self.project(dots)
        for face in self.faces:
            draw_dots = []
            for vertex in face:
                draw_dots.append(drawable_dots[vertex])
            pygame.draw.lines(self.engine.screen, CUBE_COLOR_1, True, draw_dots, 2)
