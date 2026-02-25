import pygame
import os 
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self,type, x,y, speed, health):
        self.all_images = {}
        self.type = type
        self.animation_types = ("Fall", "Hurt", "Dead", 'Idle', 'Jump', 'Run', 'Slide', 'Walk')
        for t in ("cat", "dog"):
            images_dict = {}
            for animation in self.animation_types:
                img_list = []                
                for img_path in os.listdir(f"{t}/{animation}"):
                    img = pygame.image.load(f"{t}/{animation}/{img_path}")
                    img = pygame.transform.scale_by(img, 0.3)
                    img_list.append(img)
                images_dict[animation] = img_list
            self.all_images[t] = images_dict
        self.image = self.all_images[self.type]["Idle"][0]
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = 5
        self.health = 10
        self.frame_index = 0
        self.animation = "Idle"
        self.time_left = 0
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


    def change_character(self, new_type):
        self.type = new_type
        self.image = self.all_images[self.type][self.animation][0]