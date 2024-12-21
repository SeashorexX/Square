from turtle import speed
import pygame 
pygame.init()

SCREEN_WIDTH = 900 
SCREEN_HEIGHT = 500

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

x,y = 200, 400
square_size = 80
speed = 10

BLACK = (0,0,0)
BLUE = (0,0, 255)

square = True
game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    arrows = pygame.key.get_pressed()

    if arrows[pygame.K_UP] and y - speed >= 0:
        y -= speed
    if arrows[pygame.K_DOWN] and y + speed + square_size <= SCREEN_HEIGHT:
        y += speed
    if arrows[pygame.K_LEFT] and x - speed >= 0:
        x -= speed
    if arrows[pygame.K_RIGHT] and x + speed + square_size <= SCREEN_WIDTH:
        x += speed

    window.fill(BLACK)

    pygame.draw.rect(window, BLUE, (x,y, square_size, square_size))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()

