import pygame 
pygame.init()

from player import Player

WIDTH = 1024
HEIGHT = 640 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60 
clock = pygame.time.Clock()

my_player = Player("cat", 100, 200, 5, 3)

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                my_player.change_character("cat")
            if event.key == pygame.K_d:
                my_player.change_character("dog")
    screen.fill((0,0,0))
    my_player.draw(screen)
    my_player.move()

    pygame.display.update()
    clock.tick(60)