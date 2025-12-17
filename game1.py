import pygame
import random
pygame.init()
window = pygame.display.set_mode((600, 480))
r = 0 
g = 0 
b = 0 
counter =  0
mini_left = pygame.image.load("mini.png")
mini_left = pygame.transform.scale_by(mini_left, 0.2)
mini_right = pygame.transform.flip(mini_left, True, False)
rect = mini_left.get_rect(center=(300,  240))
FPS = 60
clock = pygame.time.Clock()
direction = "right"
mouse_down = False
is_turned = False
while True:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN and counter < 10:
            
        #     r = random.randint(0, 255)
        #     g = random.randint(0, 255)
        #     b = random.randint(0, 255)
        #     counter +=  1
    
    if pygame.mouse.get_pressed()[0]:
        mouse_down = True
        mouse_pos = pygame.mouse.get_pos()    
        pygame.draw.circle(window, "green", mouse_pos, 50)

    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_UP] and rect.top >= 0:
        rect.y -=  5
    elif keys[pygame.K_DOWN] and rect.bottom <= 480:
        rect.y +=  5
    if keys[pygame.K_LEFT] and rect.left >= 0:
        rect.x -=  5
        direction = "left"
    elif keys[pygame.K_RIGHT] and rect.right <= 600:
        rect.x +=  5
        direction =  "right"

    if direction == "right":
        
        mini = mini_right
    else:
        mini = mini_left
    # window.fill((r, g, b))
    window.blit(mini, rect)
    pygame.display.flip()