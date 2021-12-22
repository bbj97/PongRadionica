import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screenWidth = 1024
screenHeight = 768

screen = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Pong game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
    