import pygame
import os
from bullet import Bullet

class Airplane:
    def __init__(self, x,y, speed, ammo):
        self.all_images = {}
        self.animation_types = ("Fly", "Shoot", "Dead")
        for animation in self.animation_types:
            img_list = []
            for img_path in os.listdir(f"Plane/{animation}"):
                img = pygame.image.load(f"Plane/{animation}/{img_path}")
                img = pygame.transform.scale_by(img, 0.3)
                img_list.append(img)
            self.all_images[animation] = img_list

        self.image = self.all_images["Fly"][0]
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = 5
        self.ammo = ammo
        self.frame_index = 0
        self.animation = "Fly"
        self.time_left = 0
        self.bullet_group = pygame.sprite.Group()
        self.last_shoot_time = pygame.time.get_ticks()
    def draw(self, screen, jelly_group,score):
        screen.blit(self.image, self.rect)
        
        for bullet in self.bullet_group.sprites():

            score = bullet.update(jelly_group, score)
        
        
        self.bullet_group.draw(screen)
        self.do_animation()
        return score
    def do_animation(self):
        self.image = self.all_images[self.animation][self.frame_index]
        if pygame.time.get_ticks() - self.time_left >= 100:
            self.time_left = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.animation]):
                self.frame_index = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if keys[pygame.K_SPACE] and pygame.time.get_ticks() -self.last_shoot_time > 200:
            self.last_shoot_time = pygame.time.get_ticks()
            self.change_animation("Shoot")
            Bullet(self.rect.bottomright[0]-30, self.rect.bottomright[1]-40, self.bullet_group)
            print(len(self.bullet_group))
        else:
            self.change_animation("Fly")


    def change_animation(self, new_animation):
        if new_animation != self.animation:
            self.animation = new_animation
            self.frame_index = 0


    