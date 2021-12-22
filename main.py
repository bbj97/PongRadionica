import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screenWidth = 1024
screenHeight = 768

screen = pygame.display.set_mode((screenWidth,screenHeight))

# Kreiranje lopte, igrača i protivnika
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30, 30)
player = pygame.Rect(screenWidth-20, screenHeight/2-70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2-70, 10, 140)


#otvoriti paletu boja
bgColor = pygame.Color('grey12')
lightGrey = (200,200,200)

pygame.display.set_caption("Pong game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # vizualizacije
    screen.fill(bgColor)
    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opponent)
    pygame.draw.ellipse(screen, lightGrey, ball)
    pygame.draw.aaline(screen, lightGrey, (screenWidth/2,0), (screenWidth/2,screenHeight))


    pygame.display.flip()
    clock.tick(60)
