#  Cria o mapa apartir de caracteres | @ = nada / # = bloco / E = quebra linha
import pygame


def map(pg, display, inp, tam=20, inicial_pos=0):
    x = inicial_pos
    y = 0
    blocks = []
    for l in inp:
        if l == '#':
            blocks.append(pg.Rect(x, y, tam, tam))
        if l == 'E':
            x = inicial_pos-tam
            y += tam
        x += tam
    return blocks


from math import cos, sin

class Player(pygame.Rect):
    def __init__(self, x, y, tam, image, display):
        super().__init__(x, y, tam, tam)
        self.image = image
        self.image_norm = image
        self.angle = 0
        self.ds = display
        self.ray_angle = 0
        self.ray_instance = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        self.ds.blit(self.image, (self.x - int(self.image.get_height() / 2),
                                  self.y - int(self.image.get_width() / 2)))

        pygame.draw.rect(self.ds, (255, 255, 255), (self.x - 15, self.y - 15, self.width, self.height), 1)
        pygame.draw.rect(self.ds, (255, 0, 0), pygame.Rect(self.x+15, self.y+15, self.width, self.height), 2)

    def move_with_keys(self, colisores, velocity_angle=5, velocity_move=3):
        angle_keys = {1: pygame.key.get_pressed()[pygame.K_a],
                      -1: pygame.key.get_pressed()[pygame.K_d]}

        move_keys = {-1: pygame.key.get_pressed()[pygame.K_w],
                     1: pygame.key.get_pressed()[pygame.K_s]}

        for key in angle_keys:
            if angle_keys[key]:
                self.angle += key*velocity_angle

        move_axis = 0

        for key in move_keys:
            if move_keys[key]:
                move_axis = key

        angle_radian = (self.angle * 3.14) / 180

        velocity_x = move_axis * cos(angle_radian)
        velocity_y = move_axis * sin(angle_radian) * -1

        self.image = pygame.transform.rotate(self.image_norm, self.angle + 90)

        if pygame.Rect((self.x - 15),
                       (self.y - 15) + velocity_y*velocity_move,
                       self.width, self.height).collidelist(colisores) == -1:

            self.move_ip(0, velocity_y*velocity_move)

        if pygame.Rect((self.x - 15) + velocity_x * velocity_move,
                       (self.y - 15),
                       self.width, self.height).collidelist(colisores) == -1:

            self.move_ip(velocity_x*velocity_move, 0)

    def ray(self, colisores, fov=55, view_distance=200, separator=4):
        result = []
        self.ray_instance.x = self.x + (cos(self.angle))
        self.ray_instance.y = self.y + (sin(self.angle))

        color = 255 / view_distance

        for y in range(-fov, fov, 2):
            for x in range(0, view_distance, separator):
                self.ray_angle = (((self.angle + 90)+y) * 3.14) / 180

                a = (x * cos(self.ray_angle))
                b = (x * sin(self.ray_angle))

                pygame.draw.rect(self.ds, (0, 255, 0), (self.x - b, self.y - a, 2, 2))

                colisao = pygame.Rect(self.x - b,
                                      self.y - a,
                                      2, 2).collidelist(colisores) != -1

                if colisao:
                    result.append(255 - (color * x))
                    break

                if x >= view_distance-10:
                    result.append(0)
                    break

        while len(result) < 27:
            result.append(0)

        return result


