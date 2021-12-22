import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screenWidth = 1024
screenHeight = 768

screen = pygame.display.set_mode((screenWidth,screenHeight))

# Kreiranje lopte, igrača i protivnika
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30, 30)
player = pygame.Rect(screenWidth-10, screenHeight/2-70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2-70, 10, 140)

pygame.display.set_caption("Pong game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
