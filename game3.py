import pygame
pygame.init()
import random
from plane import Airplane
from jelly import Jelly
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
bg_image = pygame.image.load("BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
plane1 = Airplane(90, 200, 10, 50)
jelly1_image = pygame.image.load("NoShadow/Jelly (1).png")
jelly2_image = pygame.image.load("NoShadow/Jelly (2).png")
jelly3_image = pygame.image.load("NoShadow/Jelly (3).png")
jelly4_image = pygame.image.load("NoShadow/Jelly (4).png")
jelly5_image = pygame.image.load("NoShadow/Jelly (5).png")
jelly6_image = pygame.image.load("NoShadow/Jelly (6).png")
jelly_images_list = [
    jelly1_image,
    jelly2_image,
    jelly3_image,
    jelly4_image,
    jelly5_image,
    jelly6_image
]
jelly_number = 0
jelly_group = pygame.sprite.Group()
jelly1 = Jelly(jelly1_image, WIDTH- 100, random.randint(50, HEIGHT - 50), jelly_group)

score = 0
f  = pygame.font.SysFont("arial", 24)
score_text = f.render(f"score: {score}", True, "darkgreen")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0,0))
    score_text = f.render(f"score: {score}", True, "darkgreen")
    screen.blit(score_text, (40, 40))
    score = plane1.draw(screen, jelly_group, score)
    plane1.move()
    jelly_group.draw(screen) 
    if len(jelly_group) == 0:
        for i in range(random.randint(1,6)):
            Jelly(jelly_images_list[random.randint(0, 5)], WIDTH- 100, random.randint(50, HEIGHT - 50), jelly_group)
    jelly_group.update()
    pygame.display.update()