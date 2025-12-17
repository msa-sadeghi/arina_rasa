import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 640
miki = pygame.image.load("mini.png")
miki = pygame.transform.scale_by(miki, 0.5)
miki_rect = miki.get_rect(topleft= (100, 300))
cheese_image = pygame.image.load("cheese.png")
cheese_image = pygame.transform.scale_by(cheese_image, 0.3)
apple_image = pygame.image.load("apple.png")
apple_image = pygame.transform.scale_by(apple_image, 0.3)

random_x = random.randint(100, 500)
cheese_rect = cheese_image.get_rect(topleft=(random_x, -100))
random_x = random.randint(100, 500)
apple_rect = apple_image.get_rect(topleft=(random_x, -100))


f = pygame.font.Font("font.ttf", 24)
cheese = 0
cheese_text  = f.render(f"cheese  {cheese}", True, "green")
apple = 0
apple_text  = f.render(f"apple  {apple}", True, "green")

sound1 = pygame.mixer.Sound("sound (1).wav")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        miki_rect.x -= 7
    if keys[pygame.K_RIGHT]:
        miki_rect.x += 7
    cheese_text  = f.render(f"cheese  {cheese}", True, "green")
    apple_text  = f.render(f"apple  {apple}", True, "green")
    screen.fill((0,0,0))
    screen.blit(miki, miki_rect)
    screen.blit(cheese_image, cheese_rect)
    screen.blit(apple_image, apple_rect)
    screen.blit(cheese_text, (10, 10))
    screen.blit(apple_text, (10, 40))
    if miki_rect.colliderect(cheese_rect) or cheese_rect.bottom >= HEIGHT:
        random_x = random.randint(100, 500)
        cheese_rect.topleft = (random_x, -100)
        cheese += 1
        sound1.play()
    if miki_rect.colliderect(apple_rect) or apple_rect.bottom >= HEIGHT:
        random_x = random.randint(100, 500)
        apple_rect.topleft = (random_x, -100)
        apple += 1

    cheese_rect.y += 5
    apple_rect.y += 5
    pygame.display.update()
    CLOCK.tick(FPS)
