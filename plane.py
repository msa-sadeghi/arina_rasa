import pygame
import os
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
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.do_animation()
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

        if keys[pygame.K_SPACE]:
            self.change_animation("Shoot")
        else:
            self.change_animation("Fly")


    def change_animation(self, new_animation):
        if new_animation != self.animation:
            self.animation = new_animation
            self.frame_index = 0


    