from pygame.sprite import Sprite
import pygame
import random
class Jelly(Sprite):
    def __init__(self, image, x,y, group):
        super().__init__()
        self.image = pygame.transform.scale_by(image, 0.2)
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)

    def update(self, plane):
        if plane.rect.colliderect(self.rect):
            self.kill()
            plane.health -= 1

        self.rect.x -= random.randint(1,3)
        if self.rect.x <= 0:
            self.kill()