from pygame.sprite import Sprite
import pygame
import time
class Bullet(Sprite):
    def __init__(self, x, y, group):
        super().__init__()
        self.all_images = []
        for i in range(1, 6):
            img = pygame.image.load(f"assets/Bullet/Bullet ({i}).png")
            img = pygame.transform.scale_by(img, 0.3)
            self.all_images.append(img)

        self.image = self.all_images[0]
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        self.bip = pygame.mixer.Sound("assets/bip.wav")
    def update(self, jelly_group, score):
        self.rect.x += 10
        for jelly in jelly_group.sprites():
            if jelly.rect.colliderect(self.rect):
                self.kill()
                jelly.kill()
                self.bip.play()
                score += 1
   
        return score
        