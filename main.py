import pygame, sys

def ballAnimation():
    global ballSpeedX, ballSpeedY

    # Animacija kretanja lopte
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Postavljanje granica terena za loptu
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= screenWidth:
        ballRestart() # sudaranje s lijevim ili desnim zidom 

    # Sudaranje lopte sa igracem i s protivnikom
    if ball.colliderect(player) or ball.colliderect(opponent):
        # ballSpeedX = -1 * ballSpeedX
        ballSpeedX *= -1


def playerAnimation():
    # Kretanje playera
    player.y += playerSpeed

    # Granice terena za igraca
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def opponentAnimation():
    global opponentSpeed
    # opponent.y += opponentSpeed

    # Granice terena za protivnika
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight
    
    # Kretanje uz loptu
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        opponent.top -= opponentSpeed

def ballRestart():
    ball.center = (screenWidth/2, screenHeight/2)

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

# Brzine lopte po osi
ballSpeedX = 7
ballSpeedY = -7
playerSpeed = 0 # prvo vrijednost 0, objekt se ne kreće, zatim vrijednost 7
opponentSpeed = 7 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7 # napraviti samo ovu, stisnit i odmah pustit tipku i pokazati
            if event.key == pygame.K_UP:
                playerSpeed -= 7 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7
        

    # Iscrtavanje objekata
    screen.fill(bgColor)
    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opponent)
    pygame.draw.ellipse(screen, lightGrey, ball)
    pygame.draw.aaline(screen, lightGrey, (screenWidth/2,0), (screenWidth/2,screenHeight))

    # Funckije za animaciju
    ballAnimation()
    playerAnimation()
    opponentAnimation()
    

    pygame.display.flip()
    clock.tick(60)