from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, x, y, group):
        super().__init__()
        self.all_images = []
        for i in range(1, 6):
            img = pygame.image.load(f"Bullet/Bullet ({i}).png")
            self.all_images.append(img)

        self.image = self.all_images[0]
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)

        