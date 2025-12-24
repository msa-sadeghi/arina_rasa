import pygame
pygame.init()

from plane import Airplane
WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

bg_image = pygame.image.load("BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

plane1 = Airplane(90, 200, 10, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0,0))
    plane1.draw(screen)
    plane1.move()
    pygame.display.update()